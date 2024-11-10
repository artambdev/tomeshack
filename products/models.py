from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    visible_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_visible_name(self):
        return self.visible_name