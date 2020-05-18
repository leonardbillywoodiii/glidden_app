from django.test import TestCase
from faker import Faker

from cms.models import MemberAddress
from .setup import (user_setup, admin_user_setup)


class ModelTests(TestCase):

    def setUp(self):
        self.user = user_setup()
        self.admin_user = admin_user_setup()

    def test_member_address_is_created(self):
        faker = Faker('en_US')
        test_address = MemberAddress(
            address_type='Home',
            address_line_one=faker.street_address(),
            address_line_two=faker.secondary_address(),
            city=faker.city(),
            state=faker.state(),
            zipcode=faker.zipcode(),
            UserProfile=self.user
        )
        test_address.save()
        queried_address = MemberAddress.objects.get(id=1)

        object_string_test = test_address.address_line_one + '\n' + \
            test_address.address_line_two + '\n' + \
            test_address.city + ', ' + test_address.state + ' ' + test_address.zipcode  # noqa: E501

        self.assertEqual(test_address.address_type,
                         queried_address.address_type)
        self.assertEqual(test_address.address_line_one,
                         queried_address.address_line_one)
        self.assertEqual(test_address.address_line_two,
                         queried_address.address_line_two)
        self.assertEqual(test_address.city,
                         queried_address.city)
        self.assertEqual(test_address.state,
                         queried_address.state)
        self.assertEqual(test_address.state,
                         queried_address.state)
        self.assertEqual(test_address.zipcode,
                         queried_address.zipcode)
        self.assertEqual(test_address.UserProfile,
                         queried_address.UserProfile)
        self.assertEqual(object_string_test, str(test_address))
