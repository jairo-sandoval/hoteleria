from django.shortcuts import render
from habitaciones.models import Habitacion
from reservas.models import Reserva

def mostrar_habitaciones(request):
    no_habitaciones = Habitacion.objects.count()
    habitaciones = Habitacion.objects.all()
    reservas = Reserva.objects.all()
    no_reservas = Reserva.objects.count()


    info_habitaciones = {
        'no_habitaciones' : no_habitaciones,
        'habitaciones': habitaciones,
        'reservas': reservas,
        'no_reservas': no_reservas,
    }
    return render(request, 'habitaciones.html', info_habitaciones )
