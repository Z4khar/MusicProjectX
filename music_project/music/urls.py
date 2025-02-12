from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TrackViewSet, PlaylistViewSet, FavoriteTrackViewSet

router = DefaultRouter()  # Создаем маршрутизатор
router.register(r'tracks', TrackViewSet)  # Добавляем маршрут для треков
router.register(r'playlists', PlaylistViewSet)  # Добавляем маршрут для плейлистов
router.register(r'favorite-tracks', FavoriteTrackViewSet) 
urlpatterns = [
    path('', include(router.urls)),  # Включаем маршруты в urlpatterns
]