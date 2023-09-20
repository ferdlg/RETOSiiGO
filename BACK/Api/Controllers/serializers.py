from rest_framework import serializers
from models import Roles, Usuarios, Personas, Proveedores, Productos, Ventas, DetalleVentas, Bodegas, Sucursales, Inventarios

class RolesSerializer(serializers.ModelSerializerSerializer):
    class Meta:
        model = Roles
        fields = '__all__'
    
class UsuariosSerializer(serializers.ModelSerializerSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'

class PersonasSerializer(serializers.ModelSerializerSerializer):
    class Meta:
        model = Personas
        fields = '__all__'

class ProveedoresSerializer(serializers.ModelSerializerSerializer):
    class Meta:
        model = Proveedores
        fields = '__all__'
    
class ProductosSerializer(serializers.ModelSerializerSerializer):
    class Meta:
        model = Productos
        fields = '__all__'

class VentasSerializer(serializers.ModelSerializerSerializer):
    class Meta:
        model = Ventas
        fields = '__all__'

class DetalleVentasSerializer(serializers.ModelSerializerSerializer):
    class Meta:
        model = DetalleVentas
        fields = '__all__'

class SucursalesSerializer(serializers.ModelSerializerSerializer):
    class Meta:
        model = Sucursales
        fields = '__all__'
    
class BodegasSerializer(serializers.ModelSerializerSerializer):
    class Meta:
        model = Bodegas
        fields = '__all__'

class InventariosSerializer(serializers.ModelSerializerSerializer):
    class Meta:
        model = Inventarios
        fields = '__all__'    