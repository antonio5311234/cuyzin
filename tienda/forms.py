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
            'Réservations': forms.EmailInput(attrs={'placeholder': 'Entrez le contact pour les réservationss', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('Lieu') and cleaned_data.get('Lieu').lower() != 'rolle':
            self.add_error('Lieu', 'Lieu incorrect. Essayez encore.')
        if cleaned_data.get('Cuisine') and cleaned_data.get('Cuisine').lower() != 'chinoise':
            self.add_error('Cuisine', 'Cuisine incorrecte.')
        if cleaned_data.get('Spécialité') and cleaned_data.get('Spécialité').lower() != 'cuisine de pékin':
            self.add_error('Spécialité', 'Spécialité incorrecte.')
        if cleaned_data.get('Prix_des_plats_principaux') and cleaned_data.get('Prix_des_plats_principaux').lower() != 'entre 12 et 21':
            self.add_error('Prix_des_plats_principaux', 'Prix incorrect.')
        if cleaned_data.get('Vue') and cleaned_data.get('Vue').lower() != 'sur le lac léman':
            self.add_error('Vue', 'Vue incorrecte.')
        if cleaned_data.get('Réservations') and cleaned_data.get('Réservations').lower() != 'info@restaurantming.ch':
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

        if cleaned_data.get('Lieu') and cleaned_data.get('Lieu').lower() != 'môtier':
            self.add_error('Lieu', 'Lieu incorrect. Essayez encore.')
        if cleaned_data.get('Cuisine') and cleaned_data.get('Cuisine').lower() != 'espagnole':
            self.add_error('Cuisine', 'Cuisine incorrecte.')
        if cleaned_data.get('Spécialité') and cleaned_data.get('Spécialité').lower() != 'les tapas':
            self.add_error('Spécialité', 'Spécialité incorrecte.')
        if cleaned_data.get('Prix_des_plats_principaux') and cleaned_data.get('Prix_des_plats_principaux').lower() != 'dès 22':
            self.add_error('Prix_des_plats_principaux', 'Prix incorrect.')
        if cleaned_data.get('Vue') and cleaned_data.get('Vue').lower() != 'sur le lac de Morat':
            self.add_error('Vue', 'Vue incorrecte.')
        if cleaned_data.get('Réservations') and cleaned_data.get('Réservations').lower() != 'appelez le 021 462 89 98':
            self.add_error('Réservations', 'Réservations incorrectes.')

        return cleaned_data
