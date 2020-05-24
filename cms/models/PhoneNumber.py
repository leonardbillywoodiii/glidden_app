from django.db import models


class PhoneNumber(models.Model):
    number = models.CharField(max_length=20)
    number_type = models.CharField(max_length=20, default='Cell')
    UserProfile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)

    REQUIRED_FIELDS = ['number', 'number_type']

    def __str__(self):
        """Return String representation as Cell: 936.555.1234"""
        return '{}: {}.{}.{}'.format(
            self.number_type,
            self.number[:3],
            self.number[3:6],
            self.number[6:]
        )
