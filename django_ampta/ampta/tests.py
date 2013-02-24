"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
import unittest
from django.core.urlresolvers import reverse



# class SimpleTest(TestCase):
#     def test_basic_addition(self):
#         """
#         Tests that 1 + 1 always equals 2.
#         """
#         self.assertEqual(1 + 1, 2)



# class MyTests(TestCase):
#     def test_views(self):
#         response = self.client.get("/projects/")
#         self.assertEqual(response.status_code, 200)


class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('fakename3', 'fake@mail.com', 'mypassword')

    def test_MyView(self):
        User.objects.create_user('fakename', 'fake@mail.com', 'mypassword')
        #use test client to perform login
        user = self.client.login(username='fakename', password='mypassword')
        response = self.client.get('')

    def test_home_view(self):
         response = self.client.get(reverse('home'))