from django.views import View
from django.http import request, JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from ..models import Usuarios, Roles
from .serializers import UsuariosSerializer

class UsuariosView(View):
    @method_decorator(csrf_exempt) 
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = None):
        if id is not None and id >0:
            usuario = Usuarios.objects.filter(id_usuario = id).first()
            if usuario:
                serializer = UsuariosSerializer(usuario)
                datos = {'message':'Success', 'Usuario': serializer.data}
            else:
                datos = {'message':'Usuario no encontrado'}
        else: 
            usuario = Usuarios.objects.all()
            serializer = UsuariosSerializer(usuario, many=True)
            if len(usuario)>0:
                datos = {'message':'success','usuarios':serializer.data}
            else:
                datos = {'message':'No hay usuarios registrados'}

        return JsonResponse(datos)
    
    def post(self, request):
        json_data = json.loads(request.body)
        try:
                id_rol = json_data['id_rol_dk']
                rol = Roles.objects.get(id_rol = id_rol)

                Usuarios.objects.create(
                    username=json_data['nombre_bodega'],
                    email = json_data['email'],
                    password= json_data['password']
                )
                datos = {'message': 'Usuario registrada'}
                return JsonResponse(datos)
        except json.JSONDecodeError:
                datos = {'error': 'El formato JSON es incorrecto'}
                return JsonResponse(datos, status=400)

    def put(self, request, id):
        usuario = Usuarios.object.get(id_bodega = id)
        json_data = json.loads(request.body)
        try:
            if 'nombre_bodega' in json_data:
                usuario.nombre_bodega  = json_data['nombre_bodega']
                
                datos = {'message': 'Usuario actualizada con éxito'}
        except json.JSONDecodeError:
                datos = {'message': 'El formato JSON es incorrecto'}
                return JsonResponse(datos, status=400)
            
        except Usuarios.DoesNotExist:
                datos = {'error': 'El usuario seleccionado no existe'}
                return JsonResponse(datos, status=400)        
        return JsonResponse(datos)            

            

    def delete(self, request, id):
        try:
            usuario = get_object_or_404(Usuarios, id_usuario=id)
            usuario.delete()
            return JsonResponse({'message': 'Usuario eliminado con éxito'})
        except Usuarios.DoesNotExist:
            return JsonResponse({'error': 'El usuario seleccionado no existe'}, status=404)