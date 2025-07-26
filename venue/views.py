from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Venue

class VenueListView(ListView):
    model = Venue
    template_name = 'venue/venue_list.html'
    context_object_name = 'venues'
    paginate_by = 6

    def get_queryset(self):
        # return Venue.objects.filter(is_available=True).order_by('-created_at')
        return Venue.objects.all().order_by('-created_at')

def venue_detail(request, pk):
    venue = get_object_or_404(Venue, pk=pk)
    return render(request, 'venue/venue_detail.html', {'venue': venue})