from . import views
from django.urls import path

urlpatterns = [
    path('', views.view_tickets, name='tickets'),
    path('create/', views.create_ticket, name='create_ticket'),
]