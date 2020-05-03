from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from datetime import datetime


class AdminSiteTests(TestCase):

    def setup(self):
        """Helper function that makes a user and superuser"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='test.admin@test.com',
            first_name='Elias',
            last_name='Jackson',
            password='testpassword',
            birthday=datetime(1983, 4, 17),
            sex='male'
        )

        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test.user@test.com',
            first_name='John',
            last_name='Smith',
            password='testpassword',
            birthday=datetime(1983, 4, 17),
            sex='male'
        )

    def test_users_listed(self):
        """Test users successfuly created and listed in Admin Page"""
        self.setup()
        url = reverse('admin:cms_userprofile_changelist')
        responce = self.client.get(url)

        self.assertContains(responce, self.admin_user.first_name)
        self.assertContains(responce, self.admin_user.last_name)
        self.assertContains(responce, self.admin_user.email)

        self.assertContains(responce, self.user.first_name)
        self.assertContains(responce, self.user.last_name)
        self.assertContains(responce, self.user.email)

    def test_user_change_page(self):
        """Test Admin change page working correctly"""
        self.setup()
        url = reverse('admin:cms_userprofile_change',
                      args=[self.user.id])
        responce = self.client.get(url)

        self.assertEqual(responce.status_code, 200)

    def test_user_add_page(self):
        """Test Admin add page is working correctly"""
        self.setup()
        url = reverse('admin:cms_userprofile_add')
        responce = self.client.get(url)

        self.assertEqual(responce.status_code, 200)
