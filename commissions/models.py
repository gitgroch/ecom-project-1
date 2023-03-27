from django.db import models
from django.conf import settings


class Commission(models.Model):
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    location = models.CharField(max_length=80, null=True, blank=True)
    commission_request = models.TextField(max_length=200, blank=True)