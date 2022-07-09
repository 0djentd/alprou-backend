import logging

from simple_history.models import HistoricalRecords

from annoying.fields import AutoOneToOneField

from django.db import models
from django.contrib.auth.models import User

from model_utils.models import TimeStampedModel

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Profile(TimeStampedModel, models.Model):
    """User's profile."""

    user = AutoOneToOneField(
        User, related_name="profile",
        on_delete=models.CASCADE, primary_key=True)
    public_username = models.CharField(
        verbose_name="Public username", max_length=100,
        null=True, blank=True)
    history = HistoricalRecords()

    @property
    def username(self):
        if self.public_username:
            return self.public_username
        else:
            return self.user.username

    def __str__(self):
        return f"{self.user.username}'s profile"
