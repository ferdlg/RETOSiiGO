from django.db import models


class Bodegas(models.Model):
    id_bodega = models.AutoField(primary_key=True)
    nombre_bodega = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bodegas'


class DetalleVentas(models.Model):
    id_detalle = models.AutoField(primary_key=True)
    id_venta_fk = models.ForeignKey('Ventas', models.DO_NOTHING, db_column='id_venta_fk', blank=True, null=True)
    id_producto_fk = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto_fk', blank=True, null=True)
    cantidad_producto = models.IntegerField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle_ventas'


class Inventarios(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    id_sucursal_fk = models.ForeignKey('Sucursales', models.DO_NOTHING, db_column='id_sucursal_fk', blank=True, null=True)
    id_bodega_fk = models.ForeignKey(Bodegas, models.DO_NOTHING, db_column='id_bodega_fk', blank=True, null=True)
    id_producto_fk = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto_fk', blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventarios'


class Permisos(models.Model):
    id_permiso = models.AutoField(primary_key=True)
    nombre_permiso = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permisos'


class Personas(models.Model):
    id_persona = models.AutoField(primary_key=True)
    id_usuario_fk = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario_fk', blank=True, null=True)
    nombre_persona = models.CharField(max_length=30, blank=True, null=True)
    apellido_persona = models.CharField(max_length=30, blank=True, null=True)
    numero_documento = models.IntegerField(blank=True, null=True)
    numero_contacto = models.BigIntegerField(blank=True, null=True)
    id_sucursal_fk = models.ForeignKey('Sucursales', models.DO_NOTHING, db_column='id_sucursal_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personas'


class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=50, blank=True, null=True)
    precio_produccto = models.FloatField(blank=True, null=True)
    iva = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos'


class Proveedores(models.Model):
    id_persona_fk = models.ForeignKey(Personas, models.DO_NOTHING, db_column='id_persona_fk', blank=True, null=True)
    id_sucursal_fk = models.ForeignKey('Sucursales', models.DO_NOTHING, db_column='id_sucursal_fk', blank=True, null=True)
    id_producto_fk = models.ForeignKey(Productos, models.DO_NOTHING, db_column='id_producto_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedores'
        #queso

class Roles(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles'


class RolesHasPermisos(models.Model):
    id_rol_fk = models.ForeignKey(Roles, models.DO_NOTHING, db_column='id_rol_fk', blank=True, null=True)
    id_permiso_fk = models.ForeignKey(Permisos, models.DO_NOTHING, db_column='id_permiso_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roles_has_permisos'


class Sucursales(models.Model):
    id_sucursal = models.AutoField(primary_key=True)
    nombre_sucursal = models.CharField(max_length=30, blank=True, null=True)
    ciudad = models.CharField(max_length=30, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    id_bodega_fk = models.ForeignKey(Bodegas, models.DO_NOTHING, db_column='id_bodega_fk', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sucursales'


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    id_rol_fk = models.ForeignKey(Roles, models.DO_NOTHING, db_column='id_rol_fk', blank=True, null=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'


class Ventas(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_persona_fk = models.ForeignKey(Personas, models.DO_NOTHING, db_column='id_persona_fk', blank=True, null=True)
    fecha_venta = models.DateTimeField(blank=True, null=True)
    encola_estado = models.IntegerField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ventas'
