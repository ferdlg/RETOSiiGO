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
    numero_contacto bigint,
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

drop trigger if exists actualiza_stock_inventario;
delimiter $$
create trigger actualiza_stock_inventario after insert on detalle_ventas
for each row
begin
	declare cantidad_producto INT;
    declare stock_actual INT;
    declare estado_venta boolean;
    select cantidad into cantidad_producto from detalle_ventas where id_venta_fk = NEW.id_venta_fk;
    select stock into stock_actual from inventarios where id_producto = NEW.id_producto_fk;
    if stock_actual>=cantidad_producto THEN
		update inventarios
		set stock = stock-cantidad_producto
		where id_producto = NEW.id_producto_fk;
	end if;
end $$

INSERT INTO ROLES (nombre_rol)
VALUE
	('SuperAdmin'),
    ('AdminSucursal'),
    ('EmpleadoSucursal'),
    ('Proveedor');
    
INSERT INTO USUARIOS (id_rol_fk, username, email, password)
VALUES
  (1, 'Fernanda', 'ferdlgpar@gmail.com', 'clave1'),
  (2, 'usuario2', 'usuario2@example.com', 'clave2'),
  (3, 'usuario3', 'usuario3@example.com', 'clave3'),
  (4, 'usuario4', 'usuario4@example.com', 'clave4'),
  (1, 'usuario5', 'usuario5@example.com', 'clave5'),
  (2, 'usuario6', 'usuario6@example.com', 'clave6'),
  (3, 'usuario7', 'usuario7@example.com', 'clave7'),
  (4, 'Camila', 'ariasruizcamilaa@gmail.com', 'clave8'),
  (1, 'usuario9', 'usuario9@example.com', 'clave9'),
  (2, 'usuario10', 'usuario10@example.com', 'clave10'),
  (3, 'usuario11', 'usuario11@example.com', 'clave11'),
  (4, 'usuario12', 'usuario12@example.com', 'clave12'),
  (1, 'usuario13', 'usuario13@example.com', 'clave13'),
  (2, 'usuario14', 'usuario14@example.com', 'clave14'),
  (3, 'usuario15', 'usuario15@example.com', 'clave15');
  INSERT INTO BODEGAS (nombre_bodega)
VALUES
  ('Bodega1'),
  ('Bodega2'),
  ('Bodega3'),
  ('Bodega4'),
  ('Bodega5'),
  ('Bodega6'),
  ('Bodega7'),
  ('Bodega8'),
  ('Bodega9'),
  ('Bodega10'),
  ('Bodega11'),
  ('Bodega12'),
  ('Bodega13'),
  ('Bodega14'),
  ('Bodega15');
  INSERT INTO SUCURSALES (nombre_sucursal, ciudad, direccion, email, id_bodega_fk, estado_inactiva)
VALUES
  ('Sucursal1', 'Ciudad1', 'Dirección1', 'sucursal1@example.com', 1, 0),
  ('Sucursal2', 'Ciudad2', 'Dirección2', 'sucursal2@example.com', 2, 0),
  ('Sucursal3', 'Ciudad3', 'Dirección3', 'sucursal3@example.com', 3, 0),
  ('Sucursal4', 'Ciudad4', 'Dirección4', 'sucursal4@example.com', 1, 0),
  ('Sucursal5', 'Ciudad5', 'Dirección5', 'sucursal5@example.com', 2, 0),
  ('Sucursal6', 'Ciudad6', 'Dirección6', 'sucursal6@example.com', 3, 0),
  ('Sucursal7', 'Ciudad7', 'Dirección7', 'sucursal7@example.com', 1, 0),
  ('Sucursal8', 'Ciudad8', 'Dirección8', 'sucursal8@example.com', 2, 0),
  ('Sucursal9', 'Ciudad9', 'Dirección9', 'sucursal9@example.com', 3, 0),
  ('Sucursal10', 'Ciudad10', 'Dirección10', 'sucursal10@example.com', 1, 0),
  ('Sucursal11', 'Ciudad11', 'Dirección11', 'sucursal11@example.com', 2, 0),
  ('Sucursal12', 'Ciudad12', 'Dirección12', 'sucursal12@example.com', 3, 0),
  ('Sucursal13', 'Ciudad13', 'Dirección13', 'sucursal13@example.com', 1, 0),
  ('Sucursal14', 'Ciudad14', 'Dirección14', 'sucursal14@example.com', 2, 0),
  ('Sucursal15', 'Ciudad15', 'Dirección15', 'sucursal15@example.com', 3, 0);
  INSERT INTO PERSONAS (id_usuario_fk, nombre_persona, apellido_persona, numero_documento, numero_contacto, id_sucursal_fk)
VALUES
  (1, 'Nombre1', 'Apellido1', 1234567891, 9876543211, 1),
  (2, 'Nombre2', 'Apellido2', 1234567892, 9876543212, 2),
  (3, 'Nombre3', 'Apellido3', 1234567893, 9876543213, 3),
  (4, 'Nombre4', 'Apellido4', 1234567894, 9876543214, 1),
  (5, 'Nombre5', 'Apellido5', 1234567895, 9876543215, 2),
  (6, 'Nombre6', 'Apellido6', 1234567896, 9876543216, 3),
  (7, 'Nombre7', 'Apellido7', 1234567897, 9876543217, 1),
  (8, 'Nombre8', 'Apellido8', 1234567898, 9876543218, 2),
  (9, 'Nombre9', 'Apellido9', 1234567899, 9876543219, 3),
  (10, 'Nombre10', 'Apellido10', 1234567800, 9876543220, 1),
  (11, 'Nombre11', 'Apellido11', 1234567801, 9876543221, 2),
  (12, 'Nombre12', 'Apellido12', 1234567802, 9876543222, 3),
  (13, 'Nombre13', 'Apellido13', 1234567803, 9876543223, 1),
  (14, 'Nombre14', 'Apellido14', 1234567804, 9876543224, 2),
  (15, 'Nombre15', 'Apellido15', 1234567805, 9876543225, 3);
  INSERT INTO PRODUCTOS (nombre_producto, precio_produccto, iva)
VALUES
  ('Producto1', 10.99, 0.16),
  ('Producto2', 15.99, 0.16),
  ('Producto3', 8.49, 0.16),
  ('Producto4', 12.99, 0.16),
  ('Producto5', 9.99, 0.16),
  ('Producto6', 14.49, 0.16),
  ('Producto7', 11.99, 0.16),
  ('Producto8', 7.99, 0.16),
  ('Producto9', 13.99, 0.16),
  ('Producto10', 6.49, 0.16),
  ('Producto11', 16.99, 0.16),
  ('Producto12', 10.49, 0.16),
  ('Producto13', 18.99, 0.16),
  ('Producto14', 7.49, 0.16),
  ('Producto15', 9.99, 0.16);
  
  -- Insertar 15 registros ficticios en la tabla INVENTARIOS
INSERT INTO INVENTARIOS (id_sucursal_fk, id_bodega_fk, id_producto_fk, stock)
VALUES
  (1, 1, 1, 100),
  (1, 2, 2, 50),
  (2, 1, 3, 75),
  (2, 2, 4, 60),
  (3, 1, 5, 80),
  (3, 2, 6, 40),
  (4, 1, 7, 90),
  (4, 2, 8, 70),
  (5, 1, 9, 110),
  (5, 2, 10, 55),
  (6, 1, 11, 65),
  (6, 2, 12, 85),
  (7, 1, 13, 95),
  (7, 2, 14, 45),
  (8, 1, 15, 120);
-- Insertar 15 registros ficticios en la tabla INVENTARIOS
INSERT INTO INVENTARIOS (id_sucursal_fk, id_bodega_fk, id_producto_fk, stock)
VALUES
  (1, 1, 1, 100),
  (1, 2, 2, 50),
  (2, 1, 3, 75),
  (2, 2, 4, 60),
  (3, 1, 5, 80),
  (3, 2, 6, 40),
  (4, 1, 7, 90),
  (4, 2, 8, 70),
  (5, 1, 9, 110),
  (5, 2, 10, 55),
  (6, 1, 11, 65),
  (6, 2, 12, 85),
  (7, 1, 13, 95),
  (7, 2, 14, 45),
  (8, 1, 15, 120);
-- Insertar 15 registros ficticios en la tabla VENTAS
INSERT INTO VENTAS (id_persona_fk, fecha_venta, encola_estado, total)
VALUES
  (1, '2023-09-15 10:00:00', true, 500.00),
  (2, '2023-09-15 11:00:00', false, 750.00),
  (3, '2023-09-15 12:00:00', true, 300.00),
  (4, '2023-09-15 13:00:00', false, 650.00),
  (5, '2023-09-15 14:00:00', true, 800.00),
  (6, '2023-09-15 15:00:00', false, 350.00),
  (7, '2023-09-15 16:00:00', true, 900.00),
  (8, '2023-09-15 17:00:00', false, 400.00),
  (9, '2023-09-15 18:00:00', true, 550.00),
  (10, '2023-09-15 19:00:00', false, 700.00),
  (11, '2023-09-15 20:00:00', true, 950.00),
  (12, '2023-09-15 21:00:00', false, 600.00),
  (13, '2023-09-15 22:00:00', true, 450.00),
  (14, '2023-09-15 23:00:00', false, 850.00),
  (15, '2023-09-16 10:00:00', true, 1100.00);
-- Insertar 15 registros ficticios en la tabla DETALLE_VENTAS
INSERT INTO DETALLE_VENTAS (id_venta_fk, id_producto_fk, cantidad_producto, subtotal)
VALUES
  (1, 1, 5, 250.00),
  (1, 2, 3, 150.00),
  (2, 3, 6, 300.00),
  (2, 4, 4, 200.00),
  (3, 5, 2, 100.00),
  (3, 6, 4, 200.00),
  (4, 7, 7, 350.00),
  (4, 8, 5, 250.00),
  (5, 9, 3, 150.00),
  (5, 10, 8, 400.00),
  (6, 11, 4, 200.00),
  (6, 12, 6, 300.00),
  (7, 13, 9, 450.00),
  (7, 14, 3, 150.00),
  (8, 15, 5, 250.00);
INSERT INTO PROVEEDORES (id_persona_fk, id_sucursal_fk, id_producto_fk)
VALUES
  (1, 1, 1),
  (2, 2, 2),
  (3, 3, 3),
  (4, 4, 4),
  (5, 5, 5),
  (6, 6, 6),
  (7, 7, 7),
  (8, 8, 8),
  (9, 9, 9),
  (10, 10, 10),
  (11, 11, 11),
  (12, 12, 12),
  (13, 13, 13),
  (14, 14, 14),
  (15, 15, 15);

