from django.db import models
from datetime import datetime

# Create your models here.
class ContactForm(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    created_date = models.DateField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email