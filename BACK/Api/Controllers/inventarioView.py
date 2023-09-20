from models import Inventario, Producto
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from serializers import InventarioSerializer
from django.views import View
import json

class InventarioView(View):

    def verInventario(self, request):
        inventario = Inventario.objects.all()
        serializer = InventarioSerializer(inventario, many=True)
        if len(inventario)>0:
            datos = {'message':'succes', 'Inventario': serializer.data}
        else:
            datos= {'message':'Inventario no encontrado'}
        return datos
    
    def addInventario(self, request):
        json_data = json.loads.body(request.body)
        #obtener valore en el json
        id_producto = json_data['id_producto_fk']
        producto = Producto.objects.get(id_producto=id_producto)
        Inventario.objects.create(
            id_producto_fk = producto,
            cantidad_producto = json_data['cantidad_producto']
        )
        datos = {'message':'Inventario registrado'}
        return JsonResponse(datos)