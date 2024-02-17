from django.urls import path
from . import views

urlpatterns = [
    path('list-reservas/', views.list, name='list_reservas'),
    path('crear/', views.create_reservas, name='crear_reservas'),
    path('editar/<int:reserva_id>/', views.editar_reserva, name='editar_reserva'),
]