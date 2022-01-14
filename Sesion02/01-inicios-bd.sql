CREATE DATABASE pruebas;

CREATE TABLE personas(
	-- Ahora definimos las columnas pertenecientes a esta tabla
    id INT, --solamente se podran almacenar numeros
    nombre VARCHAR(100), --se podran almacenar caracteres hasta 100 como máximo
    dni CHAR(8), --suempre se almacenaran 8 caracteres
    fecha_nacimiento DATE, --seran solamente fecha
    created_at DATETIME, --sera fecha y hora, minuto, segundo
    sexo ENUM('Masculino','FEMENINO','otro','HELICOPTERO'), --solamente podra tener los valores definidos en el paréntesis
    estado BOOL --solo true o false
);