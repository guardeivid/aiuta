# -*- coding: utf-8 -*-
# HERENCIA

# Clase padre o superclase
class Vehiculos(object):
	def __init__(self, marca, modelo):
		self.marca = marca
		self.modelo = modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False
	
	def arrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", 
			self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena)

class Furgoneta(Vehiculos):

	def __init__(self, marca, modelo):
		#super(Furgoneta, self).__init__(marca, modelo)
		Vehiculos.__init__(self, marca, modelo)

	def carga(self, cargar):
		self.cargado=cargar
		if self.cargado:
			return "la furgoneta está cargada"
		else:
			return "la furgoneta NO esta cargada"
		


#Clase Moto hereda de Vehiculos
class Moto(Vehiculos):
	hcaballito=""
	#pass
	#en p3 no es necesario declarar el constructor para llamar al padre con los mismos argumentos
	def __init__(self, marca, modelo):
		#super(Moto, self).__init__(marca, modelo)
		Vehiculos.__init__(self, marca, modelo)

	def caballito(self):
		self.hcaballito="voy haciendo caballito"

	#sobreescribiendo un metodo
	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", 
			self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado: ", self.frena, self.hcaballito)


#clase independiente
class VElectricos(Vehiculos):
	def __init__(self, marca, modelo):
		super(VElectricos, self).__init__(marca, modelo)
		self.autonomia=100

	def cargarEnergia(self):
		self.cargando=True


#Herencia multiple, a la izquierda va la clase mas cercana, la que tiene preferncia
class BicicletaElectrica(VElectricos, Vehiculos):
	def __init__(self, marca, modelo):
		super(BicicletaElectrica, self).__init__(marca, modelo)
		#VElectricos.__init__(self)
		#Vehiculos.__init__(self, "Orbea", "HC1030")
