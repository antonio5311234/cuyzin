from django.db import models

class Ejercicio1(models.Model):
    nombre = models.CharField(max_length=100, default="Restaurant Ming")
    Lieu = models.CharField(max_length=100)
    Cuisine = models.CharField(max_length=100)
    Spécialité = models.CharField(max_length=100)
    Prix_des_plats_principaux = models.CharField(max_length=50)
    Vue = models.CharField(max_length=100)
    Réservations = models.CharField()

    def __str__(self):
        return self.nombre
    
class Ejercicio2(models.Model):
    nombre = models.CharField(max_length=100, default="Restaurant Ming")
    Lieu = models.CharField(max_length=100)
    Cuisine = models.CharField(max_length=100)
    Spécialité = models.CharField(max_length=100)
    Prix_des_plats_principaux = models.CharField(max_length=50)
    Vue = models.CharField(max_length=100)
    Réservations = models.CharField()

    def __str__(self):
        return self.nombre