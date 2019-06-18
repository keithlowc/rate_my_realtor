from django.contrib import admin

# Register your models here.

from .models import RealtorAgency, Agent, AgentsData

admin.site.register(RealtorAgency)
admin.site.register(Agent)
admin.site.register(AgentsData)
