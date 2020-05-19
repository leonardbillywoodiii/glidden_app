from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from cms.models import UserProfile


class UserProfileModelTests(TestCase):

    def setUp(self):
        """ Setup for model testing. Creates User and Superuser """

        self.user = get_user_model().objects.create_user(
            email='test.test@test.com',
            password='TestPassword',
            first_name='Joe',
            last_name='Smith',
            birthday=datetime(1983, 4, 17),
            sex='male'
        )

        self.admin_user = get_user_model().objects.create_superuser(
            email='test@test.com',
            first_name='joe',
            last_name='bloe',
            password='!@#$%^&*()',
            birthday=datetime(1983, 4, 17),
            sex='male'
        )

    def test_create_user_with_email_successfull(self):
        """Test creating a new user with and email successfull"""
        user = UserProfile.objects.get(id=1)

        self.assertEqual(self.user.email, user.email)
        self.assertTrue(user.check_password('TestPassword'))

    def test_new_user_invalid_email(self):
        """Test if error on invalid or no email"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                first_name='Elias',
                last_name='Smith',
                password='TestPassword',
                birthday=datetime(1983, 4, 17),
                sex='male'
            )

    def test_create_new_superuser_successfull(self):
        """Test creating a new superuser"""

        self.assertTrue(self.admin_user.is_superuser)
        self.assertTrue(self.admin_user.is_staff)
