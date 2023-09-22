from django.contrib import admin
from .Controllers.inventarioView import InventariosView
from .Controllers.ventasView import VentaView
from .Controllers.detalleVentasView import DetalleVentasView
from .Controllers.sucursalesView import SucursalesView 
from django.urls import path

urlpatterns = [
    path('ventas/',VentaView.as_view() , name="ventas-vista"),
    path('ventas/<int:id>',VentaView.as_view(), name="venta-vista"),
    path('detalleVentas/',DetalleVentasView.as_view(), name="detalle-ventas-vista"),
    path('detalleVentas/<int:id>',DetalleVentasView.as_view(), name="detalle-venta-vista"),
    path('inventarios/',InventariosView.as_view(), name="Inventarios"),
    path('inventarios/<int:id>',InventariosView.as_view(), name="Inventario"),
    path('listsucursales/', SucursalesView.as_view(), name="List-Sucursales"),
    path('listsucursales/<int:id>',SucursalesView.as_view(), name="sucursal-vista"),

]
