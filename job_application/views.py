from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from dotenv import load_dotenv
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
import os


# Create your views here.


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            message_body = f"""
            Hey, {first_name}! Thanks for using our platform! 😄
            Here you have your information: 
            Your complete name: {first_name} {last_name}. 
            Your current occupation: {occupation}
            I hope this to be helpful, have a great day! 🫶🏻
            """

            email_to_send = EmailMessage(subject="New form submission! 📩", body=message_body, to=[email])
            email_to_send.send()

            Form.objects.create(first_name=first_name, last_name=last_name, email=email, occupation=occupation,
                                date=date)

            messages.success(request,
                             "Form submitted successfully!")

    return render(request, template_name='index.html')


def about(request):
    return render(request, 'about.html')
