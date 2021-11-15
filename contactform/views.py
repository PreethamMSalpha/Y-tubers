from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import ContactForm


# Create your views here.
def contactform(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']
        company_name = request.POST['company_name']
        subject = request.POST['subject']
        message = request.POST['message']
    
        phone = request.POST['phone']
        contactform = ContactForm(full_name=full_name, phone=phone, email=email, company_name=company_name, subject=subject, message=message)
        contactform.save()
        messages.success(request, 'Thanks for reaching out!')
        return redirect('youtubers')