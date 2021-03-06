from django.db import models


class MemberAddress(models.Model):
    address_type = models.CharField(max_length=100, default='Home')
    address_line_one = models.CharField(max_length=100)
    address_line_two = models.CharField(max_length=100, default=None)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    UserProfile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
