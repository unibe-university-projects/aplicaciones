from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Menu
#
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
            menus = Menu.objects.all()
            print(menus)
            print('entra qqqqqqqqq')
            return render(request, 'list-menu.html', {'menus': menus})
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    



def get_gastos(request):
    try:
        menu = Menu.objects.all()
        data = serialize_gastos(menu)
        return JsonResponse({'menu': data}, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def serialize_gastos(menus):
    """
    Serializa los objetos Gasto en una lista de diccionarios.
    """
    data = []
    for nemu in menus:
        reserva_data = {
            'id': nemu.id,
            'tipo_menu': menus.tipo_menu,
            'producto': menus.producto,
        }
        data.append(reserva_data)
    return data
