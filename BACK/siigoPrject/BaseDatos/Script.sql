DROP DATABASE IF EXISTS siigo_db;
CREATE DATABASE siigo_db;
USE siigo_db;
CREATE TABLE ROLES(
	id_rol int auto_increment not null,
    nombre_rol varchar(20),
    primary key(id_rol)
);
CREATE TABLE PERMISOS(
	id_permiso int auto_increment not null,
    nombre_permiso varchar(30),
    primary key(id_permiso)
);
CREATE TABLE USUARIOS(
	id_usuario int auto_increment not null,
    id_rol_fk int,
	username varchar(30) ,
    email varchar(50),
    password varchar(200),
    primary key(id_usuario),
    foreign key(id_rol_fk) references roles(id_rol)
);

CREATE TABLE BODEGAS(
	id_bodega int auto_increment not null,
    nombre_bodega varchar(30),
    primary key(id_bodega)
);

CREATE TABLE SUCURSALES(
	id_sucursal int auto_increment not null,
    nombre_sucursal varchar(30),
    ciudad varchar(30),
    direccion varchar(50),
    email varchar(50),
    id_bodega_fk int,
    primary key(id_sucursal),
    foreign key(id_bodega_fk) references bodegas(id_bodega)
);
CREATE TABLE PERSONAS(
	id_persona int auto_increment not null,
    id_usuario_fk int,
    nombre_persona varchar(30),
    apellido_persona varchar(30),
    numero_documento int,
    numero_contacto int,
    id_sucursal_fk int,
    primary key(id_persona),
	foreign key(id_sucursal_fk) references sucursales(id_sucursal),
	foreign key(id_usuario_fk) references usuarios(id_usuario)
);

CREATE TABLE ROLES_HAS_PERMISOS(
	id_rol_fk int,
    id_permiso_fk int,
    foreign key(id_rol_fk) references roles(id_rol),
    foreign key(id_permiso_fk) references permisos(id_permiso)
);

CREATE TABLE PRODUCTOS(
	id_producto int auto_increment not null,
    nombre_producto varchar(50),
    precio_produccto float,
    iva float,
    primary key(id_producto)
);

CREATE TABLE INVENTARIOS(
	id_inventario int auto_increment not null,
    id_sucursal_fk int,
    id_bodega_fk int,
    id_producto_fk int,
	stock int,
    primary key(id_inventario),
    foreign key(id_producto_fk) references productos(id_producto),
    foreign key(id_sucursal_fk) references sucursales(id_sucursal),
    foreign key(id_bodega_fk) references bodegas(id_bodega)
);

CREATE TABLE VENTAS(
	id_venta int auto_increment not null,
    id_persona_fk int,
    fecha_venta datetime,
    encola_estado boolean,
    total float,
    primary key(id_venta),
    foreign key(id_persona_fk) references personas(id_persona)
);

CREATE TABLE DETALLE_VENTAS(
	id_detalle int auto_increment not null,
    id_venta_fk int,
    id_producto_fk int,
    cantidad_producto int,
    subtotal float,
    primary key(id_detalle),
    foreign key(id_venta_fk) references ventas(id_venta),
    foreign key(id_producto_fk) references productos(id_producto)
);
CREATE TABLE PROVEEDORES(
	id_persona_fk int,
    id_sucursal_fk int,
    id_producto_fk int,
    foreign key(id_persona_fk) references personas(id_persona),
    foreign key(id_sucursal_fk) references sucursales(id_sucursal),
    foreign key(id_producto_fk) references productos(id_producto)
);


