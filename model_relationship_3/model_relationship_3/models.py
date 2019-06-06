from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)

class Food_Critic(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant')

class Review(models.Model):
    name =  models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant')
    food_critic = models.ForeignKey(Food_Critic, on_delete=models.CASCADE, related_name='food_critic')

class Chef(models.Model):
    name = models.CharField(max_length=255)

