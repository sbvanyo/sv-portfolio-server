from rest_framework import routers
from app_portfolio.views import ArtworkViewSet

artworks_router = routers.DefaultRouter()
artworks_router.register("artworks", viewset=ArtworkViewSet, basename="artworks")
