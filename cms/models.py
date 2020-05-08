from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


class UserProfileManager(BaseUserManager):
    """Manager for UserProfile Model"""

    def create_user(
            self, email, first_name, last_name, birthday, sex, password):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            birthday=birthday,
            sex=sex
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
            self, email, first_name, last_name, birthday, sex, password):
        """Create and save new superuser"""
        user = self.create_user(
            email, first_name, last_name, birthday, sex, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField()
    sex = models.CharField(max_length=10,
                           choices=(('M', 'Male'), ('F', 'Female'),)
                           )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'birthday', 'sex']

    def get_full_name(self):
        """Retrieve full name"""
        return self.first_name + self.last_name

    def get_short_name(self):
        """Retrieve short name of User"""
        return self.first_name

    def ___str___(self):
        """Return String representation"""
        return self.email


class PhoneNumber(models.Model):
    number = models.CharField(max_length=20)
    number_type = models.CharField(max_length=20, default='Cell')
    UserProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    REQUIRED_FIELDS = ['number', 'number_type']

    def __str__(self):
        """Return String representation as Cell: 936.555.1234"""
        return '{}: {}.{}.{}'.format(
            self.number_type,
            self.number[:3],
            self.number[3:6],
            self.number[6:]
        )


class MemberAddress(models.Model):
    address_type = models.CharField(max_length=100, default='Home')
    address_line_one = models.CharField(max_length=100)
    address_line_two = models.CharField(max_length=100, default=None)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    UserProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    REQUIRED_FIELDS = ['address_type',
                       'address_line_one',
                       'address_line_two',
                       'city',
                       'state',
                       'zipcode'
                       ]

    def __str__(self):
        address = self.address_line_one + '\n'
        if (self.address_line_two is not None or ''):
            address += self.address_line_two + '\n'
        address += self.city + ', ' + self.state + ' ' + self.zipcode
        return address


class GeneralAddress(models.Model):
    name = models.CharField(max_length=100)
    address_line_one = models.CharField(max_length=100)
    address_line_two = models.CharField(max_length=100, default=None)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    added_by_user_id = models.ForeignKey(
        UserProfile, on_delete=models.DO_NOTHING)

    REQUIRED_FIELDS = ['name',
                       'address_line_one',
                       'address_line_two',
                       'city',
                       'state',
                       'zipcode',
                       'added_by_user_id'
                       ]

    def __str__(self):
        address = self.name + '\n'
        address += self.address_line_one + '\n'
        if (self.address_line_two is not None or ''):
            address += self.address_line_two + '\n'
        address += self.city + ', ' + self.state + ' ' + self.zipcode
        return address


class Ministry(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10, choices=(
        ('M', 'Male'), ('F', 'Female'), ('B', 'Both'),), default='Both')
    age_lower_bounds = models.IntegerField(default=None)
    age_upper_bounds = models.IntegerField(default=None)
    age_nickname = models.CharField(max_length=50, default=None)
    description = models.TextField()
    general_address = models.ForeignKey(
        GeneralAddress, on_delete=models.DO_NOTHING, blank=True, null=True)
    member_address = models.ForeignKey(
        MemberAddress, on_delete=models.DO_NOTHING, blank=True, null=True)

    REQUIRED_FIELDS = ['name',
                       'sex',
                       'description',
                       ]

    def __str__(self):
        ministry_str = self.name + '\n'
        ministry_str += 'Gender: ' + self.sex + ' '
        if (self.age_lower_bounds and self.age_upper_bounds is not None):
            ministry_str += str(self.age_lower_bounds) + ' - ' + str(self.age_upper_bounds) + '\n'  # noqa E501
        if (self.age_nickname is not None):
            ministry_str += self.age_nickname + '\n'
        ministry_str += self.description + '\n'
        if (self.general_address is not None):
            ministry_str += str(self.general_address)
        elif(self.member_address is not None):
            ministry_str += str(self.member_address)
        return ministry_str
