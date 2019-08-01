from django.db import models
from users.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator

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
    rating = models.FloatField(
        validators=[MaxValueValidator(100), MinValueValidator(0)])
        
    def __str__(self):
        return f'{self.name} from {self.company.name}'

class AgentsData(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    comments = models.TextField(
        max_length=350, blank=False, null=False, default=None)
    rating = models.FloatField(
        validators=[MaxValueValidator(100), MinValueValidator(0)], default=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, 
                                    related_name='user_created_by',
                                    default=None, null=True, blank=True)

    def __str__(self):
        return f'{self.agent.name} {self.agent.last_name} - Rated: {self.rating}'
    
    class meta:
        verbose_name = "Agent Data"
        verbose_name_plural = "Agent Data"

class Background(models.Model):
    tweet_id = models.IntegerField()
    tweet_txt = models.CharField(max_length=5000, blank=False, null=False, default=None)

    def __str__(self):
        return f'{self.tweet_id}'


    
