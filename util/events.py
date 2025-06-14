from rabbit.models import AMQPEvent
from django.conf import settings
from rest_framework.renderers import JSONRenderer
from core.models import EventThrottler
from core.serializers import MatchEventSerializer

def create_amqp_event(exchange, event_type, data):
    if settings.AMQP_THROTTLING_ENABLED:
        EventThrottler.objects.create(
            exchange=exchange,
            event_type=event_type,
            data=JSONRenderer().render(data).decode("utf-8"),
        )
    else:
        AMQPEvent.objects.create(
            exchange=exchange,
            event_type=event_type,
            data=JSONRenderer().render(data).decode("utf-8"),
        )


def create_amqp_event_from_match_event(match_event):
    create_amqp_event(
        settings.AMQP_MATCH_EVENTS_EXCHANGE,
        "new",
        MatchEventSerializer(match_event).data,
    )
