from django.contrib import admin
from .models import AboutUsHeading, Beliefs1, Beliefs2, Beliefs3, AboutUsPix

# Register your models here.


class AboutPixAdmin(admin.ModelAdmin):
    list_display = ['header',]


admin.site.register(AboutUsPix, AboutPixAdmin)


class AboutusAdmin(admin.ModelAdmin):
    list_display = ['header', 'slug']


admin.site.register(AboutUsHeading, AboutusAdmin)


class Belief1Admin(admin.ModelAdmin):
    list_display = ['header', ]


admin.site.register(Beliefs1, Belief1Admin)


class Belief2Admin(admin.ModelAdmin):
    list_display = ['header', ]


admin.site.register(Beliefs2, Belief2Admin)


class Belief3Admin(admin.ModelAdmin):
    list_display = ['header', ]


admin.site.register(Beliefs3, Belief3Admin)