from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from cms.models import PhoneNumber


class ModelTests(TestCase):

    def setUp(self):
        """ Setup for model testing. Creates User and Superuser """

        email = 'test.test@test.com'
        password = 'TestPassword'
        first_name = 'Joe'
        last_name = 'Smith'
        birthday = datetime(1983, 4, 17)
        sex = 'male'
        self.user = get_user_model().objects.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            birthday=birthday,
            sex=sex
        )

        self.admin_user = get_user_model().objects.create_superuser(
            email='test@test.com',
            first_name='joe',
            last_name='bloe',
            password='!@#$%^&*()',
            birthday=datetime(1983, 4, 17),
            sex='male'
        )

    def test_phone_number_is_created(self):
        test_number = PhoneNumber(
            number='9365551481',
            number_type='Home',
            UserProfile=self.user
        )
        test_number.save()
        queried_number = PhoneNumber.objects.get(id=1)

        self.assertEqual(test_number.number, queried_number.number)
        self.assertEqual(test_number.number_type, queried_number.number_type)
        self.assertEqual(queried_number.UserProfile.id, self.user.id)
        self.assertEqual(str(queried_number), 'Home: 936.555.1481')
