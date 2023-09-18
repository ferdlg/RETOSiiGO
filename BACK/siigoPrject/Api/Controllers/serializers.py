from rest_framework import serializers
from models import Empresa, Bodega, Proveedor, Sucursal, Producto, Inventario, Factura, DetalleFactura, Usuario

class EmpresaSerializer(serializers.ModelSerializerSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class BodegaSerializer(serializers.ModelSerializerSerializer):
    class Meta:
        model = Bodega
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Proveedor
        fields = '__all__'

class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'

class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = '__all__'

class DetalleFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleFactura
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'