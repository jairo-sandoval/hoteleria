from django.contrib import admin
from django.urls import path
from reservas.views import obtener_info_reserva, obtener_datos_personales, obtener_datos_bancarios
from habitaciones.views import mostrar_habitaciones
from inicio.views import welcome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome),
    path('habitaciones/', mostrar_habitaciones, name='reserva'),
    path('habitaciones/reservar/<int:id>', obtener_info_reserva, name='habitaciones'),
    path('habitaciones/reservar/datos_personales', obtener_datos_personales, name='datos_personales'),
    path('habitaciones/reservar/metodo_pago', obtener_datos_bancarios, name='datos_bancarios'),
] 
