from django.db import models
from django.contrib.auth.models import User

class Ejercicio1(models.Model):
    nombre = models.CharField(max_length=100, default="Restaurant Ming")
    Lieu = models.CharField(max_length=100)
    Cuisine = models.CharField(max_length=100)
    Spécialité = models.CharField(max_length=100)
    Prix_des_plats_principaux = models.CharField(max_length=50)
    Vue = models.CharField(max_length=100)
    Réservations = models.CharField(max_length=100)


    def __str__(self):
        return self.nombre
    
class Ejercicio2(models.Model):
    nombre = models.CharField(max_length=100, default="Restaurant Ming")
    Lieu = models.CharField(max_length=100)
    Cuisine = models.CharField(max_length=100)
    Spécialité = models.CharField(max_length=100)
    Prix_des_plats_principaux = models.CharField(max_length=50)
    Vue = models.CharField(max_length=100)
    Réservations = models.CharField(max_length=100)


    def __str__(self):
        return self.nombre
    

class Ejercicio1Historial(models.Model):
    ejercicio = models.ForeignKey(Ejercicio1, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    enviado = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.timestamp}"


class Ejercicio1Comentario(models.Model):
    historial = models.ForeignKey(Ejercicio1Historial, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()

    def __str__(self):
        return f"Comentario de {self.autor.username} sobre {self.historial}"


class Ejercicio1Nota(models.Model):
    historial = models.ForeignKey(Ejercicio1Historial, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    nota = models.TextField()

    def __str__(self):
        return f"Nota de {self.autor.username} sobre {self.historial}"
