from django.contrib import admin

from .models import Ejercicio1, Ejercicio2

@admin.register(Ejercicio1)
class Ejercicio1Admin(admin.ModelAdmin):
    list_display = ['nombre', 'Lieu', 'Cuisine', 'Spécialité', 'Prix_des_plats_principaux', 'Vue', 'Réservations']
    search_fields = ['Lieu', 'Cuisine', 'Spécialité']

@admin.register(Ejercicio2)
class Ejercicio2Admin(admin.ModelAdmin):
    list_display = ['nombre', 'Lieu', 'Cuisine', 'Spécialité', 'Prix_des_plats_principaux', 'Vue', 'Réservations']
    search_fields = ['Lieu', 'Cuisine', 'Spécialité']
