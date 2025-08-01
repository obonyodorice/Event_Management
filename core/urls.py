"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index, about_view, contact_view

urlpatterns = [
    path('', index, name='index'), 
    path('about/', about_view, name='about'),
    path('contact/',contact_view, name='contact'), 
    path('admin/', admin.site.urls),
    path('venue/',include('venue.urls')), 
    path('bookings/', include('bookings.urls')),  # Include URLs from the venue app
    path('users/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),  # Include URLs from the dashboard app
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
