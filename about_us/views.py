from django.shortcuts import render
from .models import AboutUsHeading, Beliefs1, AboutUsPix, Beliefs2, Beliefs3
from home.models import QuotableQuotes, QuotableImage
from leadership.models import LeaderBio

# Create your views here.


def about_us(request, category_slug=None):
    category = None
    aboutus = AboutUsHeading.objects.all()
    beliefs1 = Beliefs1.objects.all()
    beliefs2 = Beliefs2.objects.all()
    beliefs3 = Beliefs3.objects.all()
    quotableimage = QuotableImage.objects.all()
    quotablequote1 = QuotableQuotes.objects.filter(pk=1)
    quotablequote2 = QuotableQuotes.objects.filter(pk=2)
    quotablequote3 = QuotableQuotes.objects.filter(pk=3)
    openingphoto = AboutUsPix.objects.all()
    leaders = LeaderBio.objects.all()


    return render(request, 'about_us/about_us.html', {'aboutus': aboutus, 'beliefs1': beliefs1,
                                                      'beliefs2': beliefs2,
                                                      'beliefs3': beliefs3,
                                                      'quotableimage':quotableimage,
                                                      "quotablequote1": quotablequote1, 'quotablequote2': quotablequote2,
                                                      'quotablequote3': quotablequote3, 'openingphoto': openingphoto,
                                                      'leaders': leaders})
