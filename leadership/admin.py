from django.contrib import admin
from .models import Leadership, LeaderBio


class LeadershipAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Leadership, LeadershipAdmin)


class LeaderBioAdmin(admin.ModelAdmin):
    list_display = ['leader_name', 'slug', 'lead_pastor', ]
    list_editable = ['lead_pastor', ]
    prepopulated_fields = {'slug': ('leader_name',)}


admin.site.register(LeaderBio, LeaderBioAdmin)
