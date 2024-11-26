from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import ReviewForm
from .models import Category, Book, Review


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

        self.review = Review(review_of=self.book,
            author=self.user,
            uid="review-uid",
            content="Review content",
            hidden=False
        )
        self.review.save()

        self.hidden = Review(review_of=self.book,
            author=self.user,
            uid="review-hidden-uid",
            content="Hidden content",
            hidden=True
        )
        self.hidden.save()

    def test_render_book_list(self):
        """
        Test that books appear on the book list
        """
        response = self.client.get(reverse(
            'products'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Book Title", response.content)

    def test_no_hidden_on_book_view(self):
        """
        Test that hidden reviews do not appear on the book view
        """
        response = self.client.get(reverse(
            'view_book', args=['book-uid']))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(b"Hidden content" in response.content)

    def test_hidden_for_superusers_on_main_page(self):
        """
        Test that hidden posts do appear for superusers
        """
        self.client.login(
            username="userName", password="passWord")
        response = self.client.get(reverse(
            'view_book', args=['book-uid']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hidden content", response.content)

    def test_render_book_view_page(self):
        """
        Test that a book can be viewed directly
        """
        response = self.client.get(reverse(
            'view_book', args=['book-uid']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Book Title", response.content)
        self.assertIsInstance(
            response.context['review_form'], ReviewForm)

    def test_successful_review_submission(self):
        """
        Test that a review can be successfully created
        """
        self.client.login(
            username="userName", password="passWord")
        review_data = {
            'content': 'This is a test review!'
        }
        response = self.client.post(reverse(
            'view_book', args=['book-uid']), review_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'This is a test review!',
            response.content
        )

    def test_successful_review_deletion(self):
        """
        Test that a post can be deleted
        And that the post no longer exists
        """
        self.client.login(
            username="userName", password="passWord")
        response = self.client.post(reverse(
            'delete_review', args=["review-uid"]), follow=True)
        self.assertEqual(response.status_code, 200)
