--
-- File generated with SQLiteStudio v3.2.1 on mar. dic. 22 14:40:01 2020
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Usuarios
CREATE TABLE Usuarios (
    id        INTEGER PRIMARY KEY,
    nombre    STRING,
    apellidos STRING,
    usuario   STRING,
    correo    STRING,
    clave     STRING
);
INSERT INTO Usuarios (id, nombre, apellidos, usuario, correo, clave) VALUES (1, 'Karol', 'Gomez Rios', 'Karolgoodzy', 'karol@uninorte.edu.co', 24680000);
INSERT INTO Usuarios (id, nombre, apellidos, usuario, correo, clave) VALUES (2, 'Andres', 'Rojas Sandoval', 'afrsgithub', 'andres@uninorte.edu.co', 54321234);
INSERT INTO Usuarios (id, nombre, apellidos, usuario, correo, clave) VALUES (3, 'Cristian', 'Vitola Angulo', 'chrissvian', 'cristian@uninorte.edu.co', 12345432);
INSERT INTO Usuarios (id, nombre, apellidos, usuario, correo, clave) VALUES (4, 'Maria', 'Lopez', 'marilo', 'maria@uninorte.edu.co', 99990000);
INSERT INTO Usuarios (id, nombre, apellidos, usuario, correo, clave) VALUES (5, 'carlos', 'Sanchez', 'carlosa', 'carlosa@uninorte.edu.co', 45678900);
INSERT INTO Usuarios (id, nombre, apellidos, usuario, correo, clave) VALUES (6, 'Cristian', 'vitola Angulo', 'chrissvian', 'chriss.vian@gmail.com', 12345678);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
