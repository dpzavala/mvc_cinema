#Definition of the schema fo the DB

#Create the DB
DROP DATABASE IF EXISTS cine_db;
CREATE DATABASE IF NOT EXISTS cine_db;

#Select the database to work with
USE cine_db;

#Create the kernel tables
CREATE TABLE IF NOT EXISTS usuarios(
id_usuario int NOT NULL AUTO_INCREMENT,
u_nombre VARCHAR(35) NOT NULL,
u_apellidop VARCHAR(35) NOT NULL,
u_apellidom VARCHAR(35),
u_correo VARCHAR(35) NOT NULL,
u_telefono VARCHAR(35),
u_password VARCHAR(35) NOT NULL,
u_tipo VARCHAR(20) NOT NULL,
PRIMARY KEY(id_usuario)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS salas(
id_sala INT NOT NULL AUTO_INCREMENT,
s_atotal VARCHAR(20) NOT NULL,
s_status VARCHAR(20) NOT NULL,
PRIMARY KEY(id_sala)
) ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS peliculas(
id_pelicula int NOT NULL AUTO_INCREMENT,
p_titulo VARCHAR(35) NOT NULL,
p_duracion VARCHAR(35) NOT NULL,
p_clasificacion VARCHAR(35),
p_sipnosis VARCHAR(250) NOT NULL,
p_formato VARCHAR(10) NOT NULL,
p_idioma VARCHAR(20) NOT NULL,
p_director VARCHAR(54) NOT NULL,
p_actores VARCHAR(54) NOT NULL,
PRIMARY KEY(id_pelicula)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS asientos(
id_asiento int NOT NULL AUTO_INCREMENT,
a_status VARCHAR(20) NOT NULL,
PRIMARY KEY(id_asiento)
)ENGINE = InnoDB;



#CREATE the dependent tables
CREATE TABLE IF NOT EXISTS horarios(
id_horario INT NOT NULL AUTO_INCREMENT,
id_sala INT NOT NULL,
id_pelicula INT NOT NULL,
h_fecha DATE NOT NULL,
h_hora VARCHAR(20) NOT NULL,
PRIMARY KEY(id_horario),
CONSTRAINT fkpelicula_hp FOREIGN KEY(id_pelicula)
	REFERENCES peliculas(id_pelicula)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
CONSTRAINT fksala_hp FOREIGN KEY(id_sala)
	REFERENCES salas(id_sala)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS boletos(
id_boleto INT NOT NULL AUTO_INCREMENT,
id_usuario INT NOT NULL,
id_pelicula INT NOT NULL,
id_sala INT NOT NULL,
id_asiento INT NOT NULL,
b_fecha DATE NOT NULL,
b_hora VARCHAR(20) NOT NULL,
PRIMARY KEY(id_boleto),
CONSTRAINT fkusuario_bu FOREIGN KEY(id_usuario)
	REFERENCES usuarios(id_usuario)
	ON DELETE CASCADE
	ON UPDATE CASCADE,
CONSTRAINT fkpelicula_bp FOREIGN KEY(id_pelicula)
	REFERENCES peliculas(id_pelicula)
	ON DELETE CASCADE
    ON UPDATE CASCADE,
CONSTRAINT fksala_bs FOREIGN KEY(id_sala)
	REFERENCES salas(id_sala)
	ON DELETE CASCADE
    ON UPDATE CASCADE,
CONSTRAINT fkasiento_ba FOREIGN KEY(id_asiento)
	REFERENCES asientos(id_asiento)
	ON DELETE CASCADE
    ON UPDATE CASCADE
)ENGINE = InnoDB;
