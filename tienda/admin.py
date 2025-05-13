from django.contrib import admin
from .models import (
    Ejercicio1, Ejercicio2,
    Ejercicio1Historial, Ejercicio1Comentario, Ejercicio1Nota
)

@admin.register(Ejercicio1)
class Ejercicio1Admin(admin.ModelAdmin):
    list_display = ['nombre', 'Lieu', 'Cuisine', 'Spécialité', 'Prix_des_plats_principaux', 'Vue', 'Réservations']
    search_fields = ['Lieu', 'Cuisine', 'Spécialité']

@admin.register(Ejercicio2)
class Ejercicio2Admin(admin.ModelAdmin):
    list_display = ['nombre', 'Lieu', 'Cuisine', 'Spécialité', 'Prix_des_plats_principaux', 'Vue', 'Réservations']
    search_fields = ['Lieu', 'Cuisine', 'Spécialité']

@admin.register(Ejercicio1Historial)
class Ejercicio1HistorialAdmin(admin.ModelAdmin):
    list_display = ['ejercicio', 'usuario', 'enviado', 'timestamp']
    search_fields = ['usuario__username', 'ejercicio__nombre']
    list_filter = ['enviado', 'timestamp']

@admin.register(Ejercicio1Comentario)
class Ejercicio1ComentarioAdmin(admin.ModelAdmin):
    list_display = ['historial', 'autor', 'comentario']
    search_fields = ['autor__username', 'comentario']

@admin.register(Ejercicio1Nota)
class Ejercicio1NotaAdmin(admin.ModelAdmin):
    list_display = ['historial', 'autor', 'nota']
    search_fields = ['autor__username', 'nota']

