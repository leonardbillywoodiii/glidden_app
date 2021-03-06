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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
