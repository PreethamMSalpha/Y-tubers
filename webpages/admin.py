from django.contrib import admin
from .models import Slider, Team
from django.utils.html import format_html

# Register your models here.

class SliderAdmin(admin.ModelAdmin):

    def sliderPhoto(seld, object):
        return format_html('<img src="{}" width="150" height="60" />'.format(object.photo.url))
    
    list_display = ('id', 'headline', 'sliderPhoto', 'button_text',)
    list_display_links = ('headline', )


class TeamAdmin(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img src="{}" width="40" />'.format(object.photo.url))

    list_display = ('id', 'myphoto', 'first_name', 'role', 'created_date')
    list_display_links = ('first_name', )
    search_fields = ('first_name', 'role')
    list_filter = ('role',)


admin.site.register(Slider, SliderAdmin)
admin.site.register(Team, TeamAdmin)
