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
    title = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stars = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    def get_description(self):
        return f'"{self.description[:40]}..."'