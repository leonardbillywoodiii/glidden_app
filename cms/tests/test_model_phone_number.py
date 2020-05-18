from django.test import TestCase

from cms.models import PhoneNumber
from .setup import (user_setup, admin_user_setup)


class ModelTests(TestCase):

    def setUp(self):
        self.user = user_setup()
        self.admin_user = admin_user_setup()

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
