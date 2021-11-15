from django.contrib import admin
from django.utils.html import format_html
from .models import ContactForm

# Register your models here.

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'company_name', 'subject')
    list_display_links = ('full_name', 'email')
    list_filter = ('created_date',)  


admin.site.register(ContactForm, ContactFormAdmin)