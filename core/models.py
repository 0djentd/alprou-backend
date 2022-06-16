import time
import datetime
import logging

from taggit.managers import TaggableManager
from simple_history.models import HistoricalRecords

from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet

from model_utils.models import TimeStampedModel

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Habit(TimeStampedModel, models.Model):
    """Object representing a habit."""
    user = models.ForeignKey(User,
                             related_name="habits",
                             on_delete=models.CASCADE)

    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(max_length=2000, blank=True, null=False)
    negative = models.BooleanField(default=False, blank=False, null=False)
    active = models.BooleanField(default=True, blank=False, null=False)
    public = models.BooleanField(default=False, blank=False, null=False)
    history = HistoricalRecords()
    tags = TaggableManager()

    # Days when habit was completed
    # completed: list[Day]

    def complete(self) -> bool:
        """Check habit as completed today.

        Returns False, if already completed today.
        """
        day = Day(user=self.user, habit=self)
        if len(self.completed) == 0:
            day.save()
            result = True
        else:
            timedelta = datetime.datetime.now() - self.completed[-1].datetime
            if timedelta.days < 1:
                if timedelta.days < 0:
                    raise ValueError
                result = False
            else:
                day.save()
                result = True
        logger.debug(f"Checking {self} as complete.")
        logger.debug(f"day: {day}")
        logger.debug(result)
        return result


class Day(models.Model):
    """Object representing date/time when user checked habit as completed."""
    user = models.ForeignKey(User,
                             related_name="days",
                             on_delete=models.CASCADE)
    habit = models.ForeignKey(Habit,
                              related_name="completed",
                              on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=False, blank=False, null=False)
    history = HistoricalRecords()


class Profile(TimeStampedModel, models.Model):
    """User's profile."""
    user = models.OneToOneField(User,
                                related_name="profile",
                                on_delete=models.CASCADE,
                                auto_created=True)
    public = models.BooleanField(default=False, blank=False, null=False)
    public_username = models.CharField(verbose_name="Public username", max_length=100, null=True, blank=False)
    profile_image = models.ImageField(null=True, blank=True)
    background_image = models.ImageField(null=True, blank=True)
    history = HistoricalRecords()

    @property
    def active_habits(self) -> QuerySet:
        active_habits =  self.user.habits.all().filter(active=True)
        return active_habits

    @property
    def habits(self) -> QuerySet:
        active_habits =  self.user.habits.all()
        return active_habits
