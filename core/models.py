from django.db import models
from django.contrib.auth.models import User


class Habit(models.Model):
    """Object representing a habit."""
    user = models.ForeignKey(User,
                             related_name="habits",
                             on_delete=models.CASCADE)

    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(max_length=2000, blank=True, null=False)
    negative = models.BooleanField(default=False, blank=False, null=False)
    active = models.BooleanField(default=True, blank=False, null=False)

    # Days when habit was completed
    # completed: list[Day]

    def complete(self):
        """Check habit as completed today."""
        day = Day(user=self.user, habit=self)
        day.save()
        return


class Day(models.Model):
    """Object representing date/time when user checked habit as completed."""
    user = models.ForeignKey(User,
                             related_name="days",
                             on_delete=models.CASCADE)
    habit = models.ForeignKey(Habit,
                              related_name="completed",
                              on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    """User's profile."""
    user = models.OneToOneField(User,
                                related_name="profile",
                                on_delete=models.CASCADE,
                                auto_created=True)
