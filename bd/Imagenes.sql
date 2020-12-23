--
-- File generated with SQLiteStudio v3.2.1 on mar. dic. 22 14:38:31 2020
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Imagenes
CREATE TABLE Imagenes (
    id                  INTEGER PRIMARY KEY,
    usuarios_id         INTEGER REFERENCES usuarios (id) ON DELETE RESTRICT,
    name_image          STRING,
    tipo                INTEGER,
    fecha_subida        STRING,
    fecha_actualizacion STRING
);
INSERT INTO Imagenes (id, usuarios_id, name_image, tipo, fecha_subida, fecha_actualizacion) VALUES (1, 2, 'imagen1', 'publica', '12/05/2017', '12/05/2017');
INSERT INTO Imagenes (id, usuarios_id, name_image, tipo, fecha_subida, fecha_actualizacion) VALUES (2, 3, 'imagen2', 'privada', '24/08/2018', '09/09/2018');
INSERT INTO Imagenes (id, usuarios_id, name_image, tipo, fecha_subida, fecha_actualizacion) VALUES (3, 1, 'imagen3', 'privada', '07/03/2012', '20/05/2019');
INSERT INTO Imagenes (id, usuarios_id, name_image, tipo, fecha_subida, fecha_actualizacion) VALUES (4, 2, 'imagen4', 'publica', '11/01/2015', '21/07/2020');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
