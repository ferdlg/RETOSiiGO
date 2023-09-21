from ..models import Ventas, Sucursales, Ventas, Personas
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from .serializers import VentasSerializer
from django.views import View
import json

class VentaView(View):

    def get(self, request):
        venta = Ventas.objects.all()
        serializer = VentasSerializer(venta, many = True)
        if len(venta)>0:
            datos = {'message':'succes', 'facturas': serializer.data}
        else:
            datos= {'message':'Facturas no encontradas'}
        return JsonResponse(datos)
    
    def post(self, request):
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
    
    def put(request, id):
            venta = Ventas.objects.get(id_detalleVenta = id)
            json_data = json.loads(request.body)
            try:
                if 'id_persona_fk' in json_data:
                    id_persona = json_data['id_persona_fk']
                    persona = Personas.objects.get(id_persona=id_persona)
                    venta.id_persona_fk= persona
                
                if 'fecha_venta' in json_data:
                    venta.fecha_venta=json_data['fecha_venta']
                    
                if 'encola_estado' in json_data:
                    venta.encola_estado=json_data['encola_estado']
                
                venta.save()
                datos = {'message':' Venta actualizada con exito'}

            except json.JSONDecodeError:
                datos={'message':'El formato JSON es incorrecto'}
                return JsonResponse(datos, status = 400)
            
            except venta.DoesNotExist:
                datos = {'error':'La venta seleccionada no existe'}
                return JsonResponse(datos, status = 400)
            return JsonResponse(datos)
    