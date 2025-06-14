from datetime import timedelta, timezone
from typing import List

from celery import shared_task
from django.db.models import Q
from util.events import create_amqp_event
from django.conf import settings
from core.models import Badges, Banner, CustomUser, Frames, GameWeek, PushNotification, UserBadges, UserBanners, UserFrames
import mixpanel

mixpanel_client = mixpanel.Mixpanel('be4f6d7541a1930dcec47b443dc1a86f')

def count_user_notifications_last_hour(user):
    one_hour_ago = timezone.now() - timedelta(hours=1)
    return PushNotification.objects.filter(user=user, sent_at__gte=one_hour_ago).count()


from django.utils import timezone


def send_push(user, title, message, url=None):
    # Prepare the event data
    event_data = {
        "user_id": str(user.id),  # Ensure UUID is converted to string
        "title": title,
        "message": message,
        "push_token": user.firebase_id,
    }

    # Count the number of notifications sent to the user in the last hour
    notification_count = count_user_notifications_last_hour(user)

    if url is not None:
        event_data["url"] = url

    if notification_count < 3:
        # Create a PushNotification record in the database
        PushNotification.objects.create(
            user=user,
            title=title,
            message=message,
            payload=event_data,
            sent_at=timezone.now()
        )

        # Send the push notification event (via AMQP)
        create_amqp_event(
            settings.RMQ_FCM_EXCHANGE,
            "push_notification",
            event_data,
        )

        # Mixpanel event properties
        event_props = {
            "event_name":  "Push Notification",
            "title":       title,
            "description": message,
            "distinct_id": str(user.id),  # Ensure UUID is converted to string
            "type":        "sent",
            "username":    user.name,
        }

        # Track the push notification event in Mixpanel
        try:
            mixpanel_client.track(str(user.id), "Push Notification Sent to User", event_props)
        except Exception as e:
            # Log the error for debugging if Mixpanel tracking fails
            print(f"Mixpanel event tracking failed: {e}")
    else:
        print(f"Not sending push notification to {user.name}. Limit of 3 notifications per hour reached.")


@shared_task
def send_push_to_users(user_ids, week_id):
    users = CustomUser.objects.filter(
        Q(id__in=user_ids) & Q(firebase_id__startswith="Expo")
    )
    title = 'Your game week concluded'
    message = 'Tap to here to see summary'
    url = f"/divisions/summary/{week_id}"

    print(f"push push: {title}, {message}, {url}")
    for user in filter_repeated_users(users):
        try:
            send_push(user, title, message, url)
            print(f"pushed: {user.id} {title}, {message}, {url}")
        except Exception as e:
            print(f"Failed to send notification to {user.id}: {e}")


@shared_task
def send_push_to_user(user_id, title, message):
    user = CustomUser.objects.get(id=user_id)
    if user.firebase_id and user.firebase_id.startswith("Expo"):
        send_push(user, title, message)


@shared_task
def send_push_to_all(title, message):
    users = CustomUser.objects.filter(firebase_id__startswith="Expo")
    for user in filter_repeated_users(users):
        send_push(user, title, message)


def filter_repeated_users(users: List[CustomUser]) -> List[CustomUser]:
    sorted_users = sorted(users, reverse=True, key=lambda user: user.updated_at)
    already_present = set()

    result = []
    for user in sorted_users:
        if user.firebase_id not in already_present:
            already_present.add(user.firebase_id)
            result.append(user)

    return result

@shared_task
def assign_default_items_to_users():
    # Fetch default badges, frames, and banners
    default_badges = Badges.objects.filter(type='default')
    default_frames = Frames.objects.filter(type='default')
    default_banners = Banner.objects.filter(type='default')

    # Fetch all users
    users = CustomUser.objects.all()

    # Assign default badges to users
    for user in users:
        for badge in default_badges:
            if not UserBadges.objects.filter(user=user, badge=badge).exists():
                UserBadges.objects.create(user=user, badge=badge)

    # Assign default frames to users
    for user in users:
        for frame in default_frames:
            if not UserFrames.objects.filter(user=user, frame=frame).exists():
                UserFrames.objects.create(user=user, frame=frame)

    # Assign default banners to users
    for user in users:
        for banner in default_banners:
            if not UserBanners.objects.filter(user=user, banner=banner).exists():
                UserBanners.objects.create(user=user, banner=banner)