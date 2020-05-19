from django.test import TestCase
from faker import Faker

from cms.models import GeneralAddress
from .setup import (user_setup, admin_user_setup)


class GeneralAddressModelTests(TestCase):

    def setUp(self):
        self.user = user_setup()
        self.admin_user = admin_user_setup()

    def test_general_address_is_created(self):
        faker = Faker('en_US')
        test_address = GeneralAddress(
            name=faker.company() + ' ' + faker.company_suffix(),
            address_line_one=faker.street_address(),
            address_line_two=faker.secondary_address(),
            city=faker.city(),
            state=faker.state(),
            zipcode=faker.zipcode(),
            added_by_user_id=self.admin_user
        )
        test_address.save()
        queried_address = GeneralAddress.objects.get(id=1)

        object_string_test = test_address.name + '\n' + \
            test_address.address_line_one + '\n' + \
            test_address.address_line_two + '\n' + \
            test_address.city + ', ' + test_address.state + ' ' + test_address.zipcode  # noqa: E501

        self.assertEqual(test_address.name,
                         queried_address.name)
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
        self.assertEqual(test_address.added_by_user_id,
                         queried_address.added_by_user_id)
        self.assertEqual(object_string_test, str(test_address))
