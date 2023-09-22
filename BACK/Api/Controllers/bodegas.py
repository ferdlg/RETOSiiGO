from django.views import View
from django.http import request, JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from ..models import Sucursales, Bodegas
from .serializers import BodegasSerializer

class BodegasView(View):
    @method_decorator(csrf_exempt) 
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = None):
        if id is not None and id >0:
            bodega = Bodegas.objects.filter(id_bodega = id).first()
            if bodega:
                serializer = BodegasSerializer(bodega)
                datos = {'message':'Success', 'Bodega': serializer.data}
            else:
                datos = {'message':'Bodega no encontrada'}
        else: 
            bodega = Bodegas.objects.all()
            serializer = BodegasSerializer(bodega, many=True)
            if len(bodega)>0:
                datos = {'message':'success','Bodegas':serializer.data}
            else:
                datos = {'message':'No hay bodegas registradas'}

        return JsonResponse(datos)
    
    def post(self, request):
        json_data = json.loads(request.body)
        try:
                Bodegas.objects.create(
                    nombre_bodega=json_data['nombre_bodega'],
                )
                datos = {'message': 'Bodega registrada'}
                return JsonResponse(datos)
        except json.JSONDecodeError:
                datos = {'error': 'El formato JSON es incorrecto'}
                return JsonResponse(datos, status=400)

    def put(self, request, id):
        bodega = Bodegas.object.get(id_bodega = id)
        json_data = json.loads(request.body)
        try:
            if 'nombre_bodega' in json_data:
                bodega.nombre_bodega  = json_data['nombre_bodega']
                
                datos = {'message': 'Bodega actualizada con éxito'}
        except json.JSONDecodeError:
                datos = {'message': 'El formato JSON es incorrecto'}
                return JsonResponse(datos, status=400)
            
        except Bodegas.DoesNotExist:
                datos = {'error': 'La sucursal seleccionada no existe'}
                return JsonResponse(datos, status=400)        
        return JsonResponse(datos)            

    def delete(self, request, id):
        try:
            bodega = get_object_or_404(Bodegas, id_usuario=id)
            bodega.delete()
            return JsonResponse({'message': 'Bodega eliminada con éxito'})
        except Bodegas.DoesNotExist:
            return JsonResponse({'error': 'La bodega seleccionada no existe'}, status=404)

