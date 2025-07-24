from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Booking
from venue.models import Venue  # Adjust import as needed


def create_booking(request, venue_id):
    venue = get_object_or_404(Venue, id=venue_id)
    
    if request.method == 'POST':
        try:
            duration = int(request.POST.get('duration'))
            total_price = venue.price_per_hour * duration
            
            booking = Booking.objects.create(
                user=request.user,
                venue=venue,
                event_date=request.POST.get('event_date'),
                start_time=request.POST.get('start_time'),
                duration=duration,
                guests=int(request.POST.get('guests')),
                total_price=total_price
            )
            
            messages.success(request, 'Booking created successfully!')
            return redirect('bookings:booking_success', booking_id=booking.id)
            
        except Exception as e:
            messages.error(request, 'Error creating booking. Please try again.')
    
    return redirect('venue:venue_detail', venue_id=venue_id)

def booking_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'bookings/success.html', {'booking': booking})