import time
import datetime
import logging

from taggit.managers import TaggableManager
from simple_history.models import HistoricalRecords

from annoying.fields import AutoOneToOneField

from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet

from model_utils.models import TimeStampedModel

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Profile(TimeStampedModel, models.Model):
    """User's profile."""

    user = AutoOneToOneField(
        User, related_name="profile",
        on_delete=models.CASCADE, primary_key=True)

    private = models.BooleanField(default=False, blank=False, null=False)

    public_username = models.CharField(
        verbose_name="Public username", max_length=100,
        null=True, blank=True)

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