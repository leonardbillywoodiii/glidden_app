from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import datetime


class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        """Test creating a new user with and email successfull"""

        email = 'test.test@test.com'
        password = 'TestPassword'
        first_name = 'Joe'
        last_name = 'Smith'
        birthday = datetime(1983, 4, 17)
        sex = 'male'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            birthday=birthday,
            sex=sex
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

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
        user = get_user_model().objects.create_superuser(
            email='test@test.com',
            first_name='joe',
            last_name='bloe',
            password='!@#$%^&*()',
            birthday=datetime(1983, 4, 17),
            sex='male'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
