from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=255)
    
class Comic(models.Model):
    name = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='comics')

class Writer(models.Model):
    name =  models.CharField(max_length=255)

class Issue(models.Model):
    number = models.IntegerField()
    writers = models.ManyToManyField(Writer, related_name='issues')
    artists = models.ManyToManyField(Artist, related_name='issues')
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE, related_name='issues')
