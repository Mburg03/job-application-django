from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from datetime import date

# Create your views here.
current_date = date.today()
formatted_date = current_date.strftime('%Y-%d-%m')


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            print(f" second form pass {form.cleaned_data}")
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]
            # Phone
            phone = form.cleaned_data["phone_number"]
            # City
            city = form.cleaned_data["city"]
            # Address
            address = form.cleaned_data["street_address"]
            # Age
            age = form.cleaned_data["age"]
            # last job title
            last_job_title = form.cleaned_data["job_title"]
            # last employer
            last_employer = form.cleaned_data["employer"]
            # duration of employment
            duration_of_last_employment = form.cleaned_data["employment_duration"]


            message_body = f"""
            Hey, {first_name}! Thanks for using our platform! 😄
            Here you have your information: 
            
            Your complete name: {first_name} {last_name}. 
            Your current occupation: {occupation}
            
            I hope this to be helpful, have a great day! 🫶🏻
            """

            email_to_send = EmailMessage(subject="New form submission! 📩", body=message_body, to=[email])
            email_to_send.send()
            try:
                Form.objects.create(first_name=first_name, last_name=last_name, email=email, occupation=occupation,
                                    date=date, phone_number=phone, age=age, city=city, street_address=address,
                                    job_title=last_job_title, employer=last_employer,
                                    employment_duration=duration_of_last_employment)
            except Exception as e:
                print(f"Error saving form data: {e}")

            messages.success(request,
                             "Form submitted successfully!")
        else:
            print(form.errors)
    print("just here")
    return render(request, template_name='index.html', context={'current_date': formatted_date})


def about(request):
    return render(request, 'about.html')
