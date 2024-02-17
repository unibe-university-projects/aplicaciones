from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import PersonasForm
from .models import Persona
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
import json
# Create your views here.

@csrf_exempt
def create_person(request):
    if request.headers.get('accept', '') == 'application/json':
        return crear_api(request)
    else:
        return 'hola'



@csrf_exempt
def crear_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            form = PersonasForm(data)
            if form.is_valid():
                form.save()
                return JsonResponse({'mensaje': 'Persona creado correctamente'})
            else:
                return JsonResponse({'error': 'El formulario no es válido. Verifica los campos.'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Error al decodificar la solicitud JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
