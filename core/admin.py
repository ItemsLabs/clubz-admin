from datetime import timedelta

from django import forms
from django.db import models
from django.conf import settings
from django.contrib import admin, messages
from django.contrib.admin import SimpleListFilter
from django.contrib.admin.widgets import AutocompleteSelect
from django.core.exceptions import ValidationError
from django.db import transaction
from django.forms import BaseInlineFormSet
from django.http import HttpResponseRedirect
from django.utils import timezone, html
from django.utils.safestring import mark_safe
from django.conf import settings
from django.shortcuts import render, redirect
from core.notifications import send_push_to_user, send_push_to_all
from core import const
from core.models import AppInbox, AssignedCardPack, CustomUser, NftBucket, Rewards, Team, Match, Player, Game, Action, PowerUp, PowerUpAction, MatchReward, \
    CompetitionConfig, Competition, MatchLeaderboard, Transactions, BanPenalty, CompetitionEdition, CompetitionPhase, \
    ManualSubscription, DataFeedSimModel, MatchEvent, OptaFeedItem, OptaFeedItemVersion, GameEvent, GamePowerUp, \
    StoreProduct, StoreProductTransactions, DivisionReward, UserDivision, UserGameWeekHistory, GameWeek, Division, \
    GameSeason, CardPackType

from soccer_wiki.models import SoccerWikiPlayer
from core import commands
from opta.sync import sync_feed
import uuid
from csvexport.actions import csvexport
from django import forms
from core.models import CustomUser
from django.urls import path


class NotificationForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter notification title'}), label="Title")
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter notification message'}), label="Message")
    user_ids = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter comma-separated user IDs'}),
        required=False,
        label="User IDs (comma-separated)"
    )

class BanPenaltiesInline(admin.TabularInline):
    model = BanPenalty
    readonly_fields = ('start_time',)
    ordering = ('-start_time',)
    extra = 0
    fields = ('start_time', 'end_time', 'reason',)

class UserGameWeekHistoriesInline(admin.TabularInline):
    model = UserGameWeekHistory
    extra = 0  # Number of empty forms to display
    readonly_fields = ('week_division_position', 'week_division_tier', 'week_points', 'week_coins','new_division_tier', 'status')
    fields = ('week_division_position', 'week_division_tier', 'week_points', 'week_coins', 'new_division_tier', 'status')

class DivisionsInline(admin.TabularInline):
    model = UserDivision
    extra = 0  # Number of empty forms to display
    fields = ('game_week_name', 'division_tier')
    readonly_fields = ('game_week_name', 'division_tier')

    def game_week_name(self, obj):
        return obj.game_week.name
    game_week_name.short_description = 'Week period'

    def division_tier(self, obj):
        return obj.division.tier
    division_tier.short_description = 'Division Tier'

class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CustomUser._meta.fields]
    list_filter = (
        'verified', 'subscription_tier', 'moderator', 'premium', 'influencer',
        'email_verified', 'name_changed', 'last_name_change', 'created_at', 'updated_at',
    )
    search_fields = (
        'name', 'email', 'paypal_email', 'firebase_id', 'referral_code',
        'wallet_address', 'sequence_session_id', 'verification_token'
    )
    fields = [field.name for field in CustomUser._meta.fields if field.name not in ('id', 'password')]
    readonly_fields = (
        'firebase_id', 'balance', 'referral_code', 'referrer_id', 'created_at', 'updated_at'
    )
    ordering = ('-created_at',)
    inlines = (BanPenaltiesInline, UserGameWeekHistoriesInline, DivisionsInline)
    autocomplete_fields = ('referrer',)


    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('send-notification/', self.admin_site.admin_view(self.send_notification), name='send-notification'),
        ]
        return custom_urls + urls

    def send_notification(self, request):
        if request.method == 'POST':
            form = NotificationForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                message = form.cleaned_data['message']
                user_ids = form.cleaned_data['user_ids']
                if not user_ids:
                    send_push_to_all.delay(title, message)
                else:
                    user_id_list = user_ids.split(',')
                    for user_id in user_id_list:
                        try:
                            user = CustomUser.objects.get(id=user_id.strip())
                            if user.firebase_id and user.firebase_id.startswith("Expo"):
                                send_push_to_user.delay(user.id, title, message)
                        except CustomUser.DoesNotExist:
                            continue
                messages.success(request, "Notification tasks have been initiated.")
                return redirect('..')
        else:
            form = NotificationForm()

        return render(request, '../templates/notifications.html', {'form': form})




class CompetitionConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'filter', 'enabled', 'sport')
    fields = ('sport', 'name', 'filter', 'enabled')
    def save_model(self, request, obj, form, change):
        if form.is_valid():
            competition = obj.related_competition
            if competition is not None:
                competition.enabled = obj.enabled
                competition.save()
        super().save_model(request, obj, form, change)



class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_name', 'code','enabled')
    fields = ('name', 'code', 'short_name','enabled')
    readonly_fields = ('name', 'code',)


class CompetitionEditingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'competition', 'import_id')
    list_filter = ('competition',)
    search_fields = ('name', 'import_id')
    fields = ('import_id', 'name', 'competition', 'enabled',)
    readonly_fields = ('import_id', 'name', 'competition',)

    def has_change_permission(self, request, obj=None):
        return True


class CompetitionPhaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'import_id', 'competition_name')
    list_filter = ('competition_edition__competition',)
    search_fields = ('name', 'import_id')

    def competition_name(self, obj):
        return obj.competition_edition.competition.name

    competition_name.short_description = 'Competition'

    def has_change_permission(self, request, obj=None):
        return False


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_name', 'abbr')
    search_fields = ('id', 'name', 'short_name', 'abbr',)
    fields = ('short_name', 'abbr', 'crest_url', 'name', 'country', 'region')
    readonly_fields = ('name', 'country', 'region',)


class IsSimulationFilter(SimpleListFilter):
    title = 'Is Simulated'
    parameter_name = 'is_simulated'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'Yes':
            return queryset.exclude(simulation_from_match__isnull=True)
        elif value == 'No':
            return queryset.filter(simulation_from_match__isnull=True)
        return queryset


class MatchTimeFilter(SimpleListFilter):
    title = 'Match Time'
    parameter_name = 'match_time'

    def lookups(self, request, model_admin):
        return (
            ('today', 'Today'),
            ('past_7_days', 'Past 7 days'),
            ('next_7_days', 'Next 7 days'),
        )

    def queryset(self, request, queryset):
        now = timezone.now()
        start = now.replace(hour=0, minute=0, second=0)

        value = self.value()
        if value == 'today':
            return queryset.filter(match_time__gte=start, match_time__lt=start + timedelta(hours=24))
        elif value == 'past_7_days':
            return queryset.filter(match_time__gte=start - timedelta(days=7), match_time__lt=start)
        elif value == 'next_7_days':
            return queryset.filter(match_time__gte=start, match_time__lt=start + timedelta(days=7))
        return queryset


class CompetitionFilter(SimpleListFilter):
    title = 'Competition'
    parameter_name = 'competition'

    def lookups(self, request, model_admin):
        return tuple((c.pk, c.name) for c in Competition.objects.order_by('name'))

    def queryset(self, request, queryset):
        value = self.value()

        if value:
            return queryset.filter(competition=value)
        return queryset


class MatchRewardFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        positions = []
        for form in self.forms:
            if form.cleaned_data and not form.cleaned_data.get('DELETE', False):
                min_position = form.cleaned_data.get('min_position')
                max_position = form.cleaned_data.get('max_position')
                if min_position is not None:
                    positions.append((min_position, max_position))
        print(positions)
        if not commands.validate_positions(positions):
            raise ValidationError(
                "Invalid position ranges. Please ensure there are no gaps and min_position is less than or equal to "
                "max_position.")

class MatchRewardInline(admin.TabularInline):
    model = MatchReward
    extra = 1  # Number of empty forms to display

    fields = ('min_position', 'max_position', 'amount', 'game', 'lapt', 'event', 'balls', 'signed_balls', 'shirts', 'signed_shirts', 'kickoff_pack_1', 'kickoff_pack_2', 'kickoff_pack_3', 'season_pack_1', 'season_pack_2', 'season_pack_3')
    ordering = ('min_position',)


class MatchAdmin(admin.ModelAdmin):
    def toggle_enabled(self, request, queryset):
        for match in queryset:
            match.enabled = not match.enabled
            match.save()

    toggle_enabled.short_description = "Toggle enabled status of selected matches"

    list_display = ('enabled', 'import_id', 'home_team', 'away_team',
                    'status', 'match_time', 'competition_name',
                    'is_simulated', 'leaderboard_link',)
    list_display_links = ('import_id',)
    list_filter = ('enabled', IsSimulationFilter, 'match_type', MatchTimeFilter, 'status', CompetitionFilter)
    search_fields = ('id', 'import_id',)
    inlines = (MatchRewardInline,)
    change_form_template = "match_change.html"
    ordering = ('-match_time',)
    actions = [toggle_enabled]

    def response_change(self, request, obj):
        if "_start-short-simulation" in request.POST:
            obj.create_simulation(duration=timedelta(minutes=10))
            self.message_user(request, "Simulation successfully started")
            return HttpResponseRedirect(".")
        elif "_start-long-simulation" in request.POST:
            obj.create_simulation(duration=timedelta(minutes=90))
            self.message_user(request, "Simulation successfully started")
            return HttpResponseRedirect(".")

        return super().response_change(request, obj)

    def get_readonly_fields(self, request, obj=None):
        return [f.name for f in self.model._meta.fields if f.name != 'match_type']

    def is_simulated(self, obj):
        return obj.simulation_from_match is not None

    def competition_name(self, obj):
        return obj.competition.name

    def leaderboard_link(self, obj):
        return mark_safe(
            '<a href="/admin/core/matchleaderboard/?match_id={}" target="_blank">Leaderboard</a>'.format(obj.pk))

    leaderboard_link.short_description = 'Leaderboard'


class PlayerAdmin(admin.ModelAdmin):
    search_fields = ('id', 'full_name', 'first_name', 'last_name', 'nick_name',)
    list_display = ('id', 'first_name', 'last_name', 'nick_name', 'soccer_wiki_player_id',)
    autocomplete_fields = ('soccer_wiki_player',)


class SoccerWikiPlayerAdmin(admin.ModelAdmin):
    search_fields = ('import_id', 'first_name', 'second_name')
    list_display = ('id', 'first_name', 'second_name', 'import_id', 'internal_image_url')


class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'match_id',)
    readonly_fields = ('match', 'user',)


class ActionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'score', 'category', 'nft_category')
    ordering = ('ordering',)


class PowerUpActionInline(admin.TabularInline):
    model = PowerUpAction
    ordering = ('ordering',)


class StoreProductAdmin(admin.ModelAdmin):
    list_display = ('store_product_id', 'description', 'price', 'currency', 'google_product_id', 'apple_product_id')
    ordering = ('id', 'store_product_id', 'price', 'currency')
    actions = [csvexport]
    csvexport_export_fields = [
        'store_product_id',
        'price',
        'currency',
        'google_product_id',
        'apple_product_id',
    ]
    csvexport_selected_fields = [
        'store_product_id',
        'price',
        'currency',
        'google_product_id',
        'apple_product_id',
    ]

class PowerUpAdmin(admin.ModelAdmin):
    list_display = ('name', 'sport')
    ordering = ('id',)
    inlines = [PowerUpActionInline]


class MatchLeaderboardAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_email', 'position', 'score', 'get_match')
    ordering = ('position',)
    actions = [csvexport]
    csvexport_export_fields = [
        'user.name',
        'user.email',
        'position',
        'score',
        'user.verified',
        'match.id',
    ]
    csvexport_selected_fields = [
        'user.name',
        'user.email',
        'position',
        'score',
        'user.verified',
        'match.id',
    ]

    def get_match(self, obj):
        if obj.match is not None:
            label =  f"{obj.match}"
            return html.format_html(f'<a href="/admin/core/match/{obj.match_id}/change/">{label}</a>')
        return html.format_html('<a href="/admin/core/match/{}/change/">No match set</a>', obj.match_id)
    get_match.short_description = 'Match'

    def get_queryset(self, request):
        qs = super(MatchLeaderboardAdmin, self).get_queryset(request)
        return qs.select_related('user')

    def user_name(self, obj):
        return '{} ({})'.format(obj.user.name, obj.user_id)

    def user_email(self, obj):
        return '{}'.format(obj.user.email)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class ObjectTypeFilter(SimpleListFilter):
    title = 'Object Type'
    parameter_name = 'object_type'

    def lookups(self, request, model_admin):
        return Transactions.OBJECT_TYPE

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(object_type=self.value())
        return queryset

class DeliveredFilter(SimpleListFilter):
    title = 'Delivered Status'
    parameter_name = 'delivered'

    def lookups(self, request, model_admin):
        return (
            ('True', 'Delivered'),
            ('False', 'Not Delivered'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'True':
            return queryset.filter(delivered=True)
        elif self.value() == 'False':
            return queryset.filter(delivered=False)
        return queryset

class UnclaimedPrizesFilter(SimpleListFilter):
    title = 'Unclaimed Prizes'
    parameter_name = 'unclaimed'

    def lookups(self, request, model_admin):
        return (
            ('undelivered', 'Undelivered'),
            ('unsent', 'Unsent'),
            ('both', 'Undelivered & Unsent'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'undelivered':
            return queryset.filter(delivered=False)
        elif value == 'unsent':
            return queryset.filter(sent=False)
        elif value == 'both':
            return queryset.filter(delivered=False, sent=False)
        return queryset


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'user_name', 'amount', 'object_type', 'quantity', 'delivered', 'sent')
    list_filter = (ObjectTypeFilter, DeliveredFilter, UnclaimedPrizesFilter, 'created_at')
    search_fields = ('user__name', 'user__email', 'blockchain_uuid', 'text')
    ordering = ('-created_at',)

    # Make 'delivered' and 'sent' fields editable in both the list and detail view
    list_editable = ('delivered', 'sent')

    # Include 'delivered' and 'sent' fields in the detail view
    fields = ('user', 'amount', 'object_type', 'quantity', 'delivered', 'sent')

    # Ensure these fields are editable and not readonly
    def get_readonly_fields(self, request, obj=None):
        return []

    def user_name(self, obj):
        return f'{obj.user.name} ({obj.user_id})'

    # Optionally, you can override save_model to include any custom logic if needed
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

class ManualSubscriptionForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        CustomUser.objects.all(), required=True,
        widget=AutocompleteSelect(ManualSubscription.user.field.remote_field, admin.site),
    )
    subscription_duration = forms.ChoiceField(choices=(
        (i + 1, '{} Month ({}$)'.format(i + 1, (i + 1) * settings.PREMIUM_SUBSCRIPTION_PRICE))
        for i in range(12)
    ), required=True, label='Subscription Duration')

    def clean(self):
        duration_in_months = int(self.cleaned_data['subscription_duration'])
        amount = settings.PREMIUM_SUBSCRIPTION_PRICE * duration_in_months

        with transaction.atomic():
            locked_user = CustomUser.objects.select_for_update().get(pk=self.cleaned_data['user'].pk)
            if locked_user.balance < amount:
                raise ValidationError('Not enough money on balance')

    class Meta:
        model = ManualSubscription
        exclude = ['expires_at', 'tier']


class ManualSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'user_name', 'tier', 'expires_at', 'transaction_amount')
    autocomplete_fields = ('user',)
    ordering = ('-created_at',)
    search_fields = ('user__name',)

    def user_name(self, obj):
        return '{} ({})'.format(obj.user.name, obj.user_id)

    def transaction_amount(self, obj):
        return obj.transaction.first().amount

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_form(self, request, obj=None, change=False, **kwargs):
        if obj:
            return super(ManualSubscriptionAdmin, self).get_form(request, obj, change, **kwargs)
        # use custom form only for `add` action
        return ManualSubscriptionForm

    def save_model(self, request, obj, form, change):
        # calculate expires at and amount to be written off
        duration_in_months = int(form.cleaned_data['subscription_duration'])
        obj.expires_at = timezone.now() + timedelta(days=30 * duration_in_months)
        obj.tier = const.TIER_PREMIUM
        amount = settings.PREMIUM_SUBSCRIPTION_PRICE * duration_in_months

        with transaction.atomic():
            locked_user = CustomUser.objects.select_for_update().get(pk=obj.user.pk)
            if locked_user.balance < amount:
                raise ValidationError('Not enough money on balance')

            print('Amount if', amount)

            super().save_model(request, obj, form, change)
            # insert transaction pointing to subscription
            Transactions.objects.create(
                user=locked_user,
                amount=-amount,
                text='Manual subscription',
                manual_subscription=obj,
                delivered=True,
            )
            locked_user.update_premium()


class MatchInline(admin.TabularInline):
    model = Match

class DataFeedSimAdmin(admin.ModelAdmin):
    list_display = ('id', 'import_id', 'get_match', 'processed')

    def get_match(self, obj):
        if obj.match is not None:
            label =  f"{obj.match}"
            return html.format_html(f'<a href="/admin/core/datafeedsimmodel/{obj.id}/change/">{label}</a>')
        return html.format_html('<a href="/admin/core/datafeedsimmodel/{}/change/">No match set</a>', obj.id)
    get_match.short_description = 'Match'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'match':
            kwargs["queryset"] = Match.objects.filter(
                    simulation_from_match_id__isnull=False
                ).order_by("-match_time")  # We just need simulated matches only
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            matchtmp = obj.match
            if obj.import_id is None:
                obj.import_id = matchtmp.get_import_id()
            if (obj.import_id is not None and obj.import_id != "") and \
                (obj.json_events is None or obj.json_events == "" or obj.json_events == "null"):
                obj.json_events = settings.OPTA_CLIENT.get_match_events(obj.import_id)
                obj.processed = False
            if not obj.processed:
                if matchtmp.import_id is None:
                    matchtmp.import_id = f"simulation-{uuid.uuid4()}-{obj.import_id}"
                # cleanup game events
                obj.match.status = "g"
                obj.match.save()
                MatchEvent.objects.filter(match=obj.match).delete()
                optaItems = OptaFeedItem.objects.filter(match=obj.match)
                OptaFeedItemVersion.objects.filter(item__in=optaItems).delete()
                optaItems.delete()
                GameEvent.objects.filter(game__in=Game.objects.filter(match=obj.match)).delete()
                GamePowerUp.objects.filter(game__in=Game.objects.filter(match=obj.match)).delete()
                # sync feed again
                sync_feed(matchtmp, obj.json_events, True)
                obj.processed = True
                messages.success(request, "Events has been processed.")
            super().save_model(request, obj, form, change)

class InboxForm(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)
    user_ids = forms.CharField(
        required=False,
        help_text="Comma-separated list of user IDs to send the inbox message to. Leave blank to send to all users."
    )
    status = forms.ChoiceField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')])
    priority = forms.ChoiceField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    category = forms.ChoiceField(choices=[('Update', 'Update'), ('Reward', 'Reward')])
    image_url = forms.URLField(required=False)
    link_url = forms.URLField(required=False)
    
@admin.register(AppInbox)
class AppInboxAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'category', 'user', 'created_at', 'read')
    
    def send_inbox_message(self, request):
        if request.method == 'POST':
            form = InboxForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                user_ids = form.cleaned_data['user_ids']
                status = form.cleaned_data['status']
                priority = form.cleaned_data['priority']
                category = form.cleaned_data['category']
                image_url = form.cleaned_data['image_url']
                link_url = form.cleaned_data['link_url']
                
                if not user_ids:
                    # Send to all users
                    users = CustomUser.objects.all()
                else:
                    user_id_list = [user_id.strip() for user_id in user_ids.split(',')]
                    users = CustomUser.objects.filter(id__in=user_id_list)

                for user in users:
                    AppInbox.objects.create(
                        title=title,
                        description=description,
                        status=status,
                        priority=priority,
                        category=category,
                        image_url=image_url,
                        link_url=link_url,
                        user=user,
                    )
                
                messages.success(request, "Inbox messages have been successfully sent.")
                return redirect('..')
        else:
            form = InboxForm()

        return render(request, '../templates/send_inbox_message.html', {'form': form})

    # Register the admin action
    actions = [send_inbox_message]

@admin.register(UserDivision)
class UserDivisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'division', 'game_week', 'join_date')
    search_fields = ('user__username', 'division__name', 'game_week__name', 'user_id')
    list_filter = ('division', 'game_week')

@admin.register(UserGameWeekHistory)
class UserGameWeekHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'game_week', 'week_division', 'week_division_position', 'week_division_tier',
        'week_points', 'week_coins', 'new_division', 'new_division_tier', 'status'
    )
    search_fields = ('user__username', 'game_week__name', 'week_division__name', 'new_division__name')
    list_filter = ('game_week', 'week_division', 'new_division', 'status')


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'tier', 'percentage', 'relegation_min_range', 'relegation_max_range', 'promotion_min_range', 'promotion_max_range',  'updated_at',)
    search_fields = ('id', 'name',)
    list_filter = ('tier',)

@admin.register(GameSeason)
class GameSeasonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_at', 'end_at','created_at')
    search_fields = ('name',)

@admin.register(CardPackType)
class CardPackTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'card_pack_code', 'description', 'image', 'tier1', 'tier2', 'tier3', 'tier4', 'tier5', 'created_at')
    search_fields = ('name',)

@admin.register(NftBucket)
class NftBucketAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'team_id', 'age', 'game_position', 'position', 'nationality', 
        'common_limit', 'uncommon_limit', 'rare_limit', 'ultra_rare_limit', 'legendary_limit',
    )
    search_fields = ('name', 'team_id', 'nationality', 'position', 'game_position',)
    list_filter = ('game_position', 'position', 'team_id',)

    def player_name(self, obj):
        return f"{obj.name}"

    player_name.short_description = 'Player Name'

class DivisionRewardForm(forms.ModelForm):
    credits = forms.FloatField(label="Credits")
    game_token = forms.FloatField(label="Game Token")
    lapt_token = forms.FloatField(label="Lapt Token")
    event_tickets = forms.IntegerField(label="Event Tickets")
    ball = forms.IntegerField(label="Ball")
    signed_ball = forms.IntegerField(label="Signed Ball")
    shirt = forms.IntegerField(label="Shirt")
    signed_shirt = forms.IntegerField(label="Signed Shirt")
    kickoff_pack_1 = forms.IntegerField(label="Kickoff Pack 1", required=False)
    kickoff_pack_2 = forms.IntegerField(label="Kickoff Pack 2", required=False)
    kickoff_pack_3 = forms.IntegerField(label="Kickoff Pack 3", required=False)
    season_pack_1 = forms.IntegerField(label="Season Pack 1", required=False)
    season_pack_2 = forms.IntegerField(label="Season Pack 2", required=False)
    season_pack_3 = forms.IntegerField(label="Season Pack 3", required=False)

    class Meta:
        model = DivisionReward
        fields = ['week', 'division', 'min_position', 'max_position']  # Exclude 'reward'

    def __init__(self, *args, **kwargs):
        super(DivisionRewardForm, self).__init__(*args, **kwargs)
        
        # Ensure reward exists before accessing it
        if self.instance and self.instance.reward:
            self.fields['credits'].initial = self.instance.reward.credits
            self.fields['game_token'].initial = self.instance.reward.game_token
            self.fields['lapt_token'].initial = self.instance.reward.lapt_token
            self.fields['event_tickets'].initial = self.instance.reward.event_tickets
            self.fields['ball'].initial = self.instance.reward.ball
            self.fields['signed_ball'].initial = self.instance.reward.signed_ball
            self.fields['shirt'].initial = self.instance.reward.shirt
            self.fields['signed_shirt'].initial = self.instance.reward.signed_shirt

            # Check if the kickoff pack fields exist before initializing them
            for field_name in ['kickoff_pack_1', 'kickoff_pack_2', 'kickoff_pack_3', 'season_pack_1', 'season_pack_2', 'season_pack_3']:
                if hasattr(self.instance.reward, field_name):
                    self.fields[field_name].initial = getattr(self.instance.reward, field_name)

    def save(self, commit=True):
        instance = super(DivisionRewardForm, self).save(commit=False)

        # Ensure reward object is created or updated
        if instance.reward is None:
            # Create a new reward if none exists
            instance.reward = Rewards.objects.create(
                name=f'Reward for {instance.week.name} - {instance.division.name}',
                credits=self.cleaned_data['credits'],
                game_token=self.cleaned_data['game_token'],
                lapt_token=self.cleaned_data['lapt_token'],
                event_tickets=self.cleaned_data['event_tickets'],
                ball=self.cleaned_data['ball'],
                signed_ball=self.cleaned_data['signed_ball'],
                shirt=self.cleaned_data['shirt'],
                signed_shirt=self.cleaned_data['signed_shirt'],
                kickoff_pack_1=self.cleaned_data.get('kickoff_pack_1'),
                kickoff_pack_2=self.cleaned_data.get('kickoff_pack_2'),
                kickoff_pack_3=self.cleaned_data.get('kickoff_pack_3'),
                season_pack_1=self.cleaned_data.get('season_pack_1'),
                season_pack_2=self.cleaned_data.get('season_pack_2'),
                season_pack_3=self.cleaned_data.get('season_pack')
            )
        else:
            # Update existing reward
            instance.reward.credits = self.cleaned_data['credits']
            instance.reward.game_token = self.cleaned_data['game_token']
            instance.reward.lapt_token = self.cleaned_data['lapt_token']
            instance.reward.event_tickets = self.cleaned_data['event_tickets']
            instance.reward.ball = self.cleaned_data['ball']
            instance.reward.signed_ball = self.cleaned_data['signed_ball']
            instance.reward.shirt = self.cleaned_data['shirt']
            instance.reward.signed_shirt = self.cleaned_data['signed_shirt']
            
            # Check if the kickoff pack fields exist before updating them
            for field_name in ['kickoff_pack_1', 'kickoff_pack_2', 'kickoff_pack_3', 'season_pack_1', 'season_pack_2', 'season_pack_3']:
                if field_name in self.cleaned_data:
                    setattr(instance.reward, field_name, self.cleaned_data.get(field_name))

            instance.reward.save()

        if commit:
            instance.save()

        return instance

class RewardsInline(admin.StackedInline):
    model = Rewards
    extra = 0  # No extra empty forms
    fields = (
        'name', 'credits', 'game_token', 'lapt_token', 
        'event_tickets', 'ball', 'signed_ball', 'shirt', 'signed_shirt', 'kickoff_pack_1', 'kickoff_pack_2', 'kickoff_pack_3'
    )

class DivisionRewardInline(admin.TabularInline):
    model = DivisionReward
    extra = 1  # Number of empty forms to display
    form = DivisionRewardForm

    fields = (
        'division', 'min_position', 'max_position',
        'reward',  # Include the reward field
        'credits', 'game_token', 'lapt_token',
        'event_tickets', 'ball', 'signed_ball', 'shirt', 'signed_shirt', 'kickoff_pack_1', 'kickoff_pack_2', 'kickoff_pack_3', 'season_pack_1', 'season_pack_2', 'season_pack_3'
    )
    readonly_fields = []

    def credits(self, obj):
        return obj.reward.credits

    def game_token(self, obj):
        return obj.reward.game_token

    def lapt_token(self, obj):
        return obj.reward.lapt_token

    def event_tickets(self, obj):
        return obj.reward.event_tickets

    def ball(self, obj):
        return obj.reward.ball

    def signed_ball(self, obj):
        return obj.reward.signed_ball

    def shirt(self, obj):
        return obj.reward.shirt

    def signed_shirt(self, obj):
        return obj.reward.signed_shirt

@admin.register(DivisionReward)
class DivisionRewardAdmin(admin.ModelAdmin):
    form = DivisionRewardForm
    
    # Define the fields that will be displayed in the admin list view
    list_display = (
        'week', 'division', 'min_position', 'max_position',
        'credits', 'game_token', 'lapt_token',
        'event_tickets', 'ball', 'signed_ball', 'shirt', 'signed_shirt', 
        'kickoff_pack_1', 'kickoff_pack_2', 'kickoff_pack_3', 'season_pack_1', 'season_pack_2', 'season_pack_3'
    )

    search_fields = ('week__name', 'division__name')
    list_filter = ('week', 'division')

    # Custom methods to display related rewards fields in the list
    def credits(self, obj):
        return obj.reward.credits if obj.reward else None
    credits.short_description = 'Credits'  # Optional, adds a better display label

    def game_token(self, obj):
        return obj.reward.game_token if obj.reward else None
    game_token.short_description = 'Game Token'

    def lapt_token(self, obj):
        return obj.reward.lapt_token if obj.reward else None
    lapt_token.short_description = 'Lapt Token'

    def event_tickets(self, obj):
        return obj.reward.event_tickets if obj.reward else None
    event_tickets.short_description = 'Event Tickets'

    def ball(self, obj):
        return obj.reward.ball if obj.reward else None
    ball.short_description = 'Ball'

    def signed_ball(self, obj):
        return obj.reward.signed_ball if obj.reward else None
    signed_ball.short_description = 'Signed Ball'

    def shirt(self, obj):
        return obj.reward.shirt if obj.reward else None
    shirt.short_description = 'Shirt'

    def signed_shirt(self, obj):
        return obj.reward.signed_shirt if obj.reward else None
    signed_shirt.short_description = 'Signed Shirt'

    def kickoff_pack_1(self, obj):
        return obj.reward.kickoff_pack_1 if obj.reward else None
    kickoff_pack_1.short_description = 'Kickoff Pack 1'

    def kickoff_pack_2(self, obj):
        return obj.reward.kickoff_pack_2 if obj.reward else None
    kickoff_pack_2.short_description = 'Kickoff Pack 2'

    def kickoff_pack_3(self, obj):
        return obj.reward.kickoff_pack_3 if obj.reward else None
    kickoff_pack_3.short_description = 'Kickoff Pack 3'
    
    def season_pack_1(self, obj):
        return obj.reward.season_pack_1 if obj.reward else None
    season_pack_1.short_description = 'Season Pack 1'
    
    def season_pack_2(self, obj):
        return obj.reward.season_pack_2 if obj.reward else None
    season_pack_2.short_description = 'Season Pack 2'
    
    def season_pack_3(self, obj):
        return obj.reward.season_pack_3 if obj.reward else None
    season_pack_3.short_description = 'Season Pack 3'

@admin.register(GameWeek)
class GameWeekAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_at', 'end_at', 'scored_at', 'status')
    search_fields = ('id', 'name',)
    list_filter = ('status',)
    inlines = [DivisionRewardInline]

class UserModelChoiceField(forms.ModelChoiceField):
    def to_python(self, value):
        if not value:
            raise ValidationError("This field is required.")
        try:
            # Attempt to fetch by UUID
            return CustomUser.objects.get(pk=uuid.UUID(value))
        except (CustomUser.DoesNotExist, ValueError):
            # Fallback to fetching by username
            try:
                return CustomUser.objects.get(name=value)
            except CustomUser.DoesNotExist:
                raise ValidationError("User not found by username or ID.")

class AssignedCardPackForm(forms.ModelForm):
    user = UserModelChoiceField(
        queryset=CustomUser.objects.all(),
        widget=forms.TextInput(attrs={'placeholder': 'Enter username or ID'}),
        label='User (by username or ID)',
        help_text="Enter the username or ID of the user."
    )
    card_pack_type = forms.ModelChoiceField(
        queryset=CardPackType.objects.all().order_by('name'),
        label="Card Pack Type"
    )
    store_transaction_id = forms.ModelChoiceField(
        queryset=StoreProductTransactions.objects.all().order_by('id'),
        required=False,
        label="Store Transaction ID",
        widget=forms.Select(attrs={'placeholder': 'Select store transaction ID'})
    )

    class Meta:
        model = AssignedCardPack
        fields = ['user', 'card_pack_type', 'opened', 'opened_at', 'revealed_at', 'revealed', 'store_transaction_id']

    def clean_user(self):
        user_input = self.cleaned_data['user']
        try:
            # Attempt to fetch by UUID
            return CustomUser.objects.get(id=user_input.id)
        except (CustomUser.DoesNotExist, ValueError):
            try:
                # Fallback to fetching by username
                return CustomUser.objects.get(name=user_input.name)
            except CustomUser.DoesNotExist:
                raise ValidationError("User not found by username or ID.")

@admin.register(AssignedCardPack)
class AssignedCardPackAdmin(admin.ModelAdmin):
    form = AssignedCardPackForm
    list_display = ('user', 'card_pack_type', 'opened', 'revealed')
    search_fields = ('user__name', 'card_pack_type__name')

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('assign-card-pack/', self.admin_site.admin_view(self.assign_card_pack), name='assign-card-pack'),
        ]
        return custom_urls + urls

    def assign_card_pack(self, request):
        if request.method == 'POST':
            form = AssignedCardPackForm(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    messages.success(request, "Assigned Card Pack created successfully.")
                    return redirect('..')
                except Exception as e:
                    messages.error(request, f"An error occurred: {str(e)}")
            else:
                messages.error(request, "Please correct the errors below.")
        else:
            form = AssignedCardPackForm()

        context = {
            'form': form,
            'opts': self.model._meta,
            'title': 'Assign Card Pack to User',
        }
        return render(request, '../templates/assign_card_pack.html', context)

class RewardsAdmin(admin.ModelAdmin):
    # Specify the fields you want to display in the admin form
    list_display = ['name', 'credits', 'game_token', 'lapt_token', 'event_tickets', 'ball', 'signed_ball', 'shirt', 'signed_shirt', 'kickoff_pack_1', 'kickoff_pack_2', 'kickoff_pack_3', 'season_pack_1', 'season_pack_2', 'season_pack_3']

    # Optional: Specify the fields in the form layout order
    fields = ['name', 'credits', 'game_token', 'lapt_token', 'event_tickets', 'ball', 'signed_ball', 'shirt', 'signed_shirt', 'kickoff_pack_1', 'kickoff_pack_2', 'kickoff_pack_3', 'season_pack_1', 'season_pack_2', 'season_pack_3']

# Register the Rewards model with the custom admin
admin.site.register(Rewards, RewardsAdmin)

admin.site.register(DataFeedSimModel, DataFeedSimAdmin)
admin.site.register(CustomUser, UserAdmin)
admin.site.register(CompetitionConfig, CompetitionConfigAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(CompetitionEdition, CompetitionEditingAdmin)
admin.site.register(CompetitionPhase, CompetitionPhaseAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(SoccerWikiPlayer, SoccerWikiPlayerAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Action, ActionAdmin)
admin.site.register(PowerUp, PowerUpAdmin)
admin.site.register(Transactions, TransactionAdmin)
admin.site.register(MatchLeaderboard, MatchLeaderboardAdmin)
admin.site.register(ManualSubscription, ManualSubscriptionAdmin)
admin.site.register(StoreProduct, StoreProductAdmin)
