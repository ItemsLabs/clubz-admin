import logging
import uuid

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from core.exceptions import CannotUploadAvatar
from core.models import Subscription, \
    SubscriptionRequest
from core.serializers import CurrentUserProfileSerializer, UpdateUserAvatarSerializer, RevenueCatSyncSerializer
from revenue_cat.sync import sync_subscription
from util import gce
from util.drf import AuthAPIView
from core.tasks import task_sync_competitions, task_sync_teams, task_sync_matches_via_sdapi, task_sync_match_players


class UpdateUserAvatarView(AuthAPIView):
    def post(self, request):
        ser = UpdateUserAvatarSerializer(data=request.data)
        ser.is_valid(raise_exception=True)

        avatar = ser.validated_data['avatar']

        # upload image to gce
        try:
            bucket = settings.GCE_USER_AVATAR_BUCKET
            new_filename = str(uuid.uuid4()) + ".png"
            gce.upload_file(bucket, new_filename, avatar.read(), avatar.content_type)
            new_avatar_url = gce.get_file_url(bucket, new_filename)
        except Exception:
            logging.exception("cannot upload file to gce")
            raise CannotUploadAvatar

        user = request.user
        user.avatar_url = new_avatar_url
        user.save(update_fields=['avatar_url'])

        return Response(data=CurrentUserProfileSerializer(request.user).data)


def index(request):
    return HttpResponse("OK")


def terms(request):
    return render(request, 'terms.html')


class RevenueCatSyncView(AuthAPIView):
    def post(self, request):
        ser = RevenueCatSyncSerializer(data=request.data)
        ser.is_valid(raise_exception=True)

        # try to find subscription in database
        try:
            subscription = Subscription.objects.get(user_id=ser.data['user_id'])
            # if last_billing_update doesn't changed, just ignore this sync call
            if ser.data['last_billing_update'] == subscription.last_billing_update:
                return Response()

        except Subscription.DoesNotExist:
            # subscription doesn't exists, that's fine, it will be created later during sync
            pass

        if 'sync' in ser.data and ser.data['sync']:
            # do sync in scope of this request
            sync_subscription(ser.data['user_id'], request.user)
        else:
            # do sync in the background in queue
            SubscriptionRequest.objects.create(
                user_id=ser.data['user_id'],
                last_billing_update=ser.data['last_billing_update'],
                app_user=request.user
            )

        return Response()


key = "c36d0df5bac84c368c796b3539884c7c" # arbitrary key to allow execution of force sync and test uri

def force(request):
    msg = "OK"
    if request.GET.get("key") == key:
        start = timezone.now()
        print("force start:", start, "with keys:", request.GET)
        # if request query string contains "matches=true" then sync matches
        forced = False
        if request.GET.get("update_no_week") == "true":
            from opta.sync import sync_match_no_week
            sync_match_no_week()
            forced = True
        if request.GET.get("matches") == "true":
            mtd = request.GET.get("match_time_delta", 12)
            forced = True
            # cast mtd to int if it is a number, if it is a string, should be set to None
            if mtd is not None:
                try:
                    mtd = int(mtd)
                except:
                    mtd = 12
            competition_code = request.GET.get("code", None)
            task_sync_matches_via_sdapi.delay(mtd, forced, competition_code, forced)
        # if request query string contains "competitions=true" then sync competitions
        if request.GET.get("competitions") == "true":
            competition_code = request.GET.get("code", None)
            task_sync_competitions.delay(competition_code)
            forced = True
        # if request query string contains "teams=true" then sync all teams
        if request.GET.get("teams") == "true":
            task_sync_teams.delay()
            forced = True
        if request.GET.get("match_players") == "true":
            task_sync_match_players.delay()
            forced = True
        end = timezone.now()
        print("force end:", end)
        print("time to process force:", end-start)
        if forced:
            msg = "correctly synced"
    return HttpResponse(msg)

def uritest(request):
    if request.GET.get("key") == key:
        import requests
        req = request.GET.get("uri")
        res = requests.get(req)
        res.close()
        return HttpResponse("OK")

def datafeedsimtest(request):
    if request.GET.get("key") == key:
        from opta.sync import process_event_throttling
        process_event_throttling()
        return HttpResponse("OK")
