from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
from django.utils import timezone
from datetime import timedelta
from bookings.models import Booking
from venue.models import Venue

@login_required
def dashboard(request):
    user = request.user
    
    # Get user's bookings
    bookings = Booking.objects.filter(user=user).order_by('-created_at')
    
    # Get booking statistics
    total_bookings = bookings.count()
    total_spent = bookings.aggregate(Sum('total_price'))['total_price__sum'] or 0
    
    # Get upcoming bookings (future events)
    today = timezone.now().date()
    upcoming_bookings = bookings.filter(event_date__gte=today).order_by('event_date')[:3]
    
    # Get recent bookings (last 3)
    recent_bookings = bookings[:3]
    
    # Get booking status counts (you can extend this based on your booking status field)
    # For now, we'll categorize by date
    past_bookings_count = bookings.filter(event_date__lt=today).count()
    upcoming_bookings_count = bookings.filter(event_date__gte=today).count()
    
    # Get monthly booking data for chart (last 6 months)
    six_months_ago = today - timedelta(days=180)
    monthly_bookings = []
    
    for i in range(6):
        month_start = today.replace(day=1) - timedelta(days=30*i)
        month_end = (month_start + timedelta(days=32)).replace(day=1) - timedelta(days=1)
        month_bookings = bookings.filter(
            event_date__gte=month_start, 
            event_date__lte=month_end
        ).count()
        monthly_bookings.append({
            'month': month_start.strftime('%b %Y'),
            'count': month_bookings
        })
    
    monthly_bookings.reverse()  # Show chronological order
    
    # Get favorite venues (most booked)
    favorite_venues = bookings.values(
        'venue__name', 'venue__id'
    ).annotate(
        booking_count=Count('id')
    ).order_by('-booking_count')[:3]
    
    context = {
        'total_bookings': total_bookings,
        'total_spent': total_spent,
        'upcoming_bookings': upcoming_bookings,
        'recent_bookings': recent_bookings,
        'past_bookings_count': past_bookings_count,
        'upcoming_bookings_count': upcoming_bookings_count,
        'monthly_bookings': monthly_bookings,
        'favorite_venues': favorite_venues,
    }
    
    return render(request, 'dashboard/dashboard.html', context)

@login_required
def booking_history(request):
    user = request.user
    bookings = Booking.objects.filter(user=user).order_by('-created_at')
    
    # Filter by status if needed
    status_filter = request.GET.get('status')
    if status_filter == 'upcoming':
        today = timezone.now().date()
        bookings = bookings.filter(event_date__gte=today)
    elif status_filter == 'past':
        today = timezone.now().date()
        bookings = bookings.filter(event_date__lt=today)
    
    context = {
        'bookings': bookings,
        'status_filter': status_filter,
    }
    
    return render(request, 'dashboard/booking_history.html', context)

@login_required
def booking_detail(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id, user=request.user)
    except Booking.DoesNotExist:
        return render(request, '404.html')
    
    # Calculate booking status
    today = timezone.now().date()
    if booking.event_date < today:
        status = 'completed'
        status_class = 'success'
    elif booking.event_date == today:
        status = 'today'
        status_class = 'warning'
    else:
        status = 'upcoming'
        status_class = 'primary'
    
    context = {
        'booking': booking,
        'status': status,
        'status_class': status_class,
    }
    
    return render(request, 'dashboard/booking_detail.html', context)