from django.test import Client, TestCase
from django.urls import reverse

from .setup import admin_user_setup, user_setup


class AdminSiteTests(TestCase):

    def setUp(self):
        """Helper function that makes a user and superuser"""
        self.client = Client()
        self.admin_user = admin_user_setup()

        self.client.force_login(self.admin_user)
        self.user = user_setup()

    def test_users_listed(self):
        """Test users successfuly created and listed in Admin Page"""
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
        url = reverse('admin:cms_userprofile_change',
                      args=[self.user.id])
        responce = self.client.get(url)

        self.assertEqual(responce.status_code, 200)

    def test_user_add_page(self):
        """Test Admin add page is working correctly"""
        url = reverse('admin:cms_userprofile_add')
        responce = self.client.get(url)

        self.assertEqual(responce.status_code, 200)
