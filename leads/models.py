from django.db import models
from datetime import datetime


class Lead(models.Model):
    lead_type = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    is_hot = models.BooleanField(default=False)
    is_warm = models.BooleanField(default=False)
    is_cold = models.BooleanField(default=False)

    def __str__(self):
        return self.name
