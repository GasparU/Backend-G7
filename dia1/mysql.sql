CREATE DATABASE prueba;
-- USE prueba sirve para indicar que BD queremos trabajar
USE prueba;
CREATE TABLE productos(
-- Obligatoriamente para crear una tabla debemos debemos crear una columna
-- Solamente se puede usar UNA VEZ el auto_increment por tabla
-- primary key > indicaremos que esta columna se comporta como la identificadora de todo este registro.
-- Nombre | Tipo de Dato | [configuraciones adicionales]
id INT auto_increment primary key,
nombre varchar(50),
fecha_vencimiento date
);