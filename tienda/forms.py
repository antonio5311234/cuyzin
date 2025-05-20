from django import forms
from .models import Ejercicio1, Ejercicio2
from .widgets import CustomUserWidget  




class Ejercicio1Form(forms.ModelForm):
    guardar_historial = forms.BooleanField(
        required=False,
        label='Guardar en historial',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'guardar_historial'})
    )

    class Meta:
        model = Ejercicio1
        fields = ['Lieu', 'Cuisine', 'Spécialité', 'Prix_des_plats_principaux', 'Vue', 'Réservations', 'comentario', 'nota']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        guardar_historial = kwargs.pop('guardar_historial', False)
        bloqueado = kwargs.pop('bloqueado', False)
        super().__init__(*args, **kwargs)

        if guardar_historial:
            self.initial['guardar_historial'] = True

        if user:
            for field in self.Meta.fields:
                self.fields[field].widget = CustomUserWidget(
                    user=user,
                    guardar_historial=guardar_historial,  # Se pasa correctamente a cada campo
                    attrs={'class': 'form-control', 'disabled': 'disabled'} if bloqueado else {'class': 'form-control'}
                )


class Ejercicio2Form(forms.ModelForm):
    guardar_historial = forms.BooleanField(
        required=False,
        label='Guardar en historial',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = Ejercicio2
        fields = ['Lieu', 'Cuisine', 'Spécialité', 'Prix_des_plats_principaux', 'Vue', 'Réservations', 'comentario', 'nota']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        guardar_historial = kwargs.pop('guardar_historial', False)
        super().__init__(*args, **kwargs)

        if user:
            for field in self.Meta.fields:
                self.fields[field].widget = CustomUserWidget(
                    user=user,
                    guardar_historial=guardar_historial,
                    attrs={'class': 'form-control'}
                )
