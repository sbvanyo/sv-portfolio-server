from rest_framework import serializers
from app_portfolio.models import Artwork

class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = [
          "id",
          "title",
          "description",
          "medium",
          "date_created",
          "collection",
          "image",
          "created_at",
        ]
