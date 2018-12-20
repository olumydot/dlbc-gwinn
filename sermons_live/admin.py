from django.contrib import admin
from .models import Sermon, Sermon_details


class SermonAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Sermon, SermonAdmin)


class DetailsAdmin(admin.ModelAdmin):
    list_display = ['sermon_name', 'slug', 'recent' ]
    prepopulated_fields = {'slug': ('sermon_name',)}
    list_editable = ['recent',]


admin.site.register(Sermon_details, DetailsAdmin)
