from django.shortcuts import render
from .models import Artista,Concierto

# Create your views here.
def principal(request):
    return render(request, 'base.html')

def artistas_ordenados(request):
    artistas = Artista.objects.all().order_by('nombre')
    return render(request, 'artistasOrdenados.html', {'artistas': artistas})

def artistas_activos(request):
    artistas = Artista.objects.filter(activo=True)
    return render(request, 'artistasActivos.html',{'artistas':artistas})

def artistas_pais(request):
    artistas = Artista.objects.filter(pais='España')
    return render(request, 'artistasPais.html',{'artistas':artistas})


def concietos_precio(request):
    conciertos = Concierto.objects.filter(precio__gte=20,precio__lte=50)
    return render(request, 'conciertosPrecio.html',{'conciertos':conciertos})

def concietos_gratis(request):
    conciertos = Concierto.objects.filter(precio__lte=0)
    return render(request, 'conciertosPrecio.html',{'conciertos':conciertos})