from django.db import models
from django.contrib.auth.models import User

class Habit(models.Model):
    user = models.ForeignKey(User, related_name="habits", on_delete=models.CASCADE)

    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(max_length=2000, blank=True, null=False)
    negative = models.BooleanField(default=False, blank=False, null=False)
    active = models.BooleanField(default=True, blank=False, null=False)


class HabitTemplate(models.Model):
    user = models.ForeignKey(User, related_name="habit_templates", on_delete=models.CASCADE)

    name = models.CharField(max_length=200, blank=True, null=False)
    description = models.TextField(max_length=200, blank=True, null=False)
    negative = models.BooleanField(default=False, blank=False, null=False)

    def create_new(self, user):
        return Habit(user=user, name=self.name, description=self.description, negative=self.negative)


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE, auto_created=True)
    # # friends = models.ManyToManyField(User, related_name="followers", blank=True)
    # favorite_habits = models.ManyToManyField(Habit, related_name="favorites", blank=True)
    # favorite_habit_templates = models.ManyToManyField(HabitTemplate, related_name="favorites", blank=True)
    # 
    # public_name = models.CharField(max_length=200, blank=True, null=True)
    # birthday = models.DateField(blank=True, null=True)

    # # SETTINGS
    # private_profile = models.BooleanField(default=False)
    # public_favorites = models.BooleanField(default=True)
    # public_friends = models.BooleanField(default=True)
    # public_habits = models.BooleanField(default=True)
    # public_habit_templates = models.BooleanField(default=True)
