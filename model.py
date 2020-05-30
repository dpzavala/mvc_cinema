from mysql import connector

class Model:
    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close()
    

    """
	*************************
	* Métodos para Usuarios *
	*************************
	"""

    def create_usuario(self, nombre, apelliop, apellidom, correo, telefono, password, tipo):
        try:
            sql = 'INSERT INTO usuarios (`u_nombre`, `u_apellidop`, `u_apellidom`, `u_correo`, `u_telefono`, `u_password`, `u_tipo`) VALUES (%s, %s, %s, %s, %s, %s, %s)'
            vals = (nombre, apelliop,apellidom,correo,telefono,password,tipo)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_usuario(self, id_usuario):
        try:
            sql = 'SELECT * FROM usuarios WHERE id_usuario = %s'
            vals = (id_usuario,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_all_usuarios(self):
        try:
            sql = 'SELECT * FROM usuarios'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_usuarios_tipo(self, tipo):
        try:
            sql = ('SELECT * FROM usuarios WHERE u_tipo = %s')
            vals = (tipo,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def update_usuarios(self, fields, vals):
        try:
            sql = 'UPDATE usuarios SET '+','.join(fields)+' WHERE id_usuario = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

 
    
    def delete_usuario(self, id_usuario):
        try:
            sql = 'DELETE FROM usuarios WHERE id_usuario = %s'
            vals = (id_usuario,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    """
	**************************
	* Métodos para Peliculas *
	**************************
	"""           
    
    def create_pelicula(self, titulo, duracion, clasificacion, sipnosis, formato, idioma,  director, actores):
        try:
            sql = 'INSERT INTO peliculas (`p_titulo` , `p_duracion`, `p_clasificacion`, `p_sipnosis`, `p_formato`, `p_idioma`, `p_director`, `p_actores`) VALUES (%s, %s,  %s, %s, %s, %s, %s, %s)'
            vals = (titulo, duracion, clasificacion, sipnosis, formato, idioma, director, actores)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_pelicula(self, id_pelicula):
        try:
            sql = 'SELECT * FROM peliculas WHERE id_pelicula = %s'
            vals = (id_pelicula,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_all_peliculas(self):
        try:
            sql = 'SELECT * FROM peliculas'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_peliculas_clasificacion(self, clasificacion):
        try:
            sql = ('SELECT * FROM peliculas WHERE p_clasificacion = %s')
            vals = (clasificacion,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
            
    def update_peliculas(self, fields, vals):
        try:
            sql = 'UPDATE peliculas SET '+','.join(fields)+' WHERE id_pelicula = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_pelicula(self, id_pelicula):
        try:
            sql = 'DELETE FROM peliculas WHERE id_pelicula = %s'
            vals = (id_pelicula,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
	**************************
	* Métodos para Asientos *
	**************************
	"""
            
    
    def create_asiento(self, status):
        try:
            sql = 'INSERT INTO asientos (`a_status`) VALUES (%s)'
            vals = (status)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_asiento(self, id_asiento):
        try:
            sql = 'SELECT * FROM asientos WHERE id_asiento = %s'
            vals = (id_asiento,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_all_asientos(self):
        try:
            sql = 'SELECT * FROM asientos'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_asientos_disponibles(self, status = 'disponible'):
        try:
            sql = ('SELECT * FROM asientos WHERE a_status = %s')
            vals = (status,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
            
    def update_asientos(self, fields, vals):
        try:
            sql = 'UPDATE asientos SET '+','.join(fields)+' WHERE id_asiento = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_asiento(self, id_asiento):
        try:
            sql = 'DELETE FROM asientos WHERE id_asiento = %s'
            vals = (id_asiento,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
	*********************
	* Métodos para Salas*
	*********************
	"""
    def create_sala(self, total_asientos, status):
        try:
            sql = 'INSERT INTO salas (`s_atotal` , `s_status`) VALUES (%s, %s)'
            vals = (total_asientos, status)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_sala(self, id_sala):
        try:
            sql = 'SELECT * FROM salas WHERE id_sala = %s'
            vals = (id_sala,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_all_salas(self):
        try:
            sql = 'SELECT * FROM salas'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_salas_disponibles(self, status = 'disponible'):
        try:
            sql = ('SELECT * FROM salas WHERE s_status = %s')
            vals = (status,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
            
    def update_salas(self, fields, vals):
        try:
            sql = 'UPDATE salas SET '+','.join(fields)+' WHERE id_sala = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_sala(self, id_sala):
        try:
            sql = 'DELETE FROM salas WHERE id_sala = %s'
            vals = (id_sala,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    """
	*************************
	* Métodos para Horarios *
	*************************
	"""

    def create_horario(self, sala, pelicula, fecha, hora):
        try:
            sql = 'INSERT INTO horarios (`id_sala` , `id_pelicula`, `h_fecha`, `h_hora`) VALUES (%s, %s, %s, %s)'
            vals = (sala, pelicula, fecha, hora)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_horario(self, id_horario):
        try:
            sql = 'SELECT * FROM horarios WHERE id_horario = %s'
            vals = (id_horario,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_all_horarios(self):
        try:
            sql = 'SELECT * FROM horarios'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_horario_fecha(self, fecha):
        try:
            sql = ('SELECT * FROM horarios WHERE h_fecha = %s')
            vals = (fecha,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
            
    def update_horario(self, fields, vals):
        try:
            sql = 'UPDATE horarios SET '+','.join(fields)+' WHERE id_horario = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_horario(self, id_horario):
        try:
            sql = 'DELETE FROM horarios WHERE id_horario = %s'
            vals = (id_horario,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
	************************
	* Métodos para Boletos *
	************************
	"""


    def create_boleto(self, usuario, pelicula, sala, asiento, fecha, hora):
        try:
            sql = 'INSERT INTO boletos (`id_usuario` , `id_pelicula`, `id_sala`, `id_asiento`, `b_fecha`, `b_hora`) VALUES (%s, %s, %s, %s, %s, %s)'
            vals = (usuario, pelicula, sala, asiento, fecha, hora)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_boleto(self, id_boleto):
        try:
            sql = 'SELECT * FROM boletos WHERE id_boleto = %s'
            vals = (id_boleto,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_all_boletos(self):
        try:
            sql = 'SELECT * FROM boletos'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_boletos_fecha(self, fecha):
        try:
            sql = ('SELECT * FROM boletos WHERE b_fecha = %s')
            vals = (fecha,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_boletos_usuario_fecha(self, usuario, fecha):
        try:
            sql = ('SELECT * FROM boletos WHERE id_usuario = %s AND b_fecha = %s')
            vals = (usuario,fecha)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_datos(self,horario):
        try:
            sql = 'SELECT id_sala, id_pelicula, h_hora FROM horarios WHERE id_horario = %s'
            vals = (horario,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err


            
    def update_boleto(self, fields, vals):
        try:
            sql = 'UPDATE boletos SET '+','.join(fields)+' WHERE id_boleto = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_boleto(self, id_boleto):
        try:
            sql = 'DELETE FROM boletos WHERE id_boleto = %s'
            vals = (id_boleto,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def validar_usuario(self, correo, password):
        try:
            sql = 'SELECT u_tipo FROM usuarios WHERE u_correo = %s AND u_password = %s'
            vals = (correo, password)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err 
