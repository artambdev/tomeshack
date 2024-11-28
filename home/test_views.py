from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase


class TestListViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="userName",
            password="passWord",
            email="sample@email.com"
        )

    def test_render_index(self):
        """
        Test that the index works
        """
        response = self.client.get(reverse(
            'home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Tomeshack", response.content)
