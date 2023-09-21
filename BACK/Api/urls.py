from django.contrib import admin
from .Controllers.inventarioView import InventariosView
from .Controllers.ventasView import VentaView
from .Controllers.detalleVentasView import DetalleVentasView
from django.urls import path

urlpatterns = [
    path('ventas/',VentaView.as_view() , name="venta vista"),
    path('detalleVentas/',DetalleVentasView.as_view(), name="detalle ventas vista"),
    path('detalleVenta/<int:id>',DetalleVentasView.as_view(), name="detalle venta vista"),
    path('inventario/',InventariosView.as_view(), name="Inventario"),
]
