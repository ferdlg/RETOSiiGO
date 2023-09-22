from django.views import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from ..models import Sucursales, Bodegas
from .serializers import SucursalesSerializer  # Asegúrate de importar el serializador adecuado

class SucursalesView(View):
        
    @method_decorator(csrf_exempt) 
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=None):
            if id is not None and id > 0:
                sucursal = Sucursales.objects.filter(id_sucursal=id).first()
                if sucursal:
                    serializer = SucursalesSerializer(sucursal)
                    datos = {'message': 'success', 'Sucursal': serializer.data}
                else:
                    datos = {'message': 'No hay sucursales encontradas'}
                return JsonResponse(datos)
        
            else:
                sucursal = Sucursales.objects.all()
                serializer = SucursalesSerializer(sucursal, many=True)
                if len(sucursal) > 0:
                    datos = {'message': 'success', 'Sucursales': serializer.data}
                else:
                    datos = {'message': 'No hay sucursales registradas'}
            return JsonResponse(datos)
    
    def post(self, request):
        json_data = json.loads(request.body)
        try:
                id_bodega = json_data['id_bodega_fk']
                bodega = Bodegas.objects.get(id_bodega=id_bodega)
            
                Sucursales.objects.create(
                    nombre_sucursal=json_data['nombre_sucursal'],
                    ciudad=json_data['ciudad'],
                    direccion=json_data['direccion'],
                    email=json_data['email'],
                    id_bodega_fk=bodega
                )
                datos = {'message': 'Sucursal registrada'}
                return JsonResponse(datos)
        except json.JSONDecodeError:
                datos = {'error': 'El formato JSON es incorrecto'}
                return JsonResponse(datos, status=400)
        except Bodegas.DoesNotExist:
                datos = {'error': 'La bodega seleccionada no existe'}
                return JsonResponse(datos, status=400)
    
    def put(self, request, id):
            sucursal = Sucursales.objects.get(id_sucursal=id)
            json_data = json.loads(request.body)
            try:
                if 'nombre_sucursal' in json_data:
                    sucursal.nombre_sucursal = json_data['nombre_sucursal']
                
                if 'ciudad' in json_data:
                    sucursal.ciudad = json_data['ciudad']

                if 'direccion' in json_data:
                    sucursal.direccion = json_data['direccion']
                
                if 'email' in json_data:
                    sucursal.email = json_data['email']

                if 'estado_inactiva' in json_data:
                    sucursal.estado_inactiva = json_data['estado_inactiva']

                if 'id_bodega_fk' in json_data:
                    id_bodega = json_data['id_bodega_fk']
                    bodega = Bodegas.objects.get(id_bodega=id_bodega)
                    sucursal.id_bodega_fk = bodega

                sucursal.save()  

                datos = {'message': 'Sucursal actualizada con éxito'}
            except json.JSONDecodeError:
                datos = {'message': 'El formato JSON es incorrecto'}
                return JsonResponse(datos, status=400)
            
            except Sucursales.DoesNotExist:
                datos = {'error': 'La sucursal seleccionada no existe'}
                return JsonResponse(datos, status=400)        
            return JsonResponse(datos)
    
