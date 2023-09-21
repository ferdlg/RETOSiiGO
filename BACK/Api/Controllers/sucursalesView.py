from models import Sucursales, Bodegas
from serializers import SucursalesSerializer
from django.http import JsonResponse, request
from django.shortcuts import get_object_or_404
from django.views import View
import json



class SucursalesView(View):

    def verSucursales(self, request, id = None):

        if id is not None and id >0:
            sucursal = Sucursales.objects.filter(id_sucursal = id).first
            if(sucursal):
                serializer = SucursalesSerializer(sucursal)
                datos = {'message':'succes','Sucursal':serializer.data}
            else:
                datos = {'message':'No hay sucursales encontradas'}
            return JsonResponse(datos)
        
        else:
            sucursal = Sucursales.objects.all()
            serializer = SucursalesSerializer(sucursal, many= True)
            if len(sucursal)>0:
                datos = {'message':'succes','Sucursales:': serializer.data}
            else:
                datos = {'message':'No hay sucursales encontradas'}
        return JsonResponse(datos)
    
    def crearSucursales(request):
        if request.method =='POST':
            json_data = json.loads(request.body)
            try:
                id_bodega = json_data['id_bodega_fk']
                bodega = Bodegas.objects.get(id_bodega=id_bodega)
            
                Sucursales.objects.create(
                    nombre_sucursal = json_data['nombre_sucursal'],
                    ciudad = json_data['ciudad'],
                    direccion = json_data['direccion'],
                    email = json_data['email'],
                    id_bodega_fk = bodega
                )
                datos = {'message':'Sucursal registrada'}
                return JsonResponse(datos)
            except json.JSONDecodeError:
                datos={'error','El formato JSON es incorrecto'}
                return JsonResponse(datos, status = 400)
            except bodega.DoesNotExist:
                datos={'error':'La bodega seleccionada no existe'}
        else:
            datos={'error':'Solicitud incorrecta'}
        return JsonResponse(datos)
    
    def actualizarSucursales(request, id):
        if request.method =='PUT':
            sucursal = Sucursales.objects.get(id_sucursal=id)
            json_data= json.loads(request.body)
            try:
                if 'nombre_sucursal' in json_data:
                    Sucursales.nombre_sucursal = json_data['nombre_sucursal']
                
                if 'ciudad' in json_data:
                    Sucursales.ciudad = json_data['ciudad']

                if 'direccion' in json_data:
                    Sucursales.direccion = json_data['direccion']
                
                if 'email' in json_data:
                    Sucursales.email = json_data['email']

                if 'id_bodega_fk' in json_data:
                    id_bodega = json_data['id_bodega_fk']
                    bodega = Sucursales.objects.get(id_bodega = id_bodega)
                    Sucursales.id_bodega_fk = bodega

            except json.JSONDecodeError:
                datos={'message':'El formato JSON es incorrecto'}
                return JsonResponse(datos, status = 400)
            
            except sucursal.DoesNotExist:
                datos = {'error':'La sucursal seleccionada no existe'}
                return JsonResponse(datos, status = 400)        
        else:
            datos ={'message':'Solicitud incorrecta'}
        return JsonResponse(datos)   
    
    def eliminarSucursales(request,id):
        if request.method == 'DELETE':
            sucursal = get_object_or_404(Sucursales, id_sucursal=id)
            sucursal.delete()

            datos={'message':'Sucursal eliminada con exito'}
        else:
            datos = {'message':'Solicitud incorrecta'}
        
        return JsonResponse(datos)