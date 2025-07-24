from django.contrib import admin
from .models import Venue, VenueAdditionalImages

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ['name', 'capacity', 'location', 'price_per_hour', 'is_available']
    list_filter = ['is_available', 'capacity']
    search_fields = ['name', 'location']

@admin.register(VenueAdditionalImages)
class VenueAdditionalImagesAdmin(admin.ModelAdmin):
    list_display = ('venue', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('venue__name',)
    fields = ('venue', 'image1', 'image2', 'image3')    