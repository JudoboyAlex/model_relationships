from django.db import models

class Song(models.Model):
    name = models.CharField(max_length=255)
    
class Instrument(models.Model):
    name = models.CharField(max_length=255)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='instruments')

class Setlist(models.Model):
    name = models.CharField(max_length=255)
    songs = models.ManyToManyField(Song, related_name='setlists')
  