from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='products'),
    path('<slug:uid>/', views.view_book, name='view_book'),
    path('<slug:uid>/delete/', views.delete_review, name='delete_review'),
    path('<slug:uid>/hide/', views.hide_review, name='hide_review'),
]
