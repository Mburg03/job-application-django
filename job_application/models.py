from django.db import models


# Database model
# Create your models here.
class Form(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    street_address = models.CharField(max_length=255, null=True, blank=True)
    job_title = models.CharField(max_length=100, null=True, blank=True)
    employer = models.CharField(max_length=100, null=True, blank=True)
    employment_duration = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
