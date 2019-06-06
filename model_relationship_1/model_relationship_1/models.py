from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=255)

class Director(models.Model):
    name =  models.CharField(max_length=255)

class Play(models.Model):
    name = models.CharField(max_length=255)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='plays')

class Role(models.Model):
    name = models.CharField(max_length=255)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='roles')
    play = models.ForeignKey(Play, on_delete=models.CASCADE, related_name='roles')



