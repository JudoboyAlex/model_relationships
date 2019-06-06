from django.db import models

class Gallery(models.Model):
    name = models.CharField(max_length=255)
    
class Exhibit(models.Model):
    name = models.CharField(max_length=255)
    

class Curator(models.Model):
    name = models.CharField(max_length=255)
    gallery = models.ManyToManyField(Gallery, related_name='curators')