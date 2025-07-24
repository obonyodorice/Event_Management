from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('venue', 'user', 'event_date', 'start_time', 'duration', 'guests', 'total_price')
    list_filter = ('event_date', 'created_at')
    search_fields = ('venue__name', 'user__username')