
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='paginas/inicio.html'), name='inicio'),
    path('ejercicio1/', TemplateView.as_view(template_name='plantilla/ejercicio1.html'), name='ejercicio1'),
    path('ejercicio2/', TemplateView.as_view(template_name='plantilla/ejercicio2.html'), name='ejercicio2'),
]