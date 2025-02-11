from rest_framework import viewsets
from .models import Track, Playlist
from .serializers import TrackSerializer, PlaylistSerializer

class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()  # Получаем все треки из базы данных
    serializer_class = TrackSerializer  # Указываем, какой сериализатор использовать

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()  # Получаем все плейлисты из базы данных
    serializer_class = PlaylistSerializer  # Указываем сериализатор для плейлистов