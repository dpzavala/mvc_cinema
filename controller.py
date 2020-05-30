from model.model import Model
from view.view import View
from mysql import connector

class Controller:
	def __init__(self):
		self.model = Model()
		self.view = View()
		
	def start(self):
		self.view.start()
		validacion = self.validar_usuario()
		if validacion == 'normal':
			self.sub_menu()
		elif validacion == 'administrador':
			self.main_menu()
		else:
			self.view.msg('Error con el usuario')
		# self.view.start()
		# self.main_menu()
		return
	
	
	def main_menu(self):
		o = '0'
		while o != '8':
			self.view.main_menu()
			self.view.option('8')
			o = input()
			if o == '1':
				self.usuarios_menu()
			elif o == '2':
				self.peliculas_menu()
			elif o == '3':
				self.asientos_menu()
			elif o == '4':
				self.salas_menu()
			elif o == '5':
				self.horarios_menu()
			elif o == '6':
				self.boletos_menu()
			elif o == '7':
				self.comprar_boleto()
			elif o == '8':
				self.view.end()
			else:
				self.view.not_valid_option()
		return
	
	def sub_menu(self):
		o = '0'
		while o != '3':
			self.view.sub_menu()
			self.view.option('3')
			o = input()
			if o == '1':
				self.read_all_horarios()
			elif o == '2':
				self.comprar_boleto()
			elif o == '3':
				self.view.end()
			else:
				self.view.not_valid_option()
		return

	def update_lists(self, fs, vs):
		fields = []
		vals = []
		for f,v in zip(fs,vs):
			if v!= '':
				fields.append(f+' = %s')
				vals.append(v)
		return fields,vals
		
	def ask_usuario(self):
		self.view.ask('Nombre: ')
		nombre = input()
		self.view.ask('A.Paterno: ')
		apellidop = input()
		self.view.ask('A.Materno: ')
		apellidom = input()
		self.view.ask('Correo: ')
		correo = input()
		self.view.ask('Telefono: ')
		telefono = input()
		self.view.ask('Contraseña: ')
		contraseña = input()
		self.view.ask('Tipo: ')
		tipo = input()
		return[nombre, apellidop, apellidom, correo, telefono, contraseña, tipo]

	def usuarios_menu(self):
		o = '0'
		while o != '7':
			self.view.usuarios_menu()
			self.view.option('7')
			o = input()
			if o == '1':
				self.create_usuario()
			elif o == '2':
				self.read_usuario()
			elif o == '3':
				self.read_all_usuarios()
			elif o == '4':
				self.read_usuarios_tipo()
			elif o == '5':
				self.update_usuario()
			elif o == '6':
				self.delete_usuario()
			elif o == '7':
				return
			else:
				self.view.not_valid_option()
		return
        
               



	def create_usuario(self):
		nombre, apellidop, apellidom, correo, telefono, contraseña, tipo = self.ask_usuario()
		out = self.model.create_usuario(nombre, apellidop, apellidom, correo, telefono, contraseña, tipo)
		if out == True:
			self.view.ok(nombre+' '+apellidop, ' agrego a la base de datos')
		else:
			self.view.error('No se pudo agregar Usuario. Verifica los datos')
		return

	def read_usuario(self):
		self.view.ask('ID_Usuario: ')
		id_usuario = input()
		usuario = self.model.read_usuario(id_usuario)
		if type(usuario) == tuple:
			self.view.show_usuario_header('  Datos del Usuario '+id_usuario+' ')
			self.view.show_usuario(usuario)
			self.view.show_usuario_midder()
			self.view.show_usuario_footer()
		else:
			if usuario == None:
				self.view.error('EL USUARIO NO EXISTE')
			else:
				self.view.error('PROBLEMA AL LEER USUARIO. VERIFICA LA INFORMACION.')
		return

	def read_all_usuarios(self):
		usuarios = self.model.read_all_usuarios()
		if type(usuarios) == list:
			self.view.show_usuario_header('  Todos los Usuarios Registrados  ')
			for usuario in usuarios:
				self.view.show_usuario(usuario)
			self.view.show_usuario_midder()
			self.view.show_usuario_footer()
		else:
			self.view.error('PROBLEMA AL LEER LOS USUARIOS. VERIFICA LA INFORMACION.')
		return

	def read_usuarios_tipo(self):
		self.view.ask('Tipo de Usuario (Normal/Administrador):')
		tipo = input()
		usuarios = self.model.read_usuarios_tipo(tipo)
		if type(usuarios) == list:
			self.view.show_usuario_header(' Usuarios del Tipo '+tipo+' ')
			for usuario in usuarios:
				self.view.show_usuario(usuario)
			self.view.show_usuario_midder()
			self.view.show_usuario_footer()
		else:
			self.view.error('PROBLEMA al LEER LOS USUARIOS. VERIFICA LA INFORMACION.')
		return

	def update_usuario(self):
		self.view.ask('ID del Usario a modificar: ')
		id_usuario = input()
		usuario = self.model.read_usuario(id_usuario)
		if type(usuario) == tuple:
			self.view.show_usuario_header('Datos del Usuario'+id_usuario+' ')
			self.view.show_usuario(usuario)
			self.view.show_usuario_midder()
			self.view.show_usuario_footer()
		else:
			if usuario == None:
				self.view.error('El Usuario no existe')
			else:
				self.view.error('Problemas al leer el Usuario, Verificar informacion')
			return
		self.view.msg('Ingresa los valores a modificar:(vacio para dejarlo igual)')
		whole_vals = self.ask_usuario()
		fields, vals = self.update_lists(['u_nombre','u_apellidop','u_apellidom','u_correo','u_telefono','u_password','u_tipo'], whole_vals)
		vals.append(id_usuario)
		vals = tuple(vals)
		out = self.model.update_usuarios(fields, vals)
		if out == True:
			self.view.ok(id_usuario, 'actualizo')
		else:
			self.view.error('No se pudo actualizar el Usuario. Verifica la informacion')
		return

	def delete_usuario(self):
		self.view.ask('ID_Usuario a borrar: ')
		id_usuario = input()
		count = self.model.delete_usuario(id_usuario)
		if count !=0:
			self.view.ok(id_usuario, 'borro')
		else:
			if count == 0:
				self.view.error('El Usuario no existe')
			else:
				self.view.error('Problemas al leer el Usuario. REVISA')
		return

	def peliculas_menu(self):
		o = '0'
		while o != '7':
			self.view.peliculas_menu()
			self.view.option('7')
			o = input()
			if o == '1':
				self.create_pelicula()
			elif o == '2':
				self.read_pelicula()
			elif o == '3':
				self.read_all_peliculas()
			elif o == '4':
				self.read_peliculas_clasificacion()
			elif o == '5':
				self.update_pelicula()
			elif o == '6':
				self.delete_pelicula()
			elif o == '7':
				return
			else:
				self.view.not_valid_option()
		return
	
	def ask_pelicula(self):
		self.view.ask('Titulo: ')
		titulo = input()
		self.view.ask('Duracion (minutos): ')
		duracion = input()
		self.view.ask('Clasificacion: ')
		clasificacion = input()
		self.view.ask('Sipnosis: ')
		sipnosis = input()
		self.view.ask('Formato: ')
		formato = input()
		self.view.ask('Idioma: ')
		idioma = input()
		# self.view.ask('Fecha de Lanzamiento: ')
		# fecha_lanzamiento = input()
		self.view.ask('Director: ')
		director = input()
		self.view.ask('Actores: ')
		actores = input()
		return[titulo, duracion, clasificacion, sipnosis, formato, idioma, director, actores]


	def create_pelicula(self):
		titulo, duracion, clasificacion, sipnosis, formato, idioma, director, actores = self.ask_pelicula()
		out = self.model.create_pelicula(titulo, duracion, clasificacion, sipnosis, formato, idioma, director, actores)
		if out == True:
			self.view.ok(titulo, ' se agrego a la base de datos')
		else:
			self.view.error('No se pudo agregar Pelicula. Verifica los datos')
		return

	def read_pelicula(self):
		self.view.ask('ID_pelicula: ')
		id_pelicula = input()
		pelicula = self.model.read_pelicula(id_pelicula)
		if type(pelicula) == tuple:
			self.view.show_pelicula_header('  Datos de la Pelicula '+id_pelicula+' ')
			self.view.show_pelicula(pelicula)
			self.view.show_pelicula_midder()
			self.view.show_pelicula_footer()
		else:
			if pelicula == None:
				self.view.error('LA PELICULA NO EXISTE')
			else:
				self.view.error('PROBLEMA AL LEER PELICULA. VERIFICA LA INFORMACION.')
		return

	def read_all_peliculas(self):
		peliculas = self.model.read_all_peliculas()
		if type(peliculas) == list:
			self.view.show_pelicula_header('  Todos las Peiculas Registradas  ')
			for pelicula in peliculas:
				self.view.show_pelicula(pelicula)
			self.view.show_pelicula_midder()
			self.view.show_pelicula_footer()
		else:
			self.view.error('PROBLEMA AL LEER LAS PELICULAS. VERIFICA LA INFORMACION.')
		return

	def read_peliculas_clasificacion(self):
		self.view.ask('Tipo de Pelicula:')
		clasificacion = input()
		peliculas = self.model.read_peliculas_clasificacion(clasificacion)
		if type(peliculas) == list:
			self.view.show_pelicula_header('Peliculas del Tipo '+clasificacion+' ')
			for pelicula in peliculas:
				self.view.show_pelicula(pelicula)
			self.view.show_pelicula_midder()
			self.view.show_pelicula_footer()
		else:
			self.view.error('PROBLEMA al LEER LAS PELICULAS. VERIFICA LA INFORMACION.')
		return

	def update_pelicula(self):
		self.view.ask('ID de la Pelicula a modificar: ')
		id_pelicula = input()
		pelicula = self.model.read_pelicula(id_pelicula)
		if type(pelicula) == tuple:
			self.view.show_pelicula_header('Datos de la Pelicula'+id_pelicula+' ')
			self.view.show_pelicula(pelicula)
			self.view.show_pelicula_midder()
			self.view.show_pelicula_footer()
		else:
			if pelicula == None:
				self.view.error('La Pelicula no existe')
			else:
				self.view.error('Problemas al leer la Pelicula, Verificar informacion')
			return
		self.view.msg('Ingresa los valores a modificar:(vacio para dejarlo igual)')
		whole_vals = self.ask_pelicula()
		fields, vals = self.update_lists(['p_titulo','p_duracion','p_clasificacion','p_sipnosis','p_formato','p_idioma','p_fecha_lanzamiento', 'p_director', 'p_actores'], whole_vals)
		vals.append(id_pelicula)
		vals = tuple(vals)
		out = self.model.update_peliculas(fields, vals)
		if out == True:
			self.view.ok(id_pelicula, 'actualizo')
		else:
			self.view.error('No se pudo actualizar la pelicula. Verifica la informacion')
		return

	def delete_pelicula(self):
		self.view.ask('ID_Pelicula a borrar: ')
		id_pelicula = input()
		count = self.model.delete_pelicula(id_pelicula)
		if count !=0:
			self.view.ok(id_pelicula, 'borro')
		else:
			if count == 0:
				self.view.error('La pelicula no existe')
			else:
				self.view.error('Problemas al leer la Pelicula. REVISA')
		return
    
	def asientos_menu(self):
		o = '0'
		while o != '7':
			self.view.asientos_menu()
			self.view.option('7')
			o = input()
			if o == '1':
				self.create_asiento()
			elif o == '2':
				self.read_asiento()
			elif o == '3':
				self.read_all_asientos()
			elif o == '4':
				self.read_asientos_disponibles()
			elif o == '5':
				self.update_asiento()
			elif o == '6':
				self.delete_asiento()
			elif o == '7':
				return
			else:
				self.view.not_valid_option()
		return
		
	def ask_asiento(self):
		self.view.ask('Disponibilidad: ')
		status = input()
		return[status]


	def create_asiento(self):
		status = self.ask_asiento()
		out = self.model.create_asiento(status)
		if out == True:
			self.view.ok(status,'Nuevo asiento se agrego a la base de datos')
		else:
			self.view.error('No se pudo agregar Asiento. Verifica los datos')
		return

	def read_asiento(self):
		self.view.ask('ID_Asiento: ')
		id_asiento = input()
		asiento = self.model.read_asiento(id_asiento)
		if type(asiento) == tuple:
			self.view.show_asiento_header('  Datos del Usuario '+id_asiento+' ')
			self.view.show_asiento(asiento)
			self.view.show_asiento_midder()
			self.view.show_asiento_footer()
		else:
			if asiento == None:
				self.view.error('EL ASIENTO NO EXISTE')
			else:
				self.view.error('PROBLEMA AL LEER INFORMACION DE ASIENTO. VERIFICA LA INFORMACION.')
		return

	def read_all_asientos(self):
		asientos = self.model.read_all_asientos()
		if type(asientos) == list:
			self.view.show_asiento_header('  Todos los Asientos Registrados  ')
			for asiento in asientos:
				self.view.show_asiento(asiento)
			self.view.show_asiento_midder()
			self.view.show_asiento_footer()
		else:
			self.view.error('PROBLEMA AL LEER LOS ASIENTOS. VERIFICA LA INFORMACION.')
		return

	def read_asientos_disponibles(self):
		status = 'disponible'
		asientos = self.model.read_asientos_disponibles(status)
		if type(asientos) == list:
			self.view.show_asiento_header(' Asientos '+status+' ')
			for asiento in asientos:
				self.view.show_asiento(asiento)
			self.view.show_asiento_midder()
			self.view.show_asiento_footer()
		else:
			self.view.error('PROBLEMA AL LEER LOS ASIENTOS. VERIFICA LA INFORMACION.')
		return

	def update_asiento(self):
		self.view.ask('ID del Asiento a modificar: ')
		id_asiento = input()
		asiento = self.model.read_asiento(id_asiento)
		if type(asiento) == tuple:
			self.view.show_asiento_header('Datos del Asiento'+id_asiento+' ')
			self.view.show_asiento(asiento)
			self.view.show_asiento_midder()
			self.view.show_asiento_footer()
		else:
			if asiento == None:
				self.view.error('El Asiento no existe')
			else:
				self.view.error('Problemas al leer informaciond de asiento, Verificar informacion')
			return
		self.view.msg('Ingresa los valores a modificar:(vacio para dejarlo igual)')
		whole_vals = self.ask_asiento()
		fields, vals = self.update_lists(['a_status'], whole_vals)
		vals.append(id_asiento)
		vals = tuple(vals)
		out = self.model.update_asientos(fields, vals)
		if out == True:
			self.view.ok(id_asiento, 'actualizo')
		else:
			self.view.error('No se pudo actualizar el Asiento. Verifica la informacion')
		return

	def delete_asiento(self):
		self.view.ask('ID_Asiento a borrar: ')
		id_asiento = input()
		count = self.model.delete_asiento(id_asiento)
		if count !=0:
			self.view.ok(id_asiento, 'borro')
		else:
			if count == 0:
				self.view.error('El Asiento no existe')
			else:
				self.view.error('Problemas al leer el Asiento. REVISA')
		return
    


	def salas_menu(self):
		o = '0'
		while o != '7':
			self.view.salas_menu()
			self.view.option('7')
			o = input()
			if o == '1':
				self.create_sala()
			elif o == '2':
				self.read_sala()
			elif o == '3':
				self.read_all_salas()
			elif o == '4':
				self.read_salas_disponibles()
			elif o == '5':
				self.update_sala()
			elif o == '6':
				self.delete_sala()
			elif o == '7':
				return
			else:
				self.view.not_valid_option()
		return
	
	
	def ask_sala(self):
		self.view.ask('Total Asientos: ')
		atotal = input()
		self.view.ask('Disponibilidad: ')
		status = input()
		return[atotal, status]


	def create_sala(self):
		atotal, status = self.ask_sala()
		out = self.model.create_sala(atotal, status)
		if out == True:
			self.view.ok(status, 'La sala se agrego a la base de datos')
		else:
			self.view.error('No se pudo agregar Sala. Verifica los datos')
		return

	def read_sala(self):
		self.view.ask('ID_Sala: ')
		id_sala = input()
		sala = self.model.read_sala(id_sala)
		if type(sala) == tuple:
			self.view.show_sala_header('  Datos de la sala '+id_sala+' ')
			self.view.show_sala(sala)
			self.view.show_sala_midder()
			self.view.show_sala_footer()
		else:
			if sala == None:
				self.view.error('LA SALA NO EXISTE')
			else:
				self.view.error('PROBLEMA AL LEER SALA. VERIFICA LA INFORMACION.')
		return

	def read_all_salas(self):
		salas = self.model.read_all_salas()
		if type(salas) == list:
			self.view.show_sala_header('  Todos las Salas Registradas  ')
			for sala in salas:
				self.view.show_sala(sala)
			self.view.show_sala_midder()
			self.view.show_sala_footer()
		else:
			self.view.error('PROBLEMA AL LEER LA SALA. VERIFICA LA INFORMACION.')
		return

	def read_salas_disponibles(self):
		status = 'disponible'
		salas = self.model.read_salas_disponibles(status)
		if type(salas) == list:
			self.view.show_sala_header(' Salas Disponibles ')
			for sala in salas:
				self.view.show_sala(sala)
			self.view.show_sala_midder()
			self.view.show_sala_footer()
		else:
			self.view.error('PROBLEMA al LEER LAS SALAS. VERIFICA LA INFORMACION.')
		return

	def update_sala(self):
		self.view.ask('ID de la Sala a modificar: ')
		id_sala = input()
		sala = self.model.read_sala(id_sala)
		if type(sala) == tuple:
			self.view.show_sala_header('Datos de la Sala'+id_sala+' ')
			self.view.show_sala(sala)
			self.view.show_sala_midder()
			self.view.show_sala_footer()
		else:
			if sala == None:
				self.view.error('La sala no existe')
			else:
				self.view.error('Problemas al leer la Sala, Verificar informacion')
			return
		self.view.msg('Ingresa los valores a modificar:(vacio para dejarlo igual)')
		whole_vals = self.ask_sala()
		fields, vals = self.update_lists(['s_atota','s_status'], whole_vals)
		vals.append(id_sala)
		vals = tuple(vals)
		out = self.model.update_salas(fields, vals)
		if out == True:
			self.view.ok(id_sala, 'actualizo')
		else:
			self.view.error('No se pudo actualizar la Sala. Verifica la informacion')
		return

	def delete_sala(self):
		self.view.ask('ID_Sala a borrar: ')
		id_sala = input()
		count = self.model.delete_sala(id_sala)
		if count !=0:
			self.view.ok(id_sala, 'borro')
		else:
			if count == 0:
				self.view.error('La Sala no existe')
			else:
				self.view.error('Problemas al leer la Sala. Revisa Informacion')
		return

	def horarios_menu(self):
		o = '0'
		while o != '7':
			self.view.horarios_menu()
			self.view.option('7')
			o = input()
			if o == '1':
				self.create_horario()
			elif o == '2':
				self.read_horario()
			elif o == '3':
				self.read_all_horarios()
			elif o == '4':
				self.read_horarios_fecha(fecha='2020-05-31')
			elif o == '5':
				self.update_horario()
			elif o == '6':
				self.delete_horario()
			elif o == '7':
				return
			else:
				self.view.not_valid_option()
		return
	
	
	def ask_horario(self):
		self.view.ask('Sala (ID): ')
		sala = input()
		self.view.ask('Pelicula (ID): ')
		pelicula = input()
		self.view.ask('Fecha: ')
		fecha = input()
		self.view.ask('Hora: ')
		hora = input()
		return[sala, pelicula, fecha, hora]


	def create_horario(self):
		sala, pelicula, fecha, hora = self.ask_horario()
		out = self.model.create_horario(sala, pelicula, fecha, hora)
		if out == True:
			self.view.ok(sala, 'El horario agrego a la base de datos')
		else:
			self.view.error('No se pudo agregar Horario. Verifica los datos')
		return

	def read_horario(self):
		self.view.ask('ID_Horario: ')
		id_horario = input()
		horario = self.model.read_horario(id_horario)
		if type(horario) == tuple:
			self.view.show_horario_header('  Datos del Horario '+id_horario+' ')
			self.view.show_horario(horario)
			self.view.show_horario_midder()
			self.view.show_horario_footer()
		else:
			if horario == None:
				self.view.error('EL HORARIO NO EXISTE')
			else:
				self.view.error('PROBLEMA AL LEER HORARIO. VERIFICA LA INFORMACION.')
		return

	def read_all_horarios(self):
		horarios = self.model.read_all_horarios()
		if type(horarios) == list:
			self.view.show_horario_header('  Todos los Horarios Registrados  ')
			for horario in horarios:
				self.view.show_horario(horario)
			self.view.show_horario_midder()
			self.view.show_horario_footer()
		else:
			self.view.error('PROBLEMA AL LEER LOS HORARIOS. VERIFICA LA INFORMACION.')
		return

	def read_horarios_fecha(self, fecha):
		#self.view.ask('Fecha:')
		#fecha = input()
		horarios = self.model.read_horario_fecha(fecha)
		if type(horarios) == list:
			self.view.show_horario_header(' Horarios de la fecha '+fecha+' ')
			for horario in horarios:
				self.view.show_horario(horario)
			self.view.show_horario_midder()
			self.view.show_horario_footer()
		else:
			self.view.error('PROBLEMA al LEER LOS HORARIOS. VERIFICA LA INFORMACION.')
		return

	def update_horario(self):
		self.view.ask('ID del Horario a modificar: ')
		id_horario = input()
		horario = self.model.read_horario(id_horario)
		if type(horario) == tuple:
			self.view.show_horario_header('Datos del Horario'+id_horario+' ')
			self.view.show_horario(horario)
			self.view.show_horario_midder()
			self.view.show_horario_footer()
		else:
			if horario == None:
				self.view.error('El Horario no existe')
			else:
				self.view.error('Problemas al leer el Horario, Verificar informacion')
			return
		self.view.msg('Ingresa los valores a modificar:(vacio para dejarlo igual)')
		whole_vals = self.ask_horario()
		fields, vals = self.update_lists(['id_sala','id_pelicula','h_fecha','h_hora'], whole_vals)
		vals.append(id_horario)
		vals = tuple(vals)
		out = self.model.update_horario(fields, vals)
		if out == True:
			self.view.ok(id_horario, 'actualizo')
		else:
			self.view.error('No se pudo actualizar el Horario. Verifica la informacion')
		return

	def delete_horario(self):
		self.view.ask('ID_Horario a borrar: ')
		id_horario = input()
		count = self.model.delete_horario(id_horario)
		if count !=0:
			self.view.ok(id_horario, 'borro')
		else:
			if count == 0:
				self.view.error('El Horario no existe')
			else:
				self.view.error('Problemas al leer el Horario. REVISA')
		return
    


	def boletos_menu(self):
		o = '0'
		while o != '7':
			self.view.boletos_menu()
			self.view.option('7')
			o = input()
			if o == '1':
				self.create_boleto()
			elif o == '2':
				self.read_boleto()
			elif o == '3':
				self.read_all_boletos()
			elif o == '4':
				self.read_boletos_fecha()
			elif o == '5':
				self.update_boleto()
			elif o == '6':
				self.delete_boleto()
			elif o == '7':
				return
			else:
				self.view.not_valid_option()
		return
		
	def ask_boleto(self):
		self.view.ask('Usuario (ID): ')
		id_usuario = input()
		self.view.ask('Elige Pelicula (ID): ')
		id_pelicula = input()
		self.view.ask('Ingresa Sala del Horario (ID): ')
		id_sala = input()
		self.view.ask('Elige un Asiento (ID): ')
		id_asiento = input()
		self.view.ask('Fecha: ')
		fecha = input()
		self.view.ask('Hora: ')
		hora = input()
		return[id_usuario, id_pelicula, id_sala, id_asiento, fecha, hora]


	def create_boleto(self):
		id_usuario, id_pelicula, id_sala, id_asiento, fecha, hora = self.ask_boleto()
		out = self.model.create_boleto(id_usuario, id_pelicula, id_sala, id_asiento, fecha, hora)
		if out == True:
			self.view.ok(fecha, 'El boleto se agrego a la base de datos')
		else:
			self.view.error('No se pudo agregar Boleto. Verifica los datos')
		return

	def read_boleto(self):
		self.view.ask('ID_Boleto: ')
		id_boleto = input()
		boleto = self.model.read_boleto(id_boleto)
		if type(boleto) == tuple:
			self.view.show_boleto_header('  Datos del Boleto '+id_boleto+' ')
			self.view.show_boleto(boleto)
			self.view.show_boleto_midder()
			self.view.show_boleto_footer()
		else:
			if boleto == None:
				self.view.error('EL BOLETO NO EXISTE')
			else:
				self.view.error('PROBLEMA AL LEER BOLETO. VERIFICA LA INFORMACION.')
		return

	def read_all_boletos(self):
		boletos = self.model.read_all_boletos()
		if type(boletos) == list:
			self.view.show_boleto_header('  Todos los Boletos Registrados  ')
			for boleto in boletos:
				self.view.show_boleto(boleto)
			self.view.show_boleto_midder()
			self.view.show_boleto_footer()
		else:
			self.view.error('PROBLEMA AL LEER LOS BOLETOS. VERIFICA LA INFORMACION.')
		return

	def read_boletos_fecha(self):
		self.view.ask('Fecha:')
		fecha = input()
		boletos = self.model.read_boletos_fecha(fecha)
		if type(boletos) == list:
			self.view.show_boleto_header(' Boletos de la fecha '+fecha+' ')
			for boleto in boletos:
				self.view.show_boleto(boleto)
			self.view.show_boleto_midder()
			self.view.show_boleto_footer()
		else:
			self.view.error('PROBLEMA AL LEER LOS BOLETOS. VERIFICA LA INFORMACION.')
		return

	def read_boleto_usuario_fecha(self, usuario, fecha):
		boletos = self.model.read_boletos_usuario_fecha(usuario, fecha)
		if type(boletos) == list:
			self.view.show_boleto_header('Boletos Comprados')
			for boleto in boletos:
				self.view.show_boleto(boleto)
			self.view.show_boleto_midder()
			self.view.show_boleto_footer()
		else:
			self.view.error('PROBLEMA AL LEER LOS BOLETOS. VERIFICA LA INFORMACION.')
		return

	def update_boleto(self):
		self.view.ask('ID del Boleto a modificar: ')
		id_boleto = input()
		boleto = self.model.read_boleto(id_boleto)
		if type(boleto) == tuple:
			self.view.show_boleto_header('Datos del Boleto'+id_boleto+' ')
			self.view.show_boleto(boleto)
			self.view.show_boleto_midder()
			self.view.show_boleto_footer()
		else:
			if boleto == None:
				self.view.error('El Boleto no existe')
			else:
				self.view.error('Problemas al leer el Boleto, Verificar informacion')
			return
		self.view.msg('Ingresa los valores a modificar:(vacio para dejarlo igual)')
		whole_vals = self.ask_boleto()
		fields, vals = self.update_lists(['id_usuario','id_pelicula','id_sala','id_asiento','b_fecha','b_hora'], whole_vals)
		vals.append(id_boleto)
		vals = tuple(vals)
		out = self.model.update_boleto(fields, vals)
		if out == True:
			self.view.ok(id_boleto, 'actualizo')
		else:
			self.view.error('No se pudo actualizar el Boleto. Verifica la informacion')
		return

	def delete_boleto(self):
		self.view.ask('ID_Boleto a borrar: ')
		id_boleto = input()
		count = self.model.delete_boleto(id_boleto)
		if count !=0:
			self.view.ok(id_boleto, 'borro')
		else:
			if count == 0:
				self.view.error('El Boleto no existe')
			else:
				self.view.error('Problemas al leer el Boleto. REVISA')
		return

	def validar_usuario(self):
		self.view.ask('Ingrese su correo: ')
		correo = input()
		self.view.ask('Ingrese su contraseña: ')
		password = input()
		validacion = self.model.validar_usuario(correo, password)
		if type(validacion) == tuple:
			self.view.show_validacion_usuario(validacion)
			return validacion[0]
		else:
			self.view.error('Existe un problema con este usuario')
		return


	def comprar_boleto(self):
		self.view.ask('Ingrese su No de Usuario (ID): ')
		id_usuario = input ()
		self.view.ask('De que fecha quiere su boleto? (AAAA-MM-DD): ')
		fecha = input()
		self.read_horarios_fecha(fecha)
		#self.view.ask('Elige un horaraio (ID): ')
		#id_horario = input()
		self.read_asientos_disponibles()
		#self.view.ask('Elige un asiento: ')
		#id_asiento = input()
		self.create_boleto()
		self.read_boleto_usuario_fecha(id_usuario, fecha)
		return
		