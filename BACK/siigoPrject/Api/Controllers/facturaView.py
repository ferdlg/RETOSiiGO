from models import Factura, Sucursal
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from serializers import FacturaSerializer
from django.views import View
import json

class FacturaView(View):

    def verFactura():
        factura = Factura.objects.all()
        serializer = FacturaSerializer(factura, many = True)
        if len(factura)>0:
            datos = {'message':'succes', 'facturas': serializer.data}
        else:
            datos= {'message':'Facturas no encontradas'}
        return datos
    
    def crearFactura(self, request):
        json_data = json.loads(request.body)
        #obtener campos foraneos        
        id_sucursal = json_data['id_sucursal_fk']
        Factura.objects.create(
            id_sucursal_fk = id_sucursal
        )
        datos = {'message':'factura registrada'}
        return JsonResponse(datos)
    
    
    