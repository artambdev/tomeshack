import random
import string
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    visible_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_visible_name(self):
        return self.visible_name


class Book(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    uid = models.SlugField(max_length=200, default=None, null=True)
    title = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stars = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    def get_description(self):
        return f'"{self.description[:40]}..."'


class Post(models.Model):
    """
    Class to define the review model
    """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews"
    )
    uid = models.SlugField(max_length=200, default=None, null=True)
    review_of = models.ForeignKey(
        Book,
        on_delete=models.SET_NULL,
        related_name="reviews"
    )
    content = models.TextField(max_length=200)
    stars = models.IntegerField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    hidden = models.BooleanField()

    def Meta(self):
        """
        Show the newest reviews first in admin screen
        """
        ordering = ["-created_on"]

    def __str__(self):
        return f'"{self.content[:15]}..." | written by {self.author}'
