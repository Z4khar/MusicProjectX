from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Track, Playlist, FavoriteTrack
from .serializers import TrackSerializer, PlaylistSerializer, FavoriteTrackSerializer


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()  # Получаем все треки из базы данных
    serializer_class = TrackSerializer  # Указываем, какой сериализатор использовать

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()  # Получаем все плейлисты из базы данных
    serializer_class = PlaylistSerializer  # Указываем сериализатор для плейлистов

class FavoriteTrackViewSet(viewsets.ModelViewSet):  # Новый класс для работы с избранными треками
    queryset = FavoriteTrack.objects.all()  # Получаем все избранные треки из базы данных
    serializer_class = FavoriteTrackSerializer  # Указываем сериализатор для избранных треков 