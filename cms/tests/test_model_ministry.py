from django.test import TestCase
from faker import Faker

from cms.models import Ministry

from .setup import (admin_user_setup, general_address_setup,
                    member_address_setup, user_setup)


class MinistryModelTests(TestCase):

    def setUp(self):
        self.user = user_setup()
        self.admin_user = admin_user_setup()
        self.MemberAddress = member_address_setup(self.user)
        self.GeneralAddress = general_address_setup(self.admin_user)

    def test_ministry_is_created(self):
        faker = Faker()
        test_ministry = Ministry(
            name='Women of Grace',
            sex='Both',
            age_lower_bounds=16,
            age_upper_bounds=24,
            age_nickname='Teens and Young Adults',
            description=faker.paragraph(4, True, None),
            GeneralAddress=self.GeneralAddress,
            MemberAddress=self.MemberAddress
        )
        test_ministry.save()

        queried_ministry = Ministry.objects.get(id=1)

        test_ministry_str_check = test_ministry.name + '\n' + \
            'Gender: ' + test_ministry.sex + ' ' + \
            str(test_ministry.age_lower_bounds) + ' - ' + \
            str(test_ministry.age_upper_bounds) + '\n' + \
            test_ministry.age_nickname + '\n' + \
            test_ministry.description + '\n' + \
            str(test_ministry.GeneralAddress)

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
        self.assertEqual(test_ministry.GeneralAddress,
                         queried_ministry.GeneralAddress)
        self.assertEqual(test_ministry.MemberAddress,
                         queried_ministry.MemberAddress)
        self.assertEqual(test_ministry_str_check, str(queried_ministry))

    def test_ministry_is_created_no_GeneralAddress(self):
        faker = Faker()
        test_ministry = Ministry(
            name='Women of Grace',
            sex='Both',
            age_lower_bounds=16,
            age_upper_bounds=24,
            age_nickname='Teens and Young Adults',
            description=faker.paragraph(4, True, None),
            GeneralAddress=None,
            MemberAddress=self.MemberAddress
        )
        self.assertFalse(test_ministry.save())
        queried_ministry = Ministry.objects.get(id=1)

        test_ministry_str_check = test_ministry.name + '\n' + \
            'Gender: ' + test_ministry.sex + ' ' + \
            str(test_ministry.age_lower_bounds) + ' - ' + \
            str(test_ministry.age_upper_bounds) + '\n' + \
            test_ministry.age_nickname + '\n' + \
            test_ministry.description + '\n' + \
            str(test_ministry.MemberAddress)

        self.assertEqual(test_ministry_str_check, str(queried_ministry))

    def test_ministry_is_created_no_MemberAddress(self):
        faker = Faker()
        test_ministry = Ministry(
            name='Women of Grace',
            sex='Both',
            age_lower_bounds=16,
            age_upper_bounds=24,
            age_nickname='Teens and Young Adults',
            description=faker.paragraph(4, True, None),
            GeneralAddress=self.GeneralAddress,
            MemberAddress=None
        )
        self.assertFalse(test_ministry.save())

        queried_ministry = Ministry.objects.get(id=1)

        test_ministry_str_check = test_ministry.name + '\n' + \
            'Gender: ' + test_ministry.sex + ' ' + \
            str(test_ministry.age_lower_bounds) + ' - ' + \
            str(test_ministry.age_upper_bounds) + '\n' + \
            test_ministry.age_nickname + '\n' + \
            test_ministry.description + '\n' + \
            str(test_ministry.GeneralAddress)

        self.assertEqual(test_ministry_str_check, str(queried_ministry))
