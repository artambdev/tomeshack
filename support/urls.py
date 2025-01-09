from . import views
from django.urls import path

urlpatterns = [
    path('', views.view_tickets, name='support'),
    path('create/', views.create_ticket, name='create_ticket'),
    path('<slug:uid>/', views.view_ticket, name='view_ticket'),
    path('<slug:uid>/resolve/', views.resolve_ticket, name='resolve_ticket'),
]