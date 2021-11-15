from django.contrib import admin

from django.utils.html import format_html
from .models import Hiretuber

# Register your models here.


class HireTuberAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'email', 'tuber_name')
    list_display_links = ('first_name', 'email')
    search_fields = ('tuber_name',)
    list_filter = ('tuber_name',)


admin.site.register(Hiretuber, HireTuberAdmin)
