from django.db import models

# Create your models here.

class RealtorAgency(models.Model):
    name = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(
        max_length=250, null=True, blank=True, unique=True)
    phone_number = models.CharField(
        max_length=50, null=False, blank=False, unique=True, default=0)

    def __str__(self):
        return f'{self.name}'

class Agent(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, default=None)
    last_name = models.CharField(max_length=50, blank=False, null=False, default=None)
    company = models.ForeignKey(RealtorAgency, on_delete=models.CASCADE)
    email = models.EmailField(
        max_length=250, null=True, blank=True, unique=True)
    phone_number = models.CharField(
        max_length=50, null=False, blank=False, unique=False)
    about = models.TextField(max_length=650, blank=False)
    rating = models.FloatField()

    def __str__(self):
        return f'{self.name} from {self.company.name}'

class AgentsData(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    comments = models.CharField(
        max_length=250, blank=False, null=False, default=None)
    rating = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    #created_by = models.something

    def __str__(self):
        return f'{self.agent.name} {self.agent.last_name} - Rated: {self.rating}'
    
    class meta:
        verbose_name = "Agent Data"
        verbose_name_plural = "Agent Data"


    
