from django.contrib import admin
from Controllers.inventarioView import InventarioView
from Controllers.facturaView import FacturaView
from Controllers.detalleFacturaView import DetalleFacturaView
from django.urls import path

urlpatterns = [
    path('factura/',FacturaView , name="factura vista"),
    path('detallefactura/',DetalleFacturaView , name="detalle factura vista"),
    path('inventario/',InventarioView , name="Inventario"),
]
