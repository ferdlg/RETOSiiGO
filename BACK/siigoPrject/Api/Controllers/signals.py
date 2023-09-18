import django.dispatch
from django.dispatch import Signal, receiver
from models import Inventario, Bodega, Producto, Proveedor
from django.core.mail import send_mail

#definir la señal
correo_proveedor = django.dispatch.Signal
#crear un receptor, que puede ser funcion
@receiver(correo_proveedor) 
def notificarProveedor(sender, **kawargs):
    producto = sender
    inventario = Inventario.objects.get(id_producto_fk = producto)
    cantidad_producto = Inventario.cantidad_producto
    if cantidad_producto in Inventario <10:
        proveedor = Producto.id_proveedor_fk
        mensaje = f'Proveedor, esta es una notificacion de que la existencias del producto{Producto.nombre_producto} se han agotado'
        # Enviar notificación al proveedor
        send_mail(
            'Notificación de inventario',
            mensaje,
            'tu_correo@gmail.com',  # Remitente
            [proveedor.email],  # Destinatario
        )