from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

# Create your tests here.
class UserAppTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            first_name="Ejike",
            last_name="Sylva",
            email="test@example.com",
            password="testpassword"
        )

    def test_create_user(self):
        user = self.user
        self.assertEqual(user.first_name, 'Ejike')
        self.assertEqual(user.last_name, 'Sylva')
        self.assertTrue(user.check_password('testpassword'))

    def test_authentication(self):
        response = self.client.post('/api/auth/login/', {
            'email': 'test@example.com',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)
