from app_portfolio.serializers import ArtworkSerializer
from app_portfolio.models import Artwork
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class ArtworkViewSet(ModelViewSet):
    serializer_class = ArtworkSerializer
    queryset = Artwork.objects.all().order_by("created_at")
    pagination_class = PageNumberPagination
