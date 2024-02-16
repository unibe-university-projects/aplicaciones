from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Gasto
from .forms import GastoForm
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize

def list(request):
    gastos = Gasto.objects.all()

    # Serializar los objetos Gasto a JSON si la solicitud es para la API
    if 'application/json' in request.headers.get('accept', ''):
        data = serialize('json', gastos)
        return JsonResponse(data, safe=False)

    # Renderizar la plantilla HTML si la solicitud es para HTML
    else:
        return render(request, 'list.html', {'gastos': gastos})

@csrf_exempt
def crear_gasto(request):
    if request.method == 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            gasto = form.save()
            # For HTML response:
            return redirect('list')
            # For API response (replace with your desired data):
            return JsonResponse({'success': True, 'data': serialize('json', [gasto])}, safe=False)
    else:
        form = GastoForm()
    return render(request, 'create.html', {'form': form})
