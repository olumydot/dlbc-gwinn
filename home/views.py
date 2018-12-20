from django.shortcuts import render
from .models import SliderCarousel, WelcomeMessage, IconBox, SpecialEvent, QuotableQuotes, QuotableImage, Ministries
from events.models import Event_details
from sermons_live.models import Sermon_details
from ministries.models import Ministry_details, Ministry
from livestream.models import Livestream

# Create your views here.


def index(request):
    slider = SliderCarousel.objects.all()
    welcomemessage = WelcomeMessage.objects.all()
    iconbox = IconBox.objects.all()
    specialevent = SpecialEvent.objects.all()
    quotablequotes1 = QuotableQuotes.objects.filter(pk=1)
    quotablequotes2 = QuotableQuotes.objects.filter(pk=2)
    quotablequotes3 = QuotableQuotes.objects.filter(pk=3)
    quotablequotes4 = QuotableQuotes.objects.filter(pk=4)
    quotableimage = QuotableImage.objects.all()
    ministry = Ministries.objects.all()
    sermons = Sermon_details.objects.all()
    events = Event_details.objects.all()
    ministries = Ministry_details.objects.all()
    livestream = Livestream.objects.all()

    return render(request, 'home/home/index.html', {'slider': slider, 'welcomemessage': welcomemessage,
                                                    'iconbox': iconbox, 'specialevent': specialevent,
                                                    'quotablequote1': quotablequotes1, 'quotablequote2': quotablequotes2,
                                                    'quotablequote3': quotablequotes3, 'quotablequote4': quotablequotes4,
                                                    'quotableimage': quotableimage,
                                                    'ministry': ministry, 'sermons': sermons, 'events': events,
                                                    'ministries': ministries, 'livestream': livestream,
                                                    })


def base(request):
    ministries = Ministry_details.objects.all()
    ministry = Ministry.objects.all()
    return render(request, 'home/base.html', {'ministries': ministries, 'ministry': ministry, })