from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Gasto
from .forms import GastoForm
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
import json


def list(request):
    if request.method == 'GET':
        if request.headers.get('accept', '') == 'application/json':
            return get_gastos(request)
        else:
            gastos = Gasto.objects.all()
            return render(request, 'list.html', {'gastos': gastos})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    
def get_gastos(request):
    try:
        gastos = Gasto.objects.all()
        data = serialize_gastos(gastos)
        return JsonResponse({'gastos': data}, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def serialize_gastos(gastos):
    """
    Serializa los objetos Gasto en una lista de diccionarios.
    """
    data = []
    for gasto in gastos:
        gasto_data = {
            'id': gasto.id,
            'descripcion': gasto.descripcion,
            'monto': str(gasto.monto),
            'fecha': gasto.fecha.strftime('%Y-%m-%d'),
            'categoria': gasto.categoria
        }
        data.append(gasto_data)
    return data


@csrf_exempt
def crear(request):
    if request.headers.get('accept', '') == 'application/json':
        return crear_api(request)
    else:
        return crear_form(request)
    


@csrf_exempt
def crear_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            form = GastoForm(data)
            if form.is_valid():
                form.save()
                return JsonResponse({'mensaje': 'Gasto creado correctamente'})
            else:
                return JsonResponse({'error': 'El formulario no es válido. Verifica los campos.'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Error al decodificar la solicitud JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)


@csrf_exempt
def crear_form(request):
    if request.method == 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/gestion-gastos/list-gastos/')
        else:
            return render(request, 'crear.html', {'form': form, 'error_message': 'El formulario no es válido. Verifica los campos.'})
    else:
        form = GastoForm()
        return render(request, 'crear.html', {'form': form})
