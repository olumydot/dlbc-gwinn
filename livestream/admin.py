from django.contrib import admin
from .models import Livestream


class LiveAdmin(admin.ModelAdmin):
    list_display = ['program', 'live']


admin.site.register(Livestream, LiveAdmin)

