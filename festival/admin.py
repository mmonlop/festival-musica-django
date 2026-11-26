from django.contrib import admin
from .models import Escenario,Concierto, Perfil, Reserva, Artista

# Register your models here.
admin.site.register(Escenario)
admin.site.register(Concierto)
admin.site.register(Perfil)
admin.site.register(Reserva)
admin.site.register(Artista)