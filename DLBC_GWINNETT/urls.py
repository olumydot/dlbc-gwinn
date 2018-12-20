"""DLBC_GWINNETT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    url(r'^adminG/', include(admin.site.urls)),
    url(r'^', include('home.urls', namespace='home')),
    url(r'^about_us/', include('about_us.urls', namespace='about_us')),
    url(r'^leadership/', include('leadership.urls', namespace='leadership')),
    url(r'^contact/', include('contact_us.urls', namespace='contact')),
    url(r'^ministries/', include('ministries.urls', namespace='ministries')),
    url(r'^sermons/', include('sermons_live.urls', namespace='sermons')),
    url(r'^events/', include('events.urls', namespace='events')),
    url(r'^live/', include('livestream.urls', namespace='livestream')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
