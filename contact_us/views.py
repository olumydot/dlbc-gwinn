from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import OurContact, OtherCloserLocations
from .forms import UserData

# Create your views here.


def contact_us(request):

    ourcontact = OurContact.objects.all()
    otherlocations = OtherCloserLocations.objects.all()

    return render(request, 'contact_us/thankyou.html', {'ourcontact': ourcontact, 'otherlocations': otherlocations, })


def get_user_data(request):
    ourcontact = OurContact.objects.all()
    otherlocations = OtherCloserLocations.objects.all()
    form = UserData(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('contact:thankyou'))
    return render(request, 'contact_us/contact_us.html', {'form': form, 'ourcontact': ourcontact,
                                                          'otherlocations': otherlocations,})