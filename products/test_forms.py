from django.test import TestCase
from .forms import ReviewForm


class TestReviewForm(TestCase):
    def test_form_is_valid(self):
        """
        Test that form is valid if content is properly filled out
        """
        review_form = ReviewForm({
            'content': 'This is an awesome book!'
        })
        self.assertTrue(post_form.is_valid(), msg='Post form is not valid but should be')

    def test_form_no_content_is_invalid(self):
        """
        Test that form is invalid if has no content
        """
        post_form = ReviewForm({
            'content': '',
        })
        self.assertFalse(
            post_form.is_valid(),
            msg='Post form valid despite empty content'
        )
