from django.db import models

class Veterinarian(models.Model):
    name = models.CharField(max_length=255)
    
class Animal_clinic(models.Model):
    name =  models.CharField(max_length=255)
    veterinarian = models.ForeignKey(Veterinarian, on_delete=models.CASCADE, related_name='vet')

class Pet_owner(models.Model):
    name = models.CharField(max_length=255)
    animal_clinic = models.ForeignKey(Animal_clinic, on_delete=models.CASCADE, related_name='animal_clinic')

class Pet(models.Model):
    name = models.CharField(max_length=255)
    pet_owner = models.ForeignKey(Pet_owner, on_delete=models.CASCADE, related_name='pet_owner')



