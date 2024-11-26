from .models import Review
from django import forms


class ReviewForm(forms.ModelForm):
    """
    Form for creating reviews
    """
    class Meta:
        model = Review
        fields = ('content',)