import django.dispatch
from django.dispatch import Signal, receiver
from Api.models import Inventarios, Bodegas, Productos, Proveedores, estadoVenta, Ventas
from django.core.mail import send_mail

#definir la señal de notificar al proveedor
correo_proveedor = django.dispatch.Signal()
#crear un receptor, que puede ser funcion
@receiver(correo_proveedor) 
def notificarProveedor(sender, **kawargs):
    producto = sender
    Inventario = Inventarios.objects.get(id_producto_fk = producto)
    cantidad_producto = Inventario.cantidad_producto
    if cantidad_producto in Inventario <10:
        proveedor = Productos.id_proveedor_fk
        mensaje = f'Proveedor, esta es una notificacion de que la existencias del producto{Productos.nombre_producto} se han agotado'
        # Enviar notificación al proveedor
        send_mail(
            'Notificación de inventario',
            mensaje,
            'ferdlgpar@gmail.com',  # Remitente
            [proveedor.email],  # Destinatario
        )

#producto de nuevo en stock, notificacion 

correo_sucursal = django.dispatch.Signal()
@receiver(correo_sucursal)
def notificar_sucursal(sender, **kwargs):
    producto = sender
    inventario = Inventarios.objects.get(id_producto_fk=producto)
    cantidad_producto = inventario.stock
    if cantidad_producto > 10:
        sucursal = inventario.id_sucursal_fk
        mensaje = f'Sucursal, este es un aviso de que las existencias del producto {producto.nombre_producto} han vuelto a estar disponibles.'
        send_mail(
            'Notificación de inventario',
            mensaje,
            'ferdlgpar@gmail.com',  # Remitente
            [sucursal.email],  # Destinatario
        )