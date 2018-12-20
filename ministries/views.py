from django.shortcuts import render, get_object_or_404
from .models import Ministry_details, Ministry
from leadership.models import LeaderBio
from events.models import Event_details


def ministry_list(request, ministry_slug=None):
    ministry = None
    ministries = Ministry.objects.all()
    ministries_details = Ministry_details.objects.all()
    if ministry_slug:
        ministry = get_object_or_404(Ministry, slug=ministry_slug)
        ministries_details = ministries_details.filter(ministry=ministry)

    return render(request, 'ministries/ministry_list.html', {'ministry': ministry, 'ministries': ministries,
                                                           'ministries_details': ministries_details,
                                                            })


def ministry_det(request, id, slug, ministry_slug=None):
    ministry_detail = get_object_or_404(Ministry_details, id=id, slug=slug)
    ministry = None
    ministries = Ministry.objects.all()
    leaders = LeaderBio.objects.all()
    events = Event_details.objects.all()

    if ministry_slug:
        ministry = get_object_or_404(Ministry, slug=ministry_slug)

    return render(request, 'ministries/ministry_detail.html', {'ministry_detail': ministry_detail, 'ministry': ministry,
                                                               'leaders': leaders, 'ministries': ministries, 'events': events})



