from django.urls import path
from . import views

urlpatterns = [
    path('list-gastos/', views.list, name='list_gastos'),
    path('crear/', views.crear, name='crear_gasto'),
   # path('editar/<int:id>/', views.editar_gasto, name='editar_gasto'),
    #path('eliminar/<int:id>/', views.eliminar_gasto, name='eliminar_gasto'),
]
