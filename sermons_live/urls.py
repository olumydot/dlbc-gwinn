from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.sermon_list, name='sermon_list'),
    url(r'^(?P<sermon_slug>[-\w]+)/$', views.sermon_list, name='sermon_list_by_name'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.sermon_det, name='sermon_detail'),
]