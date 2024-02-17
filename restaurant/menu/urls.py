from django.urls import path
from . import views

urlpatterns = [
    path('list-menu/', views.list, name='list_menu'),
    #path('crear-menu/', views.create_reservas, name='crear_menu'),
]