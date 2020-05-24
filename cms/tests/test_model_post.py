from django.test import TestCase
from faker import Faker
from cms.models import Post
from .setup import user_setup


class PostModelTests(TestCase):

    def setUp(self):
        self.user = user_setup()

    def test_post_created(self):
        faker = Faker('en_US')
        test_post = Post(
            title=faker.sentence(),
            body=faker.paragraph(),
            UserProfile=self.user)
        test_post.save()

        queried_post = Post.objects.get(id=1)

        self.assertEqual(test_post.title, queried_post.title)
        self.assertEqual(test_post.body, queried_post.body)
        self.assertEqual(test_post.UserProfile, queried_post.UserProfile)
