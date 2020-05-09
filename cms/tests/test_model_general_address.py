from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from faker import Faker

from cms.models import GeneralAddress


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
