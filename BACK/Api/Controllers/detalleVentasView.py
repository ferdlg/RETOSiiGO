from Api.models import DetalleVentas, Usuarios, Ventas, Productos
from django.views import View
from django.http.request import HttpRequest
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from .serializers import DetalleVentasSerializer
import json

class DetalleVentasView(View):
    @method_decorator(csrf_exempt) 
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, id):
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
    
    def post(self, request):
            json_data = json.loads(request.body) #ingresar datos json
            try:
                id_venta=json_data['id_venta_fk']
                venta = Ventas.objects.get(id_venta=id_venta)
                id_producto =json_data['id_producto_fk']
                producto = Productos.objects.get(id_producto=id_producto)
                
                DetalleVentas.objects.create(         #crear instancia detalleVentas
                    id_venta_fk= venta,
                    id_producto_fk= producto,
                    cantidad_producto = json_data['cantidad_producto'],
                    subtotal = json_data['subtotal']
                )
                datos ={'message':'Detalle de venta registrado'}
                return JsonResponse(datos)
            except json.JSONDecodeError:
                datos={'message':'El formato JSON es incorrecto'}
                return JsonResponse(datos, status = 400)
            except DetalleVentas.DoesNotExist:
                datos={'error':'Uno o mas objetos relacionados no existen'}
            return JsonResponse(datos)
    
    def put(self, request, id):
            DetalleVenta = DetalleVentas.objects.get(id_detalle = id)
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
            return JsonResponse(datos)