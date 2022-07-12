import secrets
from typing import Any

from rest_framework.test import APITestCase
from core.models import User, Profile
from django.contrib.auth.forms import UserCreationForm

from pydantic import BaseModel


def register_user(username, password):
    data = dict(username=username,
                password1=password,
                password2=password)
    form = UserCreationForm(data)
    if form.is_valid():
        form.save()
    else:
        raise ValueError
    user = User.objects.get(username=username)
    return user


class UserData(BaseModel):
    username: str
    password: str
    instance: Any

    def __init__(self, register_user=False):
        username = secrets.token_urlsafe()
        password = secrets.token_urlsafe()
        user = User(username=username)
        user.set_password(password)
        user.save()
        user.refresh_from_db()
        data = {"username": username,
                "password": password,
                "instance": user}
        super().__init__(**data)


class UserProfileTests(APITestCase):
    def setUp(self):
        self.users = [UserData() for _ in range(3)]
        self.user = self.users[0].instance
        self.profile = self.users[0].instance.profile

    def test_user_type(self):
        self.assertIsInstance(self.user, User)

    def test_profile_type(self):
        self.assertIsInstance(self.profile, Profile)

    def test_user_id(self):
        self.assertEqual(self.user.id, 1)

    def test_user_profile(self):
        self.assertEqual(self.user.profile, self.profile)
