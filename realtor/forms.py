from django import forms
from realtor.models import Agent


class AddAgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['name', 'last_name', 'company', 'email', 'phone_number', 'about', 'rating']
