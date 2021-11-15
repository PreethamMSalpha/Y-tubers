from django.urls import path

from . import views

urlpatterns = [
    path('contactinformation', views.contactinformation, name="contactinformation"),
]
