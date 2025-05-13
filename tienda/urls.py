from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('ejercicio1/', views.ejercicio1, name='ejercicio1'),
    path('ejercicio2/', views.ejercicio2, name='ejercicio2'),
    path('register/', views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='usuario/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    

]