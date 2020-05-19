from django.test import TestCase
from faker import Faker

from cms.models import MinistryLeader

from .setup import (admin_user_setup, general_address_setup,
                    member_address_setup, user_setup, ministry_setup)


class MinisteryLeaderModelTests(TestCase):

    def setUp(self):
        self.user = user_setup()
        self.admin_user = admin_user_setup()
        self.member_address = member_address_setup(self.user)
        self.general_address = general_address_setup(self.admin_user)
        self.ministry = ministry_setup(
            self.member_address, self.general_address)

    def test_ministry_leader_created(self):
        faker = Faker('en_US')
        test_ministry_leader = MinistryLeader(
            UserProfile=self.user,
            description=faker.paragraph(1, True, None),
            Ministry=self.ministry
        )
        test_ministry_leader.save()
        queried_ministery_leader = MinistryLeader.objects.get(id=1)

        test_ministry_leader_str_check = str(
            test_ministry_leader.UserProfile.first_name)
        test_ministry_leader_str_check += ' ' + \
            str(test_ministry_leader.UserProfile.last_name)
        test_ministry_leader_str_check += ' - '
        test_ministry_leader_str_check += str(
            test_ministry_leader.Ministry.name) + '\n'
        test_ministry_leader_str_check += test_ministry_leader.description

        self.assertEqual(test_ministry_leader.UserProfile,
                         queried_ministery_leader.UserProfile)
        self.assertEqual(test_ministry_leader.description,
                         queried_ministery_leader.description)
        self.assertEqual(test_ministry_leader.Ministry,
                         queried_ministery_leader.Ministry)
        self.assertEqual(test_ministry_leader_str_check,
                         str(test_ministry_leader))
