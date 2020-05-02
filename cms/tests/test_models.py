from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        """Test creating a new user with and email successfull"""

        email = 'test.test@test.com'
        password = 'TestPassword'
        first_name = 'Joe'
        last_name = 'Smith'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
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
                password='TestPassword')
#
