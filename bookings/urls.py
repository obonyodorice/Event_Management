from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('create/<int:venue_id>/', views.create_booking, name='create_booking'),
    path('success/<int:booking_id>/', views.booking_success, name='booking_success'),
]