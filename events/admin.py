from django.contrib import admin
from .models import Event, Event_details


class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Event, EventAdmin)


class DetailsAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'slug', ]
    prepopulated_fields = {'slug': ('event_name',)}


admin.site.register(Event_details, DetailsAdmin)
