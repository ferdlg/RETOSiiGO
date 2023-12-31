from django.views import View
from django.http import request, JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from ..models import Personas, Usuarios
from .serializers import PersonasSerializer

class PersonasView(View):
    @method_decorator(csrf_exempt) 
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = None):
        if id is not None and id >0:
            persona = Personas.objects.filter(id_persona = id).first()
            if persona:
                serializer = PersonasSerializer(persona)
                datos = {'message':'Success', 'Persona': serializer.data}
            else:
                datos = {'message':'Persona no encontrada'}
        else: 
            persona = Personas.objects.all()
            serializer = PersonasSerializer(persona, many=True)
            if len(persona)>0:
                datos = {'message':'success','Personas':serializer.data}
            else:
                datos = {'message':'No hay personas registradas'}

        return JsonResponse(datos)
    
    def post(self, request):
        json_data = json.loads(request.body)
        try:
                id_usuario = json_data['id_usuario_fk']
                usuario = Usuarios.objects.get(id_usuario=id_usuario)
                
                id_sucursal = json_data['id_sucursal_fk']
                sucursal = sucursal.objects.get(id_sucursal = id_sucursal)

                Personas.objects.create(
                    nombre_bodega=json_data['nombre_bodega'],
                )
                datos = {'message': 'Bodega registrada'}
                return JsonResponse(datos)
        except json.JSONDecodeError:
                datos = {'error': 'El formato JSON es incorrecto'}
                return JsonResponse(datos, status=400)

    def put(self, request, id):
        bodega = Personas.object.get(id_bodega = id)
        json_data = json.loads(request.body)
        try:
            if 'nombre_bodega' in json_data:
                bodega.nombre_bodega  = json_data['nombre_bodega']
                
                datos = {'message': 'Bodega actualizada con éxito'}
        except json.JSONDecodeError:
                datos = {'message': 'El formato JSON es incorrecto'}
                return JsonResponse(datos, status=400)
            
        except Personas.DoesNotExist:
                datos = {'error': 'La persona seleccionada no existe'}
                return JsonResponse(datos, status=400)        
        return JsonResponse(datos)            
