from django.shortcuts import render, get_object_or_404
from .models import Event, Event_details
from leadership.models import LeaderBio


def event_list(request, event_slug=None):
    event = None
    events = Event.objects.all()
    events_details = Event_details.objects.all()
    if event_slug:
        event = get_object_or_404(Event, slug=event_slug)
        events_details = events_details.filter(event=event)

    return render(request, 'events/events.html', {'event': event, 'events': events,
                                                           'events_details': events_details,
                                                            })


def event_det(request, id, slug, event_slug=None):
    event_detail = get_object_or_404(Event_details, id=id, slug=slug)
    event = None
    events = Event.objects.all()
    leaders = LeaderBio.objects.all()

    if event_slug:
        event = get_object_or_404(Event, slug=event_slug)

    return render(request, 'events/event_details.html', {'event_detail': event_detail, 'event': event,
                                                               'leaders': leaders, 'events': events, })



