from django.contrib import admin

from .models import Genre, Track, Playlist
admin.site.register(Genre)
admin.site.register(Track)
admin.site.register(Playlist)
