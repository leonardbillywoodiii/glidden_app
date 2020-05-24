from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    UserProfile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = [
        'title',
        'body',
        'UserProfile'
    ]

    def __str__(self):
        post_str = self.UserProfile.get_full_name() + '\n'
        post_str += self.created_at
        if self.created_at is not self.updated_at:
            post_str += ' modified: ' + self.updated_at
        post_str += '\n' + self.title + '\n'
        post_str += self.body
        return post_str
