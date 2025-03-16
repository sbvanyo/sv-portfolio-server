from rest_framework import serializers
from app_portfolio.models import Artwork

class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = "id", "__all__"
