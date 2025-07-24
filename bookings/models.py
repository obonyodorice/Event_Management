from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    venue = models.ForeignKey('venue.Venue', on_delete=models.CASCADE)  # Adjust app name as needed
    event_date = models.DateField()
    start_time = models.TimeField()
    duration = models.IntegerField()  # hours
    guests = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.venue.name} - {self.event_date}"