from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setup(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='test.admin@test.com',
            first_name='Elias',
            last_name='Jackson',
            password='testpassword'
        )

        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test.user@test.com',
            first_name='John',
            last_name='Smith',
            password='anotherpassword'
        )

    def test_users_listed(self):
        self.setup()
        url = reverse('admin:cms_userprofile_changelist')
        responce = self.client.get(url)

        self.assertContains(responce, self.admin_user.first_name)
        self.assertContains(responce, self.admin_user.last_name)
        self.assertContains(responce, self.admin_user.email)

        self.assertContains(responce, self.user.first_name)
        self.assertContains(responce, self.user.last_name)
        self.assertContains(responce, self.user.email)
