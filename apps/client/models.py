from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Client(models.Model):
    """Client information."""

    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    
    tax_id = models.TextField(blank=True, default="C/F")
    address = models.TextField(blank=True, default="Ciudad")
    phone = PhoneNumberField(blank=True)

    def __str__(self):
        return self.name + " " + self.last_name

