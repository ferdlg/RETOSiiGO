from models import DetalleVentas, Usuarios, Ventas, Productos
from django.views import View
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from serializers import DetalleVentasSerializer
import json

class DetalleVentasView(View):

    def verDetalleFactura(self,request):
        #obtener instancias de la tabla
        detalle_venta = DetalleVentas.objects.all()
        #traer el serializador
        serializer = DetalleVentasSerializer(detalle_venta, many=True)
        if len(detalle_venta)>0:
            datos = {'message':'succes','Detalles de facturas': serializer.data}
        else:
            datos = {'message':'Detalles no encontrados...'}
        return datos
    
    def crearDetalleFactura(self, request):
        #ingresar datos json
        json_data = json.loads(request.body)
        #obtener valore en el json
        id_usuario=json_data['id_usuario_fk']
        #obtener la instancia con la fk correspondiente
        usuario = Usuarios.objects.get(id_usuario=id_usuario)
        id_venta=json_data['id_venta_fk']
        venta = Ventas.objects.get(id_factura=id_venta)
        id_producto =json_data['id_producto_fk']
        producto = Productos.objects.get(id_producto=id_producto)
        #crear instancia detalleFactura
        DetalleVentas.objects.create(
                id_usuario_fk= usuario,
                id_venta_fk= venta,
                id_producto_fk= producto,
                cantidad_producto = json_data['cantidad_producto']
        )
        datos ={'message':'Detalle de venta registrado'}
        return JsonResponse(datos)