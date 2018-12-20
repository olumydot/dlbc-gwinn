from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.event_list, name='event_list'),
    url(r'^(?P<event_slug>[-\w]+)/$', views.event_list, name='event_list_by_name'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.event_det, name='event_detail'),
]