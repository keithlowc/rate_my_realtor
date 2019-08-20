from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

'''
Custom form for default authentication model
'''
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number')

'''
Custom form for user credentials changed
'''
class CustomUserChangeForm(UserChangeForm):
    model = CustomUser
    fields = ('username','email')