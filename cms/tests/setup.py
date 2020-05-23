from django.contrib.auth import get_user_model

import random
from cms.models import MemberAddress, GeneralAddress, Ministry, UserProfile
from faker import Faker


def user_setup():
    """ Creates a User"""
    faker = Faker('en_US')
    user = get_user_model().objects.create_user(
        email=faker.email(),
        password=faker.password(),
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        birthday=faker.date_of_birth(minimum_age=18, maximum_age=80),
        sex=random.choice(['Male', 'Female'])
    )
    return user


def admin_user_setup():
    faker = Faker('en_US')
    admin_user = get_user_model().objects.create_superuser(
        email=faker.email(),
        password=faker.password(),
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        birthday=faker.date_of_birth(minimum_age=18, maximum_age=80),
        sex=random.choice(['Male', 'Female'])
    )
    return admin_user


def member_address_setup(user: UserProfile):
    """Creates one Member Address"""
    faker = Faker('en_US')
    member_address = MemberAddress(
        address_type='Home',
        address_line_one=faker.street_address(),
        address_line_two=faker.secondary_address(),
        city=faker.city(),
        state=faker.state(),
        zipcode=faker.zipcode(),
        UserProfile=user
    )
    member_address.save()
    return member_address


def general_address_setup(admin_user: UserProfile):
    """Creates one General Address"""
    faker = Faker('en_US')
    general_address = GeneralAddress(
        name=faker.company() + ' ' + faker.company_suffix(),
        address_line_one=faker.street_address(),
        address_line_two=faker.secondary_address(),
        city=faker.city(),
        state=faker.state(),
        zipcode=faker.zipcode(),
        added_by_user_id=admin_user
    )
    general_address.save()
    return general_address


def ministry_setup(member_address: MemberAddress,
                   general_address: GeneralAddress):
    faker = Faker('en_US')
    ministry = Ministry(
        name='Women and Men of Grace',
        sex='Both',
        age_lower_bounds=16,
        age_upper_bounds=24,
        age_nickname='Teens and Young Adults',
        description=faker.paragraph(4, True, None),
        GeneralAddress=general_address,
        MemberAddress=member_address
    )
    ministry.save()
    return ministry
