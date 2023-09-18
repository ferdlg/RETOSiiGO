from django.db import models


class Bodega(models.Model):
    id_bodega = models.AutoField(db_column='ID_BODEGA', primary_key=True)  # Field name made lowercase.
    nombre_bodega = models.CharField(db_column='NOMBRE_BODEGA', max_length=30, blank=True, null=True)  # Field name made lowercase.
    id_proveedor_fk = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='ID_PROVEEDOR_FK', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'bodega'


class DetalleFactura(models.Model):
    id_detalle = models.AutoField(db_column='ID_DETALLE', primary_key=True)  # Field name made lowercase.
    id_usuario_fk = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='ID_USUARIO_FK', blank=True, null=True)  # Field name made lowercase.
    id_factura_fk = models.ForeignKey('Factura', models.DO_NOTHING, db_column='ID_FACTURA_FK', blank=True, null=True)  # Field name made lowercase.
    id_producto_fk = models.ForeignKey('Producto', models.DO_NOTHING, db_column='ID_PRODUCTO_FK', blank=True, null=True)  # Field name made lowercase.
    cantidad_detalle = models.IntegerField(db_column='CANTIDAD_DETALLE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'detalle_factura'


class Empresa(models.Model):
    id_empresa = models.AutoField(db_column='ID_EMPRESA', primary_key=True)  # Field name made lowercase.
    nomre_empresa = models.CharField(db_column='NOMRE_EMPRESA', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'empresa'


class Factura(models.Model):
    id_factura = models.AutoField(db_column='ID_FACTURA', primary_key=True)  # Field name made lowercase.
    fecha_factura = models.DateTimeField(db_column='FECHA_FACTURA', auto_now_add= True)  # Field name made lowercase.
    id_sucursal_fk = models.ForeignKey('Sucursal', models.DO_NOTHING, db_column='ID_SUCURSAL_FK', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'factura'


class Inventario(models.Model):
    id_producto_fk = models.ForeignKey('Producto', models.DO_NOTHING, db_column='ID_PRODUCTO_FK', blank=True, null=True)  # Field name made lowercase.
    cantidad_producto = models.CharField(db_column='CANTIDAD_PRODUCTO', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'inventario'


class Producto(models.Model):
    id_producto = models.AutoField(db_column='ID_PRODUCTO', primary_key=True)  # Field name made lowercase.
    nombre_producto = models.CharField(db_column='NOMBRE_PRODUCTO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    precio_producto = models.CharField(db_column='PRECIO_PRODUCTO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iva = models.DecimalField(db_column='IVA', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producto'


class Proveedor(models.Model):
    id_proveedor = models.AutoField(db_column='ID_PROVEEDOR', primary_key=True)  # Field name made lowercase.
    nombre_proveedor = models.CharField(db_column='NOMBRE_PROVEEDOR', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email_proveedor = models.CharField(db_column='EMAIL_PROVEEDOR', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'proveedor'


class Sucursal(models.Model):
    id_sucursal = models.AutoField(db_column='ID_SUCURSAL', primary_key=True)  # Field name made lowercase.
    ciudad = models.CharField(db_column='CIUDAD', max_length=50, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='DIRECCION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    id_empresa_fk = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='ID_EMPRESA_FK', blank=True, null=True)  # Field name made lowercase.
    email_sucursal = models.CharField(db_column='EMAIL_SUCURSAL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    id_bodega_fk = models.ForeignKey(Bodega, models.DO_NOTHING, db_column='ID_BODEGA_FK', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'sucursal'


class Usuario(models.Model):
    id_usuario = models.IntegerField(db_column='ID_USUARIO', primary_key=True)  # Field name made lowercase.
    nombre_usuario = models.CharField(db_column='NOMBRE_USUARIO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    apellido_usuario = models.CharField(db_column='APELLIDO_USUARIO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'usuario'
