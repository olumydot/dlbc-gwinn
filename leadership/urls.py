from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.leader_list, name='leadership_list'),
    url(r'^(?P<leader_slug>[-\w]+)/$', views.leader_list, name='leadership_list_by_name'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.leader_detail, name='leader_detail'),
]