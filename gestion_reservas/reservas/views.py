from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from habitaciones.models import Habitacion
from reservas.models import Reserva, Pago, Facturacion

ReservaForm = modelform_factory(Reserva, exclude=[])
FacturaForm = modelform_factory(Facturacion, exclude=[])
PagoForm = modelform_factory(Pago, exclude=[])

def obtener_info_reserva(request, id):
    habitacion = get_object_or_404(Habitacion, pk=id)
    no_facturas = Facturacion.objects.count()
    no_pago = Pago.objects.count()


    if no_facturas == 0 and no_pago == 0:
        return redirect('datos_personales')

    if request.method == "POST":
        form_info_user = ReservaForm(request.POST)
        if form_info_user.is_valid():
            form_info_user.save()
            return redirect('reserva')
    else:
        form_reserva = ReservaForm()
        

    datos_usuario = {
        'habitacion': habitacion, 
        'form_reserva' : form_reserva,
    }
    return render(request, 'reserva.html', datos_usuario)

def obtener_datos_personales(request):
    factura = FacturaForm()

    if request.method == "POST":
        form_info_user_factura = FacturaForm(request.POST)
        if form_info_user_factura.is_valid():
            form_info_user_factura.save()
            return redirect('datos_bancarios')
    else:
        form_factura = FacturaForm() 

    return render(request, 'datos_personales.html', {'factura': factura})

def obtener_datos_bancarios(request):
    pago = PagoForm()

    if request.method == "POST":
        form_info_user_Pago = PagoForm(request.POST)
        if form_info_user_Pago.is_valid():
            form_info_user_Pago.save()
            return redirect('habitaciones')
    else:
        form_pago = PagoForm()

    return render(request, 'metodo_pago.html', {'pago': pago})