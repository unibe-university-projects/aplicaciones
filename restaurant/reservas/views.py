from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Reserva
from .forms import ReservaForm
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
import json
from django.contrib.auth.models import User
from django.http import Http404
# Create your views here.


def list(request):
    if request.method == 'GET':
        if request.headers.get('accept', '') == 'application/json':
            return get_gastos(request)
        else:
            reservas = Reserva.objects.all()
            print(reservas)
            print('entra qqqqqqqqq')
            return render(request, 'list-reservas.html', {'reservas': reservas})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    



def get_gastos(request):
    try:
        reserva = Reserva.objects.all()
        data = serialize_gastos(reserva)
        return JsonResponse({'reserva': data}, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def serialize_gastos(reservas):
    """
    Serializa los objetos Gasto en una lista de diccionarios.
    """
    data = []
    for reserva in reservas:
        reserva_data = {
            'id': reserva.id,
            'ingreso': reserva.ingreso.strftime('%Y-%m-%d'),
            'salida': reserva.salida.strftime('%Y-%m-%d'),
            'confirmacion': reserva.confirmacion,
            'caducidad': reserva.caducidad,
            'estado': reserva.estado
        }
        data.append(reserva_data)
    return data



@csrf_exempt
def create_reservas(request):
    if request.method == 'POST':
        if request.headers.get('accept', '') == 'application/json':
            return crear_api(request)
        else:
            return crear_form(request)
    else:
        users = User.objects.all()
        return render(request, 'form-reservas.html', {'users': users})


def user(request):
    users = User.objects.all()
    print('holaaaaaaaa')
    return render(request, 'form-reservas.html', {'users': users})


@csrf_exempt
def crear_form(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            print('entra' )
            return redirect('/reservas/list-reservas/')
        else:
            print(form )
            return render(request, 'form-reservas.html', {'form': form, 'error_message': 'El formulario no es válido. Verifica los campos.'})
    else:
        form = ReservaForm()
        return render(request, 'form-reservas.html', {'form': form})
    


@csrf_exempt
def crear_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            form = ReservaForm(data)
            if form.is_valid():
                form.save()
                return JsonResponse({'mensaje': 'Reserva creado correctamente'})
            else:
                return JsonResponse({'error': 'El formulario no es válido. Verifica los campos.'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Error al decodificar la solicitud JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    




@csrf_exempt
def editar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    if request.method == 'POST':
        if request.headers.get('accept', '') == 'application/json':
            return editar_api(request, reserva)
        else:
            return editar_form(request, reserva)
    else:
        return render(request, 'editar-reserva.html', {'reserva': reserva})


def editar_form(request, reserva):
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('/reservas/list-reservas/')
        else:
            return render(request, 'editar-reserva.html', {'form': form, 'error_message': 'El formulario no es válido. Verifica los campos.'})
    else:
        form = ReservaForm(instance=reserva)
        return render(request, 'editar-reserva.html', {'form': form})


@csrf_exempt
def editar_api(request, reserva):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body.decode('utf-8'))
            form = ReservaForm(data, instance=reserva)
            if form.is_valid():
                form.save()
                return JsonResponse({'mensaje': 'Reserva actualizada correctamente'})
            else:
                return JsonResponse({'error': 'El formulario no es válido. Verifica los campos.'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Error al decodificar la solicitud JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)


def get_object_or_404(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        raise Http404("El objeto no existe")