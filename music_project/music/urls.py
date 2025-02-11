from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TrackViewSet, PlaylistViewSet

router = DefaultRouter()  # Создаем маршрутизатор
router.register(r'tracks', TrackViewSet)  # Добавляем маршрут для треков
router.register(r'playlists', PlaylistViewSet)  # Добавляем маршрут для плейлистов

urlpatterns = [
    path('', include(router.urls)),  # Включаем маршруты в urlpatterns
]