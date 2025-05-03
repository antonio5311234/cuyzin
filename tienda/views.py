from django.shortcuts import render, redirect
from .forms import Ejercicio1Form
from .forms import Ejercicio2Form

from django.http import JsonResponse


def health_check_view(request):
    return JsonResponse({"status": "ok"})

def inicio(request):
    return render(request, 'paginas/inicio.html')

def ejercicio1(request):
    mensaje = ''
    if request.method == 'POST':
        form = Ejercicio1Form(request.POST)
        if form.is_valid():
            form.save()
            mensaje = '¡Formulario enviado correctamente!'
            

              # Puedes redirigir a una página de confirmación si prefieres
    else:
        form = Ejercicio1Form()
    
    return render(request, 'paginas/ejercicio1.html', {
        'form': form,
        'mensaje': mensaje,
    })

def ejercicio2(request):
    mensaje = ''
    if request.method == 'POST':
        form = Ejercicio2Form(request.POST)
        if form.is_valid():
            form.save()
            mensaje = '¡Formulario enviado correctamente!'  # Puedes redirigir a una página de confirmación si prefieres
    else:
        form = Ejercicio2Form()
    
    return render(request, 'paginas/ejercicio2.html', {
        'form': form,
        'mensaje': mensaje,
    })

