from django.db import models
from django.contrib.auth.models import AbstractUser

'''
Custom user model to allow addition of phone_number to default auth model.
'''
class CustomUser(AbstractUser):
    # Add other fields here!
    phone_number = models.CharField(max_length=50, blank=False, default=0)
    
    def __str__(self):
        return self.email
