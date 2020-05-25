from django.db import models


class Ministry(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10, choices=(
        ('M', 'Male'), ('F', 'Female'), ('B', 'Both'),), default='Both')
    age_lower_bounds = models.IntegerField(default=None)
    age_upper_bounds = models.IntegerField(default=None)
    age_nickname = models.CharField(max_length=50, default=None)
    description = models.TextField()
    GeneralAddress = models.ForeignKey(
        'GeneralAddress', on_delete=models.DO_NOTHING, blank=True, null=True)
    MemberAddress = models.ForeignKey(
        'MemberAddress', on_delete=models.DO_NOTHING, blank=True, null=True)
<<<<<<< HEAD
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
=======
>>>>>>> master

    REQUIRED_FIELDS = [
        'name',
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
        if (self.GeneralAddress is not None):
            ministry_str += str(self.GeneralAddress)
        elif(self.MemberAddress is not None):
            ministry_str += str(self.MemberAddress)
        return ministry_str
