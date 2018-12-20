from django.shortcuts import render, get_object_or_404
from .models import Leadership, LeaderBio


def leader_list(request, leader_slug=None):
    leader = None
    leaders = Leadership.objects.all()
    leaders_bio = LeaderBio.objects.all()
    if leader_slug:
        leader = get_object_or_404(Leadership, slug=leader_slug)
        leaders_bio = leaders_bio.filter(leader=leader)

    return render(request, 'leadership/leader_list.html', {'leader': leader, 'leaders': leaders,
                                                           'leaders_bio': leaders_bio,
                                                            })


def leader_detail(request, id, slug, leader_slug=None):
    leader_bio = get_object_or_404(LeaderBio, id=id, slug=slug)
    leader = None
    leaders = Leadership.objects.all()

    if leader_slug:
        leader = get_object_or_404(Leadership, slug=leader_slug)

    return render(request, 'leadership/leader_detail.html', {'leader_bio': leader_bio, 'leader': leader,
                                                             'leaders': leaders, })



