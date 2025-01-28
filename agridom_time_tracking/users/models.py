from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    employee_id = models.CharField(unique=True, max_length=6)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    date_hired = models.DateField(blank=True, null=True)
    pin = models.CharField(max_length=4, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    preset_name = models.CharField(max_length=100, blank=True, null=True)

    # Remove redundant fields from AbstractUser
    last_name = None  # You're using 'surname' instead