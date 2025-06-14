import json

import pytz
from rest_framework import serializers

from core import const
from core.models import CustomUser, Match, Team, Player, Game, GamePick, MatchEvent, GameEvent, Competition, \
    Action, GamePowerUp, MatchReward, MatchPlayer, MatchHeadline
from datetime import datetime


class StringListField(serializers.ListField):
    child = serializers.CharField()


class UUIDListField(serializers.ListField):
    child = serializers.UUIDField()


class UpdateUserAvatarSerializer(serializers.Serializer):
    avatar = serializers.ImageField(required=True)


class CurrentUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'name', 'balance', 'paypal_email', 'avatar_url',)


class CustomTimeField(serializers.Field):
    def to_representation(self, value):
        if isinstance(value, str):
            try:
                dt_obj = datetime.fromisoformat(value)
            except ValueError:
                return value
        else:
            dt_obj = value
        if dt_obj.tzinfo is None:
            dt_obj = dt_obj.replace(tzinfo=pytz.UTC)
        formatted_time = dt_obj.isoformat()

        return formatted_time


class MatchEventSerializer(serializers.ModelSerializer):
    created_at = CustomTimeField()
    timestamp = CustomTimeField()

    class Meta:
        model = MatchEvent
        fields = ('id', 'match_id', 'created_at', 'timestamp', 'team_id',
                  'player_id', 'type', 'points', 'payload', 'minute',
                  'second', 'x', 'y', 'match_event_id', 'provider_id', 'opta_feed_item_version_id', 'status')


class RevenueCatSyncSerializer(serializers.Serializer):
    user_id = serializers.CharField(required=True)
    last_billing_update = serializers.DateTimeField(required=True)
    sync = serializers.BooleanField(required=False)
