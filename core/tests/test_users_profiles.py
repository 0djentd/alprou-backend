import secrets

from rest_framework.test import APITestCase
from core.models import User, Profile
from django.contrib.auth.forms import UserCreationForm


class UserProfileTests(APITestCase):
    def create_username_and_password(self):
        self._USERNAME = secrets.token_urlsafe()
        self._PASSWORD = secrets.token_urlsafe()

    def setUp(self):
        self.create_username_and_password()
        user = User(username=self._USERNAME)
        user.set_password(self._PASSWORD)
        user.save()
        user.refresh_from_db()
        self.user = user
        self.profile = user.profile

    def test_user_type(self):
        self.assertIsInstance(self.user, User)

    def test_profile_type(self):
        self.assertIsInstance(self.profile, Profile)

    def test_user_id(self):
        self.assertEqual(self.user.id, 1)

    def test_profile_user_id(self):
        self.assertEqual(self.user.profile.id, 1)

    def test_profile_user_id(self):
        self.assertEqual(self.profile.user.id, 1)

    def test_user_profile(self):
        self.assertEqual(self.user.profile, self.profile)


class UserRegisterTests(UserProfileTests):
    def setUp(self):
        self.create_username_and_password()
        data = dict(username=self._USERNAME,
                    password1=self._PASSWORD,
                    password2=self._PASSWORD)
        form = UserCreationForm(data)
        if form.is_valid():
            form.save()
        else:
            print(form.fields)
            print(form.data)
            print(form.error_messages)
            raise ValueError
        user = User.objects.get(username=self._USERNAME)
        self.user = user
        self.profile = user.profile
