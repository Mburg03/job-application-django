from django import forms


class ApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    date = forms.DateField()
    occupation = forms.CharField(max_length=80)
    phone_number = forms.CharField(max_length=20)
    age = forms.IntegerField()
    city = forms.CharField(max_length=50)
    street_address = forms.CharField(max_length=255)
    job_title = forms.CharField(max_length=100)
    employer = forms.CharField(max_length=100)
    employment_duration = forms.CharField(max_length=50)


class ContactUsForm(forms.Form):
    username = forms.CharField(max_length=80)
    email = forms.EmailField()
    message = forms.CharField(max_length=280)
