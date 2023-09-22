from Api.models import Inventarios, Productos, Bodegas, Sucursales
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .serializers import InventariosSerializer
from django.views import View
import json
import pandas as pd
from django.shortcuts import render


class InventariosView(View):
    @method_decorator(csrf_exempt) 
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, id=None):
            if id is not None and id > 0:
                inventario = Inventarios.objects.filter(id_sucursal=id).first()
                if inventario:
                    serializer = InventariosSerializer(inventario)
                    datos = {'message': 'success', 'Sucursal': serializer.data}
                else:
                    datos = {'message': 'No hay sucursales encontradas'}
                return JsonResponse(datos)
        
            else:
                inventario = Inventarios.objects.all()
                serializer = InventariosSerializer(inventario, many=True)
                if len(inventario) > 0:
                    datos = {'message': 'success', 'Sucursales': serializer.data}
                else:
                    datos = {'message': 'No hay inventarios encontrados'}
            return JsonResponse(datos)
    
    def post(self, request):
        json_data = json.loads(request.body)
        try:
                id_sucursal = json_data['id_sucursal_fk']
                sucursal = Sucursales.objects.get(id_sucursal=id_sucursal)
            
                id_bodega = json_data['id_bodega_fk']
                bodega = Bodegas.objects.get(id_bodega=id_bodega)

                id_producto = json_data['id_producto_fk']
                producto = Productos.objects.get(id_producto=id_producto)

                Inventarios.objects.create(
                    id_sucursal_fk = sucursal,
                    id_bodega_fk=bodega,
                    id_producto_fk=producto,
                    stock = json_data['stock']
                )
                datos = {'message': 'Sucursal registrada'}
                return JsonResponse(datos)
        except json.JSONDecodeError:
                datos = {'error': 'El formato JSON es incorrecto'}
                return JsonResponse(datos, status=400)
        except Inventarios.DoesNotExist:
                datos = {'error': 'Varios elementos seleccionados no existen'}
                return JsonResponse(datos, status=400)
    #actualizar inventario en base a datos de un archivo excel 
    def put(request):
        if request.FILES.get('RegistrosBD'):
            archivo = request.FILES['RegistrosBD']
            try:
                df = pd.read_excel(archivo)
                for _, row in df.iterrows():
                    id_sucursal = row['id_sucursal_fk']
                    id_bodega = row['id_bodega_fk']
                    id_producto = row['id_producto_fk']
                    stock = row['stock']
            #actualizar inventario en base a datos del excel 
                try:
                    inventario = Inventarios.objects.get(
                        id_sucursal_fk=id_sucursal,
                        id_bodega_fk=id_bodega,
                        id_producto_fk=id_producto
                        )
                    inventario.stock = stock
                    inventario.save()
                except Inventarios.DoesNotExist:
                        Inventarios.objects.create(
                            id_sucursal_fk=id_sucursal,
                            id_bodega_fk=id_bodega,
                            id_producto_fk=id_producto,
                            stock=stock
                        )
                return JsonResponse({'message': 'Inventario actualizado con éxito'})
            except pd.errors.EmptyDataError:
                return JsonResponse({'error': 'El archivo Excel está vacío'}, status=400)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=400)
        else:
            return JsonResponse({'error': 'No se proporcionó un archivo Excel'}, status=400)