from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('ejercicio1/', views.ejercicio1, name='ejercicio1'),
    path('ejercicio2/', views.ejercicio2, name='ejercicio2'),
    
]
