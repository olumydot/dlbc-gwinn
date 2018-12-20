from django.shortcuts import render, get_object_or_404
from .models import Livestream


def live_view(request):
    livestream = Livestream.objects.filter(pk=1)

    return render(request, 'livestream/livestream.html', {'livestream': livestream, })
