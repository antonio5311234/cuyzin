from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import Ejercicio1Form, Ejercicio2Form
from .models import Ejercicio1, Ejercicio1Historial, Ejercicio1Comentario, Ejercicio1Nota

def inicio(request):
    return render(request, 'paginas/inicio.html')

@login_required
def ejercicio1(request):
    usuario = request.user
    mensaje = ''
    errores = []

    # Checkbox "guardar_historial"
    guardar_historial = request.POST.get('guardar_historial') == 'on' if request.method == 'POST' else False

    # Historial más reciente
    historial_existente = Ejercicio1Historial.objects.filter(usuario=usuario).order_by('-timestamp').first()

# NUEVO: reiniciar si checkbox no está marcado
    if request.method == 'POST' and not guardar_historial:
        historial_existente = None
        bloqueado = False
    else:
        bloqueado = historial_existente.enviado if historial_existente else False

    # Datos iniciales si hay historial
    datos_formulario = {
        campo: getattr(historial_existente.ejercicio, campo, '') if historial_existente else ''
        for campo in ['Lieu', 'Cuisine', 'Spécialité', 'Prix_des_plats_principaux', 'Vue', 'Réservations']
    }

    if request.method == 'POST':
        form = Ejercicio1Form(
            request.POST,
            user=usuario,
            guardar_historial=guardar_historial or bloqueado,
            bloqueado=bloqueado
        )

        if guardar_historial:
            if form.is_valid():
                instance = form.save()
                enviado = True
            else:
                # ⚠️ Creamos el modelo manualmente incluso con errores
                campos = ['Lieu', 'Cuisine', 'Spécialité', 'Prix_des_plats_principaux', 'Vue', 'Réservations', 'comentario', 'nota']
                datos = {campo: request.POST.get(campo, '') for campo in campos}
                instance = Ejercicio1.objects.create(**datos)
                enviado = False

            # Guardar en historial
            Ejercicio1Historial.objects.create(
                ejercicio=instance,
                usuario=usuario,
                enviado=enviado,
                datos={campo: getattr(instance, campo, '') for campo in datos_formulario}
            )

            # Validación simple para feedback
            respuestas_correctas = {
                'Lieu': 'rolle',
                'Cuisine': 'chinoise',
                'Spécialité': 'cuisine de pékin',
                'Prix_des_plats_principaux': 'entre 12 chf et 21 chf',
                'Vue': 'sur le lac léman',
                'Réservations': 'info@restaurantming.ch',
            }
            errores = [
                f'❌ {campo} incorrecto. 😞'
                for campo, correcto in respuestas_correctas.items()
                if getattr(instance, campo, '').strip().lower() != correcto
            ]

            mensaje = '✅ ¡Formulario guardado! Puede contener errores.' if errores else '✅ ¡Formulario guardado correctamente! 🎉'
            bloqueado = enviado

            form = Ejercicio1Form(
                initial={**{field: getattr(instance, field, '') for field in datos_formulario}, 'guardar_historial': True},
                user=usuario,
                guardar_historial=True,
                bloqueado=bloqueado
            )
        else:
            mensaje = '⚠️ Debe marcar "Guardar en historial" para enviar el formulario.'
            errores = []
            form = Ejercicio1Form(
                request.POST,
                user=usuario,
                guardar_historial=False,
                bloqueado=False
            )

    else:
        form = Ejercicio1Form(
            initial={**datos_formulario, 'guardar_historial': False},
            user=usuario,
            guardar_historial=False,
            bloqueado=bloqueado
        )

    historial = Ejercicio1Historial.objects.filter(usuario=usuario).order_by('-timestamp')

    return render(request, 'plantilla/Ejercicio1.html', {
        'form': form,
        'mensaje': mensaje,
        'errores': errores,
        'historial': historial,
        'bloqueado': bloqueado,
        'guardar_historial': guardar_historial
    })

@login_required
def ejercicio2(request):
    mensaje = ''
    errores = []

    if request.method == 'POST':
        form = Ejercicio2Form(request.POST, user=request.user)
        if form.is_valid():
            instance = form.save()

            respuestas_correctas = {
                'Lieu': 'môtier',
                'Cuisine': 'espagnole',
                'Spécialité': 'les tapas',
                'Prix_des_plats_principaux': 'dès 22 chf',
                'Vue': 'sur le lac de morat',
                'Réservations': 'appelez le 021 462 89 98',
            }

            errores = [
                f'❌ {campo} incorrect. 😞'
                for campo, respuesta_correcta in respuestas_correctas.items()
                if getattr(instance, campo, '').strip().lower() != respuesta_correcta
            ]

            mensaje = '✅ ¡Formulario completado correctamente! 🎉' if not errores else '⚠️ Formulario enviado, pero contiene errores.'
            form = Ejercicio2Form(user=request.user)
        else:
            mensaje = '❌ Formulario no válido.'
            errores = [error for field_errors in form.errors.values() for error in field_errors]
    else:
        form = Ejercicio2Form(user=request.user)

    return render(request, 'plantilla/Ejercicio2.html', {'form': form, 'mensaje': mensaje, 'errores': errores})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Usuario registrado exitosamente!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'usuario/registro.html', {'form': form})
