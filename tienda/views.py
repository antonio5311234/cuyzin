from django.shortcuts import render
from .forms import Ejercicio1Form, Ejercicio2Form
from django.http import JsonResponse

def health_check_view(request):
    return JsonResponse({"status": "ok"})

def inicio(request):
    return render(request, 'paginas/inicio.html')

def ejercicio1(request):
    mensaje = ''
    errores = []

    if request.method == 'POST':
        form = Ejercicio1Form(request.POST)
        if form.is_valid():
            instance = form.save()

            # Validaciones personalizadas, sin bloquear guardado
            respuestas = {
                'Lieu': 'rolle',
                'Cuisine': 'chinoise',
                'Spécialité': 'cuisine de pékin',
                'Prix_des_plats_principaux': 'entre 12 chf et 21 chf',
                'Vue': 'sur le lac léman',
                'Réservations': 'info@restaurantming.ch',
            }

            for campo, respuesta_correcta in respuestas.items():
                valor = getattr(instance, campo, '').strip().lower()
                if valor != respuesta_correcta:
                    errores.append(f'❌ {campo} incorrect. 😞')

            if not errores:
                mensaje = '✅ ¡Formulario completado correctamente! 🎉'
            else:
                mensaje = '⚠️ Formulario enviado, pero contiene errores.'

            form = Ejercicio1Form()
        else:
            mensaje = '❌ Formulario no válido (errores de formato).'
            errores = [error for field_errors in form.errors.values() for error in field_errors]
    else:
        form = Ejercicio1Form()

    return render(request, 'plantilla/Ejercicio1.html', {
        'form': form,
        'mensaje': mensaje,
        'errores': errores,
    })

def ejercicio2(request):
    mensaje = ''
    errores = []

    if request.method == 'POST':
        form = Ejercicio2Form(request.POST)
        if form.is_valid():
            instance = form.save()

            respuestas = {
                'Lieu': 'môtier',
                'Cuisine': 'espagnole',
                'Spécialité': 'les tapas',
                'Prix_des_plats_principaux': 'dès 22 chf',
                'Vue': 'sur le lac de morat',
                'Réservations': 'appelez le 021 462 89 98',
            }

            for campo, respuesta_correcta in respuestas.items():
                valor = getattr(instance, campo, '').strip().lower()
                if valor != respuesta_correcta:
                    errores.append(f'❌ {campo} incorrect. 😞')

            if not errores:
                mensaje = '✅ ¡Formulario completado correctamente! 🎉'
            else:
                mensaje = '⚠️ Formulario enviado, pero contiene errores.'

            form = Ejercicio2Form()
        else:
            mensaje = '❌ Formulario no válido (errores de formato).'
            errores = [error for field_errors in form.errors.values() for error in field_errors]
    else:
        form = Ejercicio2Form()

    return render(request, 'plantilla/Ejercicio2.html', {
        'form': form,
        'mensaje': mensaje,
        'errores': errores,
    })
