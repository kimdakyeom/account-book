from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url = '/accounts/registration/'
        self.login_url = '/accounts/login/'

        self.register_user_data = {
            'email': 'email@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }
        self.login_user_data = {
            'email': 'email@example.com',
            'password': 'testpassword'
        }
        return super().setUp()

    def tearDown(self):
        return super().tearDown()