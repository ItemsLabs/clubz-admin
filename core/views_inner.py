from django.conf import settings
from django.db import transaction
from django.http import HttpResponse
from django.utils import timezone

from core.models import MatchEventSimulation, Match
from core.serializers import MatchEventSerializer
from util import events


def process_simulations(request):
    qs = MatchEventSimulation.objects. \
        filter(simulated_at__isnull=True,
               timestamp__lte=timezone.now())

    match_ids = set([el.match_id for el in qs])

    cnt = 0
    with transaction.atomic():
        for match_id in match_ids:
            # lock match
            _ = Match.objects.select_for_update().get(pk=match_id)

            # get simulation events, max 100 at once, do not heavy load system
            sims = MatchEventSimulation.objects. \
                       select_related('match_event'). \
                       filter(simulated_at__isnull=True,
                              timestamp__lte=timezone.now(),
                              match_id=match_id). \
                       order_by('id')[:100]

            for sim in sims:
                new_event = sim.match_event
                new_event.pk = None
                new_event.match = sim.match
                new_event.timestamp = sim.timestamp
                new_event.save()

                sim.simulated_at = timezone.now()
                sim.save(update_fields=['simulated_at'])

                # create new amqp_event
                events.create_amqp_event(
                    settings.AMQP_MATCH_EVENTS_EXCHANGE,
                    'new',
                    MatchEventSerializer(new_event).data,
                )

                cnt += 1

    return HttpResponse("simulated {} events".format(cnt))
