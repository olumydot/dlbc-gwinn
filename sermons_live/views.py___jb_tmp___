from django.shortcuts import render, get_object_or_404
from .models import Sermon, Sermon_details
from leadership.models import LeaderBio


def sermon_list(request, sermon_slug=None):
    sermon = None
    sermons = Sermon.objects.all()
    sermons_details = Sermon_details.objects.all()
    if sermon_slug:
        sermon = get_object_or_404(Sermon, slug=sermon_slug)
        sermons_details = sermons_details.filter(sermon=sermon)

    return render(request, 'sermon/sermon.html', {'sermon': sermon, 'sermons': sermons,
                                                           'sermons_details': sermons_details,
                                                            })


def sermon_det(request, id, slug, sermon_slug=None):
    sermon_detail = get_object_or_404(Sermon_details, id=id, slug=slug)
    sermon = None
    sermons = Sermon.objects.all()
    leaders = LeaderBio.objects.all()

    if sermon_slug:
        sermon = get_object_or_404(Sermon, slug=sermon_slug)

    return render(request, 'sermon/sermon_details.html', {'sermon_detail': sermon_detail, 'sermon': sermon,
                                                               'leaders': leaders, 'sermons': sermons, })



