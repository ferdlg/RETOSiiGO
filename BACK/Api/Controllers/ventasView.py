from ..models import Ventas, Sucursales, Ventas, Personas
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .serializers import VentasSerializer
from django.views import View
import json

class VentaView(View):

    @method_decorator(csrf_exempt) 
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, id = None):
        if id is not None and id > 0:
                venta = Ventas.objects.filter(id_venta=id).first()
                if venta:
                    serializer = VentasSerializer(venta)
                    datos = {'message': 'success', 'Venta': serializer.data}
                else:
                    datos = {'message':'No hay ventas encontradas' }
                return JsonResponse(datos)
        else:
            venta = Ventas.objects.all()
            serializer = VentasSerializer(venta, many=True)
            if len(venta) > 0:
                datos = {'message': 'success', 'Ventas': serializer.data}
            else:
                datos = {'message': 'No hay ventas encontradas'}
        return JsonResponse(datos)
    
    def post(self, request):
        json_data = json.loads(request.body)#obtener el valor del campo en json 
        try:
            id_persona = json_data['id_persona_fk']#obtener la instancia del campo
            persona = Personas.objects.get(id_per7 = id_persona)
        
            Ventas.objects.create(
                id_persona_fk = persona,
                fecha_venta = json_data['fecha_venta'],
                encola_estado = json_data['encola_estado'],
                total = json_data['total'],
            )
            datos = {'message':'Venta registrada'}
            return JsonResponse(datos)
        except json.JSONDecodeError:
                datos = {'error': 'El formato JSON es incorrecto'}
                return JsonResponse(datos, status=400)
        except Personas.DoesNotExist:
                datos = {'error': 'La persona seleccionada no existe'}
                return JsonResponse(datos, status=400)
    
    def put(self,request, id):
            venta = Ventas.objects.get(id_venta = id)
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