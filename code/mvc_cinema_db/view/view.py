class View:
	
	def start(self):
		print('=============================================================')
		print('| ¡Bienvenido a a nuestro Cine, gracias por tu preferencia! |')
		print('=============================================================')
		
	def end(self):
		print('=================================')
		print('|       ¡Vuelve pronto!         |')
		print('=================================')
		
	def main_menu(self):
		print('***************************************************')
		print('* -- Elige alguna a que seccion quieres acceder-- *')
		print('***************************************************')
		print('1. Usuarios')
		print('2. Peliculas')
		print('3. Asientos')
		print('4. Salas')
		print('5. Horarios')
		print('6. Boletos')
		print('7. Comprar Boleto')
		print('8. Salir')

	def sub_menu(self):
		print('*******************************************')
		print('* -- Eige a que seccion quieres acceder-- *')
		print('*******************************************')
		print('1.- Ver Horarios')
		print('2.- Comprar Boleto')
		print('3.- Salir')



	def option(self, last):
		print('Seleciona una opcion (1-'+last+'):', end = '')

	def not_valid_option(self):
		print('¡Opcion no valida!\nIntenta de nuevo')

	def ask(self, output):
		print(output, end = '')

	def msg(self, output):
		print(output)

	def ok(self, id, op):
		print('+'*(len(str(id))+len(op)+24))
		print('+ ¡'+str(id)+' se '+op+' correctamente! +')
		print('+'*(len(str(id))+len(op)+24))

	def error(self, err):
		print('  ¡ERROR!  '.center(len(err)+4,'-'))
		print('- '+err+' -')
		print('-'*(len(err)+4))

	"""
	************************
	* Vistas de Usuarios *
	************************
	"""
	def usuarios_menu(self):
		print('*****************************')
		print('* -- Submenu de Usuarios -- *')
		print('*****************************')
		print('1. Agregar Usuario')
		print('2. Mostrar un Usuario')
		print('3. Mostrar todos los Usuarios')
		print('4. Mostrar Usuarios de un tipo(Normal/Administrador)')
		print('5. Actualizar Usuario')
		print('6. Borrar Usuario')
		print('7. Regresar')

	def show_usuario(self, record):
		print('ID:', record[0])
		print('Nombre:', record[1])
		print('A.Paterno:', record[2])
		print('A.Marterno:', record[3])
		print('Correo:', record[4])
		print('Telefono:', record[5])
		print('Contraseña:', record[6])
		print('Tipo:', record[7])

	def show_usuario_header(self, header):
		print(header.center(48,'*'))
		print('-'*48)

	def show_usuario_midder(self):
		print('-'*78)

	def show_usuario_footer(self):
		print('*'*78)
	"""
	***********************
	* Vistas de Peliculas *
	***********************
	"""
	def peliculas_menu(self):
		print('******************************')
		print('* -- Submenu de Peliculas -- *')
		print('******************************')
		print('1. Agregar Pelicula')
		print('2. Mostrar una Pelicula')
		print('3. Mostrar todos las Peliculas')
		print('4. Mostrar Peliculas de cierta Clasificacion')
		print('5. Actualizar Pelicula')
		print('6. Borrar Pelicula')
		print('7. Regresar')

	def show_pelicula(self, record):
		print('ID:', record[0])
		print('Titulo:', record[1])
		print('Duracion:', record[2])
		print('Clasificacion:', record[3])
		print('Sipnosis:', record[4])
		print('Formato:', record[5])
		print('Idioma:', record[6])
		print('Fecha Lanzamiento:', record[7])
		print('Director:', record[8])
		print('Actores:', record[9])

	def show_pelicula_header(self, header):
		print(header.center(48,'*'))
		print('-'*48)

	def show_pelicula_midder(self):
		print('-'*78)

	def show_pelicula_footer(self):
		print('*'*78)


	"""
	************************
	* Vistas de Asientos *
	************************
	"""
	def asientos_menu(self):
		print('*****************************')
		print('* -- Submenu de Asientos -- *')
		print('*****************************')
		print('1. Agregar Asiento')
		print('2. Mostrar un Asiento')
		print('3. Mostrar todos los Asientos')
		print('4. Mostrar Asientos Disponibles')
		print('5. Actualizar Asiento')
		print('6. Borrar Asiento')
		print('7. Regresar')

	def show_asiento(self, record):
		print('ID:', record[0])
		print('Estado:', record[1])


	def show_asiento_header(self, header):
		print(header.center(48,'*'))
		print('-'*48)

	def show_asiento_midder(self):
		print('-'*78)

	def show_asiento_footer(self):
		print('*'*78)



	"""
	*******************
	* Vistas de Salas *
	*******************
	"""
	def salas_menu(self):
		print('*****************************')
		print('* -- Submenu de Salas -- *')
		print('*****************************')
		print('1. Agregar Sala')
		print('2. Mostrar una Sala')
		print('3. Mostrar todas las Salas')
		print('4. Mostrar Salas Disponibles')
		print('5. Actualizar Sala')
		print('6. Borrar Sala')
		print('7. Regresar')

	def show_sala(self, record):
		print('ID:', record[0])
		print('Numero Total de Asientos:', record[1])
		print('Estado:', record[2])


	def show_sala_header(self, header):
		print(header.center(48,'*'))
		print('-'*48)

	def show_sala_midder(self):
		print('-'*78)

	def show_sala_footer(self):
		print('*'*78)



	"""
	**********************
	* Vistas de Horarios *
	**********************
	"""
	def horarios_menu(self):
		print('*****************************')
		print('* -- Submenu de Horarios -- *')
		print('*****************************')
		print('1. Agregar Horario')
		print('2. Mostrar un Horario')
		print('3. Mostrar todos los Horarios')
		print('4. Mostrar Horarios de una fecha especifica')
		print('5. Actualizar Horario')
		print('6. Borrar Horario')
		print('7. Regresar')

	def show_horario(self, record):
		print('ID_Horario:', record[0])
		print('Sala:', record[1])
		print('Pelicula:', record[2])
		print('Fecha:', record[3])
		print('Hora:', record[4])


	def show_horario_header(self, header):
		print(header.center(48,'*'))
		print('-'*48)

	def show_horario_midder(self):
		print('-'*78)

	def show_horario_footer(self):
		print('*'*78)



	"""
	********************
	* Vistas de Boletos*
	********************
	"""
	def boletos_menu(self):
		print('*****************************')
		print('* -- Submenu de Boletos -- *')
		print('*****************************')
		print('1. Agregar Boleto')
		print('2. Mostrar un Boleto')
		print('3. Mostrar todos los Boletos')
		print('4. Mostrar Boletos de una fecha especifica')
		print('5. Actualizar Boleto')
		print('6. Borrar Boleto')
		print('7. Regresar')

	def show_boleto(self, record):
		print('ID:', record[0])
		print('Usuario:', record[1])
		print('Pelicula:', record[2])
		print('Sala:', record[3])
		print('Asiento:', record[4])
		print('Fecha:', record[5])
		print('Hora:', record[6])


	def show_boleto_header(self, header):
		print(header.center(48,'*'))
		print('-'*48)

	def show_boleto_midder(self):
		print('-'*78)

	def show_boleto_footer(self):
		print('*'*78)


	def show_validacion_usuario(self, record):
		print('El tipo de este usuario es: ',record)
