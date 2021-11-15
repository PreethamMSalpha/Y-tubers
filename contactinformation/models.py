from django.db import models
from datetime import datetime


# Create your models here.
# class ContactForm(models.Model):
#     full_name = models.CharField(max_length=255)
#     phone = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     company_name = models.CharField(max_length=255)
#     subject = models.CharField(max_length=255)
#     message = models.TextField(blank=True)
#     created_date = models.DateField(blank=True, default=datetime.now)

#     def __str__(self):
#         return self.email

class ContactInformation(models.Model):
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    insta_link = models.CharField(max_length=255)
    fb_link = models.CharField(max_length=255)
    twitter_link = models.CharField(max_length=255)
    youtube_link = models.CharField(max_length=255)
    created_date = models.DateField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email
