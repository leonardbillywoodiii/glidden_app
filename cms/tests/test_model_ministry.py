from datetime import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from faker import Faker

from cms.models import Ministry, MemberAddress, GeneralAddress


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
