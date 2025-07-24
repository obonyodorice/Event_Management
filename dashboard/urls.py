# dashboard/urls.py
from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('bookings/', views.booking_history, name='booking_history'),
    path('booking/<int:booking_id>/', views.booking_detail, name='booking_detail'),
]