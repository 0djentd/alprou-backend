import secrets

from typing import Any

from rest_framework.test import APITestCase
from core.models import User, Profile
from django.contrib.auth.forms import UserCreationForm
from django.test import TestCase

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

    def __init__(self, register=False):
        username = secrets.token_urlsafe()
        password = secrets.token_urlsafe()
        if register_user:
            user = register_user(username, password)
        else:
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
        self.users = [UserData(register=True) for _ in range(3)]

    def test_user_type(self):
        for user in self.users:
            with self.subTest(user=user.instance):
                self.assertIsInstance(user.instance, User)

    def test_profile_type(self):
        for user in self.users:
            with self.subTest(user=user.instance):
                self.assertIsInstance(user.instance.profile, Profile)

    def test_user_id(self):
        for id, user in enumerate(self.users):
            with self.subTest(user=user.instance):
                self.assertEqual(user.instance.id, id + 1)


class AuthTests(TestCase):
    def setUp(self):
        self.users = [UserData() for _ in range(3)]
