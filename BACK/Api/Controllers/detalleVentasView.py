from models import DetalleVentas, Usuarios, Ventas, Productos
from django.views import View
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from serializers import DetalleVentasSerializer
import json

class DetalleVentasView(View):

    def verDetalleVentas(self, request, id):
        if id is not None and id>0:
            detalle = DetalleVentas.objects.filter(id_detalle=id).first()#el primer objeto encontrado que coincida con el id
            if (detalle):
                serializer = DetalleVentasSerializer(detalle)
                datos = {'message':'Succes','Detalle':serializer.data}
            else :
                datos ={'error':'Detalle no encontrado'}
            return JsonResponse(datos)
        
        else:
            detalle_venta = DetalleVentas.objects.all()#obtener instancias de la tabla
            serializer = DetalleVentasSerializer(detalle_venta, many=True) #traer el serializador
            if len(detalle_venta)>0:
                datos = {'message':'succes','Detalles de ventas': serializer.data}
            else:
                datos = {'message':'No hay detalles encontrados...'}
        return JsonResponse(datos)
    
    def crearDetalleVentas(request):
        if request.method == 'POST':
            json_data = json.loads(request.body) #ingresar datos json
            try:
                id_usuario=json_data['id_usuario_fk']#obtener valores en el json
                usuario = Usuarios.objects.get(id_usuario=id_usuario)#obtener la instancia con la fk correspondiente
                id_venta=json_data['id_venta_fk']
                venta = Ventas.objects.get(id_venta=id_venta)
                id_producto =json_data['id_producto_fk']
                producto = Productos.objects.get(id_producto=id_producto)
                
                DetalleVentas.objects.create(         #crear instancia detalleVentas
                    id_usuario_fk= usuario,
                    id_venta_fk= venta,
                    id_producto_fk= producto,
                    cantidad_producto = json_data['cantidad_producto']
                )
                datos ={'message':'Detalle de venta registrado'}
                return JsonResponse(datos)
            except json.JSONDecodeError:
                datos={'message':'El formato JSON es incorrecto'}
                return JsonResponse(datos, status = 400)
            except DetalleVentas.DoesNotExist:
                datos={'error':'Uno o mas objetos relacionados no existen'}
        else:
            datos = {'message':'Solicitud incorrecta'}
        return JsonResponse(datos)
    
    def actualizarDetalleVenta(request, id):
        if request.method =='PUT':
            DetalleVenta = DetalleVentas.objects.get(id_detalleVenta = id)
            json_data = json.loads(request.body)
            try:
                if 'id_producto_fk' in json_data:
                    id_producto = json_data['id_producto_fk']
                    producto = Productos.objects.get(id_producto=id_producto)
                    DetalleVenta.id_producto_fk= producto
                
                if 'cantidad_producto' in json_data:
                    DetalleVenta.cantidad_producto=json_data['cantidad_producto']
                
                DetalleVenta.save()
                datos = {'message':'Detalle de venta actualizado con exito'}

            except json.JSONDecodeError:
                datos={'message':'El formato JSON es incorrecto'}
                return JsonResponse(datos, status = 400)
            
            except DetalleVenta.DoesNotExist:
                datos = {'error':'El detalle seleccionado no existe'}
                return JsonResponse(datos, status = 400)
        else:
            datos ={'message':'Solicitud incorrecta'}
        return JsonResponse(datos)