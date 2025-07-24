from django.urls import path
from . import views

app_name = 'venue'

urlpatterns = [
    path('', views.VenueListView.as_view(), name='list'),
    path('<int:pk>/', views.venue_detail, name='detail'),
]