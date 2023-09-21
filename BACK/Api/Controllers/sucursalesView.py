from models import Sucursales
from serializers import SucursalesSerializer
from django.http import JsonResponse, request
from django.views import View
import json



class SucursalesView(View):

    def verSucursales(self):
        sucursal = Sucursales.objects.all()
        serializer = SucursalesSerializer(sucursal, many= True)

        if len(sucursal)>0:
            datos = {'message':'succes','Sucursales:': serializer.data}
        else:
            datos = {'message':'No hay sucursales'}

        return JsonResponse(datos)
    
    def crearSucursales(request):

        return
    
    def actualizarSucursales(request):
        return
    
    def eliminarSucursales(request):
        return