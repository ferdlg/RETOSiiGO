from models import DetalleFactura, Usuario, Factura, Producto
from django.views import View
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from serializers import DetalleFacturaSerializer
import json

class DetalleFacturaView(View):

    def verDetalleFactura(self,request):
        #obtener instancias de la tabla
        detalle_factura = DetalleFactura.objects.all()
        #traer el serializador
        serializer = DetalleFacturaSerializer(detalle_factura, many=True)
        if len(detalle_factura)>0:
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
        usuario = Usuario.objects.get(id_usuario=id_usuario)
        id_factura=json_data['id_factura_fk']
        factura = Factura.objects.get(id_factura=id_factura)
        id_producto =json_data['id_producto_fk']
        producto = Producto.objects.get(id_producto=id_producto)
        #crear instancia detalleFactura
        DetalleFactura.objects.create(
                id_usuario_fk= usuario,
                id_factura_fk= factura,
                id_producto_fk= producto,
                cantidad_detalle = json_data['cantidad_detalle']
        )
        datos ={'message':'Detalle de factura registrado'}
        return JsonResponse(datos)