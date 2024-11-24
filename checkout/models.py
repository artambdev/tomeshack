from django.db import models
from products.models import Book


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)

    country = models.CharField(max_length=30, null=False, blank=False)
    postcode = models.CharField(max_length=16, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=40, null=False, blank=False)
    street_address2 = models.CharField(max_length=40, null=True, blank=True)
    county = models.CharField(max_length=25, null=True, blank=True)

    date = models.DateTimeField(auto_now_add=True)

    order_total = models.DecimalField(max_digits=9, decimal_places=2, null=False, default=0)



class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    book = models.ForeignKey(Book, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False, editable=False)