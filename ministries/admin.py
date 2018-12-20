from django.contrib import admin
from .models import Ministry, Ministry_details


class MinistryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Ministry, MinistryAdmin)


class DetailsAdmin(admin.ModelAdmin):
    list_display = ['ministry_name', 'slug', ]
    prepopulated_fields = {'slug': ('ministry_name',)}


admin.site.register(Ministry_details, DetailsAdmin)
