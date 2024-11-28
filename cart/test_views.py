from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from products.models import Category, Book


class TestListViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="userName",
            password="passWord",
            email="sample@email.com"
        )

        self.category = Category(
            name="category-name",
            visible_name="Category Name"
        )
        self.category.save()

        self.book = Book(
            category=self.category,
            uid="book-uid",
            title="Book Title",
            description="Sample Description",
            price=20,
            stars=5
        )
        self.book.save()

    def test_add_to_cart(self):
        """
        Test that the cart screen can be accessed
        """
        response = self.client.get(reverse(
            'view_cart'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Your Cart", response.content)
