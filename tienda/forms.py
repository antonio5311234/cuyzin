from django import forms
from .models import Ejercicio1, Ejercicio2

class Ejercicio1Form(forms.ModelForm):
    class Meta:
        model = Ejercicio1
        fields = ['Lieu', 'Cuisine', 'Spécialité', 'Prix_des_plats_principaux', 'Vue', 'Réservations']
        widgets = {
            'Lieu': forms.TextInput(attrs={'placeholder': 'Entrez le lieu', 'class': 'form-control'}),
            'Cuisine': forms.TextInput(attrs={'placeholder': 'Entrez le type de cuisine', 'class': 'form-control'}),
            'Spécialité': forms.TextInput(attrs={'placeholder': 'Entrez la spécialité', 'class': 'form-control'}),
            'Prix_des_plats_principaux': forms.TextInput(attrs={'placeholder': 'Entrez la gamme de prix', 'class': 'form-control'}),
            'Vue': forms.TextInput(attrs={'placeholder': 'Entrez la vue du restaurant', 'class': 'form-control'}),
            'Réservations': forms.EmailInput(attrs={'placeholder': 'Entrez le contact pour les réservations', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        # 🔧 CORRECCIÓN: Se agregó esta función para normalizar texto (quitar espacios y pasar a minúsculas)
        def normalize(val):
            return val.strip().lower() if val else ''

        # 🔧 CORRECCIÓN: Se usa normalize() en todas las comparaciones para evitar errores por mayúsculas o espacios
        if normalize(cleaned_data.get('Lieu')) != 'rolle':
            self.add_error('Lieu', 'Lieu incorrect. Essayez encore.')
        if normalize(cleaned_data.get('Cuisine')) != 'chinoise':
            self.add_error('Cuisine', 'Cuisine incorrecte.')
        if normalize(cleaned_data.get('Spécialité')) != 'cuisine de pékin':
            self.add_error('Spécialité', 'Spécialité incorrecte.')
        if normalize(cleaned_data.get('Prix_des_plats_principaux')) != 'entre 12 chf et 21 chf':
            self.add_error('Prix_des_plats_principaux', 'Prix incorrect.')
        if normalize(cleaned_data.get('Vue')) != 'sur le lac léman':
            self.add_error('Vue', 'Vue incorrecte.')
        if normalize(cleaned_data.get('Réservations')) != 'info@restaurantming.ch':
            self.add_error('Réservations', 'Réservations incorrectes.')

        return cleaned_data


class Ejercicio2Form(forms.ModelForm):
    class Meta:
        model = Ejercicio2
        fields = ['Lieu', 'Cuisine', 'Spécialité', 'Prix_des_plats_principaux', 'Vue', 'Réservations']
        widgets = {
            'Lieu': forms.TextInput(attrs={'placeholder': 'Entrez le lieu', 'class': 'form-control'}),
            'Cuisine': forms.TextInput(attrs={'placeholder': 'Entrez le type de cuisine', 'class': 'form-control'}),
            'Spécialité': forms.TextInput(attrs={'placeholder': 'Entrez la spécialité', 'class': 'form-control'}),
            'Prix_des_plats_principaux': forms.TextInput(attrs={'placeholder': 'Entrez la gamme de prix', 'class': 'form-control'}),
            'Vue': forms.TextInput(attrs={'placeholder': 'Entrez la vue du restaurant', 'class': 'form-control'}),
            'Réservations': forms.TextInput(attrs={'placeholder': 'Entrez le contact pour les réservations', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        # 🔧 CORRECCIÓN: misma función para normalizar texto
        def normalize(val):
            return val.strip().lower() if val else ''

        # 🔧 CORRECCIÓN: se usa normalize() para comparar de forma segura
        if normalize(cleaned_data.get('Lieu')) != 'môtier':
            self.add_error('Lieu', 'Lieu incorrect. Essayez encore.')
        if normalize(cleaned_data.get('Cuisine')) != 'espagnole':
            self.add_error('Cuisine', 'Cuisine incorrecte.')
        if normalize(cleaned_data.get('Spécialité')) != 'les tapas':
            self.add_error('Spécialité', 'Spécialité incorrecte.')
        if normalize(cleaned_data.get('Prix_des_plats_principaux')) != 'dès 22 chf':
            self.add_error('Prix_des_plats_principaux', 'Prix incorrect.')
        if normalize(cleaned_data.get('Vue')) != 'sur le lac de morat':
            self.add_error('Vue', 'Vue incorrecte.')
        if normalize(cleaned_data.get('Réservations')) != 'appelez le 021 462 89 98':
            self.add_error('Réservations', 'Réservations incorrectes.')

        return cleaned_data
