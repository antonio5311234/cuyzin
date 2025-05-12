from django import forms
from .models import Ejercicio1, Ejercicio2

class Ejercicio1Form(forms.ModelForm):
    class Meta:
        model = Ejercicio1
        fields = ['Lieu', 'Cuisine', 'Spécialité', 'Prix_des_plats_principaux', 'Vue', 'Réservations']
        widgets = {
            'Lieu': forms.TextInput(attrs={'class': 'form-control'}),
            'Cuisine': forms.TextInput(attrs={'class': 'form-control'}),
            'Spécialité': forms.TextInput(attrs={'class': 'form-control'}),
            'Prix_des_plats_principaux': forms.TextInput(attrs={'class': 'form-control'}),
            'Vue': forms.TextInput(attrs={'class': 'form-control'}),
            'Réservations': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class Ejercicio2Form(forms.ModelForm):
    class Meta:
        model = Ejercicio2
        fields = ['Lieu', 'Cuisine', 'Spécialité', 'Prix_des_plats_principaux', 'Vue', 'Réservations']
        widgets = {
            'Lieu': forms.TextInput(attrs={'class': 'form-control'}),
            'Cuisine': forms.TextInput(attrs={'class': 'form-control'}),
            'Spécialité': forms.TextInput(attrs={'class': 'form-control'}),
            'Prix_des_plats_principaux': forms.TextInput(attrs={'class': 'form-control'}),
            'Vue': forms.TextInput(attrs={'class': 'form-control'}),
            'Réservations': forms.TextInput(attrs={'class': 'form-control'}),
        }
