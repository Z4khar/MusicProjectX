from rest_framework import serializers


from .models import Track, Playlist, FavoriteTrack  # Импортируем FavoriteTrack

class TrackSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Track 
        fields = '__all__'  # Используем все поля модели Track

class PlaylistSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Playlist 
        fields = '__all__'  # Используем все поля модели Playlist

class FavoriteTrackSerializer(serializers.ModelSerializer):  # Новый сериализатор для FavoriteTrack
    class Meta:
        model = FavoriteTrack  # Указываем модель FavoriteTrack
        fields = '__all__'  # Используем все поля модели FavoriteTrack


