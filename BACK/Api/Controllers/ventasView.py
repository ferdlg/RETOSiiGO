from models import Ventas, Sucursales, DetalleVentas
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from serializers import VentasSerializer
from django.views import View
import json

class VentaView(View):

    def verVenta(self, request):
        venta = Ventas.objects.all()
        serializer = VentasSerializer(venta, many = True)
        if len(venta)>0:
            datos = {'message':'succes', 'facturas': serializer.data}
        else:
            datos= {'message':'Facturas no encontradas'}
        return datos
    
    def crearVenta(self, request):
        json_data = json.loads(request.body)
        #obtener el valor del campo en json        
        id_sucursal = json_data['id_sucursal_fk']
        #obtener la instancia del campo
        sucursal = Sucursales.objects.get(id_sucursal = id_sucursal)
        Ventas.objects.create(
            id_sucursal_fk = sucursal
        )
        datos = {'message':'Venta registrada'}
        return JsonResponse(datos)
    
    
    