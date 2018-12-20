from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.ministry_list, name='ministry_list'),
    url(r'^(?P<ministry_slug>[-\w]+)/$', views.ministry_list, name='ministry_list_by_name'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ministry_det, name='ministry_detail'),
]