from django import forms
from realtor.models import Agent, AgentsData

'''
Form to control the addition of agents
'''
class AddAgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['name', 'last_name', 'company', 'email', 'phone_number', 'about', 'rating']

'''
Form to control the data of the agent submmited by an user
'''
class AddAgentDataForm(forms.ModelForm):
    class Meta:
        model = AgentsData
        fields = ['comments', 'rating']
