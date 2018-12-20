from django.contrib import admin
from .models import SliderCarousel, WelcomeMessage, IconBox, SpecialEvent, QuotableQuotes, QuotableImage, Ministries

# Register your models here.


class SliderAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(SliderCarousel, SliderAdmin)


class WelcomeAdmin(admin.ModelAdmin):
    list_display = ['title', ]


admin.site.register(WelcomeMessage, WelcomeAdmin)


class IconAdmin(admin.ModelAdmin):
    list_display = ['title', ]


admin.site.register(IconBox, IconAdmin)


class SpecialAdmin(admin.ModelAdmin):
    list_display = ['title', ]


admin.site.register(SpecialEvent, SpecialAdmin)


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['verse', 'version', ]


admin.site.register(QuotableQuotes, QuoteAdmin)


class QuoteImageAdmin(admin.ModelAdmin):
    list_display = ['imagename', ]


admin.site.register(QuotableImage, QuoteImageAdmin)


class MinistriesAdmin(admin.ModelAdmin):
    list_display = ['ministry', 'age']


admin.site.register(Ministries, MinistriesAdmin)