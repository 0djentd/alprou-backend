from rest_framework.test import APITestCase
from core.models import User, Profile


class UsersTests(APITestCase):
    def setUp(self):
        user = User(username="test_user")
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

    def test_user_username(self):
        self.assertEqual(self.user.username, "test_user")

    def test_user_email(self):
        self.assertEqual(self.user.email, "")

    def test_profile_user_id(self):
        self.assertEqual(self.profile.user.id, 1)

    def test_user_profile(self):
        self.assertEqual(self.user.profile, self.profile)
