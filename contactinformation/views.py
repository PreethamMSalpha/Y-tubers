from django.shortcuts import render
from .models import ContactInformation

# Create your views here.


def contactinformation(request):
    info = ContactInformation.objects.all()
    data = {
        'info': info,
    }

    return render(request, 'includes/header.html', data)
