from django.contrib import admin
from .models import Artwork

# Register your models here.
@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    pass
