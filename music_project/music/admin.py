from django.contrib import admin

from .models import Genre, Track, Playlist, FavoriteTrack
admin.site.register(Genre)
admin.site.register(Track)
admin.site.register(Playlist)
admin.site.register(FavoriteTrack)
