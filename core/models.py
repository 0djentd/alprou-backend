from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    negative = models.BooleanField(default=False)
    days_completed = ArrayField(models.DateTimeField(blank=False, null=False), blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, auto_created=True)
