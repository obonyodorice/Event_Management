from django.db import models
from django.urls import reverse

class Venue(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    capacity = models.IntegerField()
    location = models.CharField(max_length=300)
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='venues/', blank=True, null=True)
    amenities = models.TextField(help_text="List amenities separated by commas")
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('venue:detail', kwargs={'pk': self.pk})

    def get_amenities_list(self):
        return [amenity.strip() for amenity in self.amenities.split(',') if amenity.strip()]
    
class VenueAdditionalImages(models.Model):
    venue = models.OneToOneField(Venue, on_delete=models.CASCADE, related_name='additional_images')
    image1 = models.ImageField(upload_to='venue_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='venue_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='venue_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Venue Additional Images"
        verbose_name_plural = "Venue Additional Images"
    
    def __str__(self):
        return f"{self.venue.name} - Additional Images"    