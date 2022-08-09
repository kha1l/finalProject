from django.urls import path, include
from .viewsets import SongViewSet, SongYourViewSet, GenreViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'songs', SongViewSet, basename='songs')
router.register(r'my_songs', SongYourViewSet, basename='my_songs')
router.register(r'genre', GenreViewSet, basename='genre')

urlpatterns = [
    path('', include(router.urls))
]
