import json

from django.conf import settings
from django.db import transaction
from django.utils import timezone
from django.utils.dateparse import parse_datetime

from core import const
from core.models import Subscription, SubscriptionRequest, CustomUser


def process_subscription_requests():
    for req in SubscriptionRequest.objects.all()[:100]:
        print('Syncing subscription {}'.format(req.user_id))
        sync_subscription(req.user_id, req.app_user)
        # delete request after syncing
        req.delete()


def expire_subscriptions():
    # check subscription that are active, but expiration time is less than current time
    for sub in Subscription.objects.filter(active=True, expiration_time__lt=timezone.now()).all():
        # find user that has this subscription
        for usr in CustomUser.objects.filter(subscription=sub).all():
            try:
                sync_subscription(sub.user_id, usr)
            except CustomUser.DoesNotExist:
                print('Not found user for subscription {}: user_id = {}'.format(sub.pk, sub.user_id))


def sync_subscription(user_id, app_user):
    subscription = sync_subscription_with_revenue_cat(user_id)

    # update premium flag of user
    if app_user:
        with transaction.atomic():
            locked_user = CustomUser.objects.select_for_update().get(pk=app_user.pk)
            # remove that subscription from all other users
            for user in CustomUser.objects.filter(subscription=subscription).exclude(pk=app_user.pk).all():
                user.subscription = None
                user.update_premium()
            locked_user.subscription = subscription
            locked_user.save(update_fields=['subscription', 'updated_at'])
            locked_user.update_premium()


def sync_subscription_with_revenue_cat(user_id):
    res = settings.REVENUE_CAT_CLIENT.get_subscriber(user_id)
    last_billing_update = find_last_billing_update(res)
    expiration_time, subscriptier_tier = find_expiration_and_tier(res)
    raw_data = json.dumps(res.get("subscriber", {}), sort_keys=True)
    is_active = expiration_time > timezone.now()

    # try to find subscription in database
    try:
        s = Subscription.objects.get(user_id=user_id)

        # update subscription if any of meaningful fields are changed
        if s.raw_data != raw_data or \
                s.last_billing_update != last_billing_update or \
                s.expiration_time != expiration_time or \
                s.active != is_active or \
                s.tier != subscriptier_tier:
            s.last_billing_update = last_billing_update
            s.expiration_time = expiration_time
            s.raw_data = raw_data
            s.active = is_active
            s.tier = subscriptier_tier
            s.save()

        return s

    except Subscription.DoesNotExist:
        # create new one
        return Subscription.objects.create(
            user_id=user_id,
            expiration_time=expiration_time,
            raw_data=raw_data,
            last_billing_update=last_billing_update,
            active=is_active,
            tier=subscriptier_tier,
        )


def check_is_active(subscriber_info=None):
    if subscriber_info is None:
        subscriber_info = dict()

    for k, v in subscriber_info.get("subscriber", {}).get("entitlements", {}).items():
        dat = parse_date(v.get("expires_date"))
        if dat > timezone.now():
            return True

    return False


def find_expiration_time(subscriber_info=None):
    if subscriber_info is None:
        subscriber_info = dict()

    dates = []
    for k, v in subscriber_info.get("subscriber", {}).get("subscriptions", {}).items():
        expires_date = parse_date(v.get("expires_date"))
        if expires_date:
            dates.append(expires_date)

    return max(dates) if len(dates) > 0 else None


def find_expiration_and_tier(subscriber_info=None):
    if subscriber_info is None:
        subscriber_info = dict()

    max_expires_date = None
    tier = const.TIER_NONE

    for k, v in subscriber_info.get("subscriber", {}).get("entitlements", {}).items():
        expires_date = parse_date(v.get("expires_date"))

        if max_expires_date is None or max_expires_date < expires_date:
            max_expires_date = expires_date
            if k == "lite":
                tier = const.TIER_LITE
            elif k == "premium":
                tier = const.TIER_PREMIUM

    return max_expires_date, tier


def find_last_billing_update(subscriber_info=None):
    if subscriber_info is None:
        subscriber_info = dict()

    # build array of possible candidates for last billing update
    dates = []

    def add_date(dat):
        parsed_date = parse_date(dat)
        if parsed_date:
            dates.append(parsed_date)

    s = subscriber_info.get("subscriber", {})
    entitlements = s.get("entitlements", {})

    for k, v in entitlements.items():
        add_date(v.get("expires_date"))
        add_date(v.get("purchase_date"))
        add_date(v.get("grace_period_expires_date"))

    subscriptions = subscriber_info.get("subscriptions", {})

    for k, v in subscriptions.items():
        add_date(v.get("expires_date"))
        add_date(v.get("original_purchase_date"))
        add_date(v.get("purchase_date"))
        add_date(v.get("grace_period_expires_date"))
        add_date(v.get("billing_issues_detected_at"))
        add_date(v.get("unsubscribe_detected_at"))

    return max(dates) if len(dates) > 0 else None


def parse_date(dat):
    if not dat:
        return None

    # try to parse date
    return parse_datetime(dat)
