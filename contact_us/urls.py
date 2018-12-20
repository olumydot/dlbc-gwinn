from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.get_user_data, name='contactus'),
    url(r'^thankyou$', views.contact_us, name='thankyou'),
]