from models import Sucursales
from serializers import SucursalesSerializer
from django.http import JsonResponse, request
from django.views import View
import json



class SucursalesView(View):

    def verSucursales(self, request):
        sucursal = Sucursales.objects.all()
        serializer = SucursalesSerializer(sucursal, many= True)

        if len(sucursal)>0:
            datos = {'message':'succes','Sucursales:': serializer.data}
        else:
            datos = {'message':'No hay sucursales'}

        return JsonResponse(datos)
    
    def crearSucursales(self, request):

        return
    
    def actualizarSucursales(self, request):
        return
    
    def eliminarSucursales(sefl, request):
        return