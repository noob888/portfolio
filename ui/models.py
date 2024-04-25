from django.db import models

# Create your models here.

class ContactModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

class HomeContactModel(models.Model):
    email = models.EmailField(unique=True)