from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
import json
def index(request):
    """
    Render the index page with a floating shapes effect.
    """
    return render(request, 'index.html')

def about_view(request):
    """About page view with company information and statistics"""
    context = {
        'stats': {
            'venues': 150,
            'events': 2500,
            'customers': 1200,
            'cities': 25,
        },
        'team_members': [
            {
                'name': 'Sarah Johnson',
                'position': 'CEO & Founder',
                'image': 'images/team/avatar.jpg',  # Will look in static/images/team/
                'bio': 'Former event planner with 15+ years experience in luxury events.',
            },
            {
                'name': 'Michael Chen',
                'position': 'CTO',
                'image': 'images/team/avatar.jpg',
                'bio': 'Tech entrepreneur passionate about connecting people through technology.',
            },
            {
                'name': 'Emma Rodriguez',
                'position': 'Head of Partnerships',
                'image': 'images/team/avatar.jpg',
                'bio': 'Specialist in venue relationships and customer success.',
            },
        ]
    }
    return render(request, 'about.html', context)

def contact_view(request):
   
    if request.method == 'POST':
        
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()
        inquiry_type = request.POST.get('inquiry_type', 'general')
        
    
    return render(request, 'contact.html')

