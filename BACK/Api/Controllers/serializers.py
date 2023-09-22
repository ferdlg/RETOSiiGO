from rest_framework import serializers
from Api.models import Roles, Usuarios, Personas, Proveedores, Productos, Ventas, DetalleVentas, Bodegas, Sucursales, Inventarios

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'
    
class UsuariosSerializer(serializers.ModelSerializer):
    rol = RolesSerializer(source = 'id_rol_fk', read_only = True)
    class Meta:
        model = Usuarios
        fields = [
            'rol',
            'id_usuario',
            'username',
            'email'
        ]

class BodegasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bodegas
        fields = '__all__'

class SucursalesSerializer(serializers.ModelSerializer):
    bodega = BodegasSerializer(source = 'id_bodega_fk', read_only = True)
    class Meta:
        model = Sucursales
        fields = [
            'id_sucursal',
            'nombre_sucursal',
            'ciudad',
            'direccion',
            'email',
            'estado_inactiva',
            'bodega'
        ]

class PersonasSerializer(serializers.ModelSerializer):
    usuario = UsuariosSerializer(source = 'id_usuario_fk', read_only = True)
    sucursal =SucursalesSerializer(source = 'id_sucursal_fk', read_only = True)
    class Meta:
        model = Personas
        fields = [
        'id_persona',
        'nombre_persona',
        'apellido_persona',
        'numero_documento',
        'numero_contacto',
        'usuario',
        'sucursal'
        ]

class ProveedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedores
        fields = '__all__'
    
class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'

class VentasSerializer(serializers.ModelSerializer):
    persona = PersonasSerializer(source = 'id_persona_fk', read_only = True)
    class Meta:
        model = Ventas
        fields = [
            'id_venta',
            'fecha_venta',
            'encola_estado',
            'total',
            'persona'
        ]

class DetalleVentasSerializer(serializers.ModelSerializer):
    venta = VentasSerializer(source = 'id_venta_fk', read_only = True)
    producto = ProductosSerializer(source = 'id_producto_fk', read_only = True)
    class Meta:
        model = DetalleVentas
        fields = [
            'id_detalle',
            'cantidad_producto',
            'subtotal',
            'venta',    
            'producto'
        ]

class InventariosSerializer(serializers.ModelSerializer):
    sucursal = SucursalesSerializer(source = 'id_sucursal_fk', read_only = True)
    bodega = BodegasSerializer(source = 'id_bodega_fk', read_only = True)
    producto = ProductosSerializer(source = 'id_producto_fk', read_only = True)
    class Meta:
        model = Inventarios
        fields = [
            'id_inventario',
            'sucursal',
            'bodega',
            'producto'
        ]    