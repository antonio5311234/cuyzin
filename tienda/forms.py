from django import forms
from .models import Ejercicio1, Ejercicio2
from .widgets import CustomUserWidget  # Asegúrate de haber creado widgets.py

class Ejercicio1Form(forms.ModelForm):
    enviar_checkbox = forms.BooleanField(
        required=False,
        label='Guardar en historial',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    comentario = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        label="Commentaires (seulement pour Marilyn)"
    )

    nota = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        label="Note (lecture seule sauf ce champ)"
    )

    class Meta:
        model = Ejercicio1
        fields = ['Lieu', 'Cuisine', 'Spécialité', 'Prix_des_plats_principaux', 'Vue', 'Réservations']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            for field in self.Meta.fields:
                self.fields[field].widget = CustomUserWidget(
                    user=user,
                    editable_for=['admin', 'profesor'],
                    readonly_for=['marilyn'],
                    hidden_for=['lector'],
                    attrs={'class': 'form-control'}
                )

            if user.username != 'marilyn':
                self.fields['comentario'].widget = forms.HiddenInput()
            if user.username != 'lector':
                self.fields['nota'].widget = forms.HiddenInput()

                
class Ejercicio2Form(forms.ModelForm):
    enviar_checkbox = forms.BooleanField(
        required=False,
        label='Guardar en historial',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    comentario = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        label="Commentaires (seulement pour Marilyn)"
    )

    nota = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        label="Note (lecture seule sauf ce champ)"
    )

    class Meta:
        model = Ejercicio2
        fields = ['Lieu', 'Cuisine', 'Spécialité', 'Prix_des_plats_principaux', 'Vue', 'Réservations']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            for field in self.Meta.fields:
                self.fields[field].widget = CustomUserWidget(
                    user=user,
                    editable_for=['admin', 'profesor'],
                    readonly_for=['marilyn'],
                    hidden_for=['lector'],
                    attrs={'class': 'form-control'}
                )

            if user.username != 'marilyn':
                self.fields['comentario'].widget = forms.HiddenInput()
            if user.username != 'lector':
                self.fields['nota'].widget = forms.HiddenInput()
