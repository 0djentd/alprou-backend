from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, auto_created=True)


class Day(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    negative = models.BooleanField(default=False)
