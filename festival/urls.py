from django.urls import path
from . import views

urlpatterns = [
    path('',views.principal, name='principal'),
    path('artistasOrdenados',views.artistas_ordenados, name='artistasOrden'),
    path('artistasActivos',views.artistas_activos,name='activos'),
    path('artistasPais',views.artistas_pais,name='artistasPais'),
    path('conciertosPrecio',views.concietos_precio,name='conciertosPrecio'),
    path('conciertosGratis',views.concietos_gratis,name='conciertosGratis'),
]