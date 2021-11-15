from django.contrib import admin
from django.utils.html import format_html
from .models import ContactInformation


class ContactInformationAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone',)
    list_display_links = ('email', 'phone')


admin.site.register(ContactInformation, ContactInformationAdmin)
