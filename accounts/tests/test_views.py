from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from ..models import User
from .test_setup import TestSetUp

class TestViews(TestSetUp):
    def test_user_register(self):
        res = self.client.post(
            self.register_url, self.register_user_data, format='json'
        )
        self.assertEqual(res.data['user']['email'], self.register_user_data['email'])
        self.assertEqual(res.status_code, 201)

    def test_user_login(self):
        res = self.client.post(
            self.login_url, self.login_user_data, format='json'
        )
        self.assertEqual(res.status_code, 200)