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

    user = models.ForeignKey(User, related_name="habits", on_delete=models.CASCADE)

    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(max_length=2000, blank=True, null=False)
    negative = models.BooleanField(default=False, blank=False, null=False)
    active = models.BooleanField(default=True, blank=False, null=False)
    private = models.BooleanField(default=False, blank=False, null=False)
    history = HistoricalRecords()
    tags = TaggableManager(blank=True)

    # Days when habit was completed
    # completed: list[Day]

    def done(self) -> bool:
        """Check habit as completed today.

        Returns False, if already completed today.
        """
        day = Day(user=self.user, habit=self)
        completed_count = len(self.completed.all())
        if completed_count == 0:
            day.save()
            result = True
        else:
            timedelta = self._get_timedelta()
            if timedelta.days < 1:
                result = False
            else:
                day.save()
                result = True
        logger.debug(f"Checking {self} as complete.")
        logger.debug(f"day: {day}")
        logger.debug(result)
        return result

    @property
    def completed_today(self) -> bool:
        completed_count = len(self.completed.all())
        if completed_count == 0:
            result = False
        else:
            timedelta = self._get_timedelta()
            result = timedelta.days == 0
        return result

    def _get_timedelta(self):
        completed_count = len(self.completed.all())
        last = self.completed.all()[completed_count - 1].datetime
        now = datetime.datetime.now(datetime.timezone.utc)
        timedelta = now - last
        logger.debug(f"{last} - {now} = {timedelta}")
        if timedelta < timedelta - timedelta:
            raise ValueError
        return timedelta

    def __str__(self):
        return f"{self.user.username}'s habit '{self.name}'"


class Day(models.Model):
    """Object representing date/time when user checked habit as completed."""

    user = models.ForeignKey(User, related_name="days", on_delete=models.CASCADE)
    habit = models.ForeignKey(Habit, related_name="completed", on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    private = models.BooleanField(default=False, blank=False, null=False)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.user.username}'s '{self.habit.name}' ({self.datetime})"


class Profile(TimeStampedModel, models.Model):
    """User's profile."""

    user = models.OneToOneField(
        User, related_name="profile", on_delete=models.CASCADE, auto_created=True
    )
    private = models.BooleanField(default=False, blank=False, null=False)
    public_username = models.CharField(
        verbose_name="Public username", max_length=100, null=True, blank=False
    )
    profile_image = models.ImageField(null=True, blank=True)
    background_image = models.ImageField(null=True, blank=True)
    history = HistoricalRecords()

    @property
    def username(self):
        if self.public_username:
            return self.public_username
        else:
            return self.user.username

    @property
    def active_habits(self) -> QuerySet:
        active_habits = self.user.habits.all().filter(active=True)
        return active_habits

    @property
    def habits(self) -> QuerySet:
        active_habits = self.user.habits.all()
        return active_habits

    def __str__(self):
        return f"{self.user.username}'s profile"
