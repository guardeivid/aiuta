class Humano:
	def __init__(self, edad):
		self.edad = edad
	def hablar(self, mensaje):
		print mensaje

class IngSistemas(Humano):
	def __init__(self):
		print 'Hola'
	def programar(self, lenguaje):
		print 'Voy a programar en ', lenguaje

class LicDerecho(Humano):
	def __init__(self, escuela):
		print 'Lic. en Derecho egresado de: ', escuela
	def estudiarCaso(self, de):
		print 'Debo estudiar el caso de ', de

class Estudioso(IngSistemas,LicDerecho):
	#metodo __init__ toma el primero de las clase declaradas
	pass
		
		
#pedro = IngSistemas()
#raul = LicDerecho(27)

juan = Estudioso()
juan.hablar("soy de herencia multiple")
juan.programar("C++")
juan.estudiarCaso(45)