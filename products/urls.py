from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.book_list, name='products'),
]
