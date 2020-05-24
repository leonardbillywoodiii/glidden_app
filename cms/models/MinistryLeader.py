from django.db import models


class MinistryLeader(models.Model):
    UserProfile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    description = models.TextField()
    Ministry = models.ForeignKey('Ministry', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['UserProfile',
                       'description',
                       'Ministry'
                       ]

    def __str__(self):
        ministry_leader_str = str(self.UserProfile.first_name) + \
            ' ' + str(self.UserProfile.last_name) + ' - '
        ministry_leader_str += str(self.Ministry.name) + '\n'
        ministry_leader_str += self.description
        return ministry_leader_str
