from django.db import models

# Create your models here.

class Artwork(models.Model):
    class ArtworkCollection(models.TextChoices):
        INKTOBER2019 = 'Inktober 2019'
        INKTOBER2020 = 'Inktober 2020'
        INKTOBER2022 = 'Inktober 2022'
        INKTOBER2023 = 'Inktober 2023'
        INKTOBER2024 = 'Inktober 2024'
        PORTRAITS = 'Portraits'
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500, blank=True)
    medium = models.CharField(max_length=100)
    date_created = models.DateField(blank=True)
    collection = models.CharField(choices=ArtworkCollection.choices, blank=True, max_length=100)
    image = models.ImageField(upload_to='artwork_images/')
    created_at = models.DateTimeField(auto_now_add=True)
