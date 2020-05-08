from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from faker import Faker

from cms.models import (MemberAddress,
                        PhoneNumber,
                        UserProfile,
                        GeneralAddress,
                        Ministry
                        )


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

    def address_set_up(self):
        faker = Faker('en_US')
        self.member_address = MemberAddress(
            address_type='Home',
            address_line_one=faker.street_address(),
            address_line_two=faker.secondary_address(),
            city=faker.city(),
            state=faker.state(),
            zipcode=faker.zipcode(),
            UserProfile=self.user
        )
        self.general_address = GeneralAddress(
            name=faker.company() + ' ' + faker.company_suffix(),
            address_line_one=faker.street_address(),
            address_line_two=faker.secondary_address(),
            city=faker.city(),
            state=faker.state(),
            zipcode=faker.zipcode(),
            added_by_user_id=self.admin_user
        )
        self.general_address.save()
        self.member_address.save()

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

    def test_ministry_is_created(self):
        faker = Faker()
        self.address_set_up()
        test_ministry = Ministry(
            name='Women of Grace',
            sex='Both',
            age_lower_bounds=16,
            age_upper_bounds=24,
            age_nickname='Teens and Young Adults',
            description=faker.paragraph(4, True, None),
            general_address=self.general_address,
            member_address=self.member_address
        )
        test_ministry.save()

        queried_ministry = Ministry.objects.get(id=1)

        test_ministry_str_check = test_ministry.name + '\n' + \
            'Gender: ' + test_ministry.sex + ' ' + \
            str(test_ministry.age_lower_bounds) + ' - ' + \
            str(test_ministry.age_upper_bounds) + '\n' + \
            test_ministry.age_nickname + '\n' + \
            test_ministry.description + '\n' + \
            str(test_ministry.general_address)

        self.assertEqual(test_ministry.name,
                         queried_ministry.name)
        self.assertEqual(test_ministry.sex,
                         queried_ministry.sex)
        self.assertEqual(test_ministry.age_lower_bounds,
                         queried_ministry.age_lower_bounds)
        self.assertEqual(test_ministry.age_upper_bounds,
                         queried_ministry.age_upper_bounds)
        self.assertEqual(test_ministry.age_nickname,
                         queried_ministry.age_nickname)
        self.assertEqual(test_ministry.description,
                         queried_ministry.description)
        self.assertEqual(test_ministry.general_address,
                         queried_ministry.general_address)
        self.assertEqual(test_ministry.member_address,
                         queried_ministry.member_address)
        self.assertEqual(test_ministry_str_check, str(queried_ministry))

    def test_ministry_is_created_no_general_address(self):
        faker = Faker()
        self.address_set_up()
        test_ministry = Ministry(
            name='Women of Grace',
            sex='Both',
            age_lower_bounds=16,
            age_upper_bounds=24,
            age_nickname='Teens and Young Adults',
            description=faker.paragraph(4, True, None),
            general_address=None,
            member_address=self.member_address
        )
        self.assertFalse(test_ministry.save())
        queried_ministry = Ministry.objects.get(id=1)

        test_ministry_str_check = test_ministry.name + '\n' + \
            'Gender: ' + test_ministry.sex + ' ' + \
            str(test_ministry.age_lower_bounds) + ' - ' + \
            str(test_ministry.age_upper_bounds) + '\n' + \
            test_ministry.age_nickname + '\n' + \
            test_ministry.description + '\n' + \
            str(test_ministry.member_address)

        self.assertEqual(test_ministry_str_check, str(queried_ministry))

    def test_ministry_is_created_no_member_address(self):
        faker = Faker()
        self.address_set_up()
        test_ministry = Ministry(
            name='Women of Grace',
            sex='Both',
            age_lower_bounds=16,
            age_upper_bounds=24,
            age_nickname='Teens and Young Adults',
            description=faker.paragraph(4, True, None),
            general_address=self.general_address,
            member_address=None
        )
        self.assertFalse(test_ministry.save())

        queried_ministry = Ministry.objects.get(id=1)

        test_ministry_str_check = test_ministry.name + '\n' + \
            'Gender: ' + test_ministry.sex + ' ' + \
            str(test_ministry.age_lower_bounds) + ' - ' + \
            str(test_ministry.age_upper_bounds) + '\n' + \
            test_ministry.age_nickname + '\n' + \
            test_ministry.description + '\n' + \
            str(test_ministry.general_address)

        self.assertEqual(test_ministry_str_check, str(queried_ministry))
