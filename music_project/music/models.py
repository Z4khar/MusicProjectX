from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model): 
    name = models.CharField(max_length=100)


class Track(models.Model): 
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='tracks/')
    cover_image = models.ImageField(upload_to='covers/')


class Playlist(models.Model): 
    user = models.ForeignKey(User,on_delete=models.CASCADE )
    name = models.CharField(max_length=200)
    track = models.ManyToManyField(Track)