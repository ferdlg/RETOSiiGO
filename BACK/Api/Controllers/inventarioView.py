from Api.models import Inventarios, Productos
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from .serializers import InventariosSerializer
from django.views import View
import json

class InventariosView(View):

    def get(self, request):
        inventario = Inventarios.objects.all()
        serializer = InventariosSerializer(inventario, many=True)
        if len(inventario)>0:
            datos = {'message':'succes', 'Inventario': serializer.data}
        else:
            datos= {'message':'Inventario no encontrado'}
        return datos
    
    def post(self, request):
        json_data = json.loads.body(request.body)
        #obtener valore en el json
        id_producto = json_data['id_producto_fk']
        producto = Productos.objects.get(id_producto=id_producto)
        Inventarios.objects.create(
            id_producto_fk = producto,
            cantidad_producto = json_data['cantidad_producto']
        )
        datos = {'message':'Inventario registrado'}
        return JsonResponse(datos)
    
    #actualizar inventario en base a datos de un archivo excel 