from django.db import models


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Media(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    media_file = models.FileField(upload_to=user_directory_path)
    UserProfile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
