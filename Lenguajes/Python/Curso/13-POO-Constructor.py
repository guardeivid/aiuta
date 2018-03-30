# Estado inicial, constructor

class Coche(object):
	
	#constructor, metodo inicial que le da el estado inicial a los objetos cuando se instancian
	def __init__(self):
		#variables publicas
		self.largoChasis=250
		self.anchoChasis=120
		#variables encapsuladas privadas, anteponiendo 2 guiones bajos __, solo accesible dentro de la propia clase
		self.__ruedas=4
		self.__enmarcha=False

	#metodos
	#self (explicito): hace referencia a la instancia de la clase (=this implicito)
	def arrancar(self, arrancamos):
		self.__enmarcha=arrancamos
		if self.__enmarcha:
			#variable local dentro de esta funcion, llamando a un metodo encapsulado
			chequeo=self.__chequeo_interno()

		if(self.__enmarcha and chequeo):
			return "el coche esta en marcha"
		elif self.__enmarcha == True and chequeo == False:
			return "algo ha ido mal en el chequeo. no podemos arrancar"
		else:
			return " el coche esta parado"

	def estado(self):
		print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", 
			self.anchoChasis, " y un largo de ", self.largoChasis)

	#metdo encapsulado, para que no este disponible desde fuera de la clase
	def __chequeo_interno(self):
		print("realizando chequeo interno")
		self.gasolina="ok2"
		self.aceite="ok"
		self.puertas="cerradas"

		if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
			return True
		else:
			return False


# construir un objeto, instanciando a la clase (no se usa new)
coche1=Coche()
print(coche1.arrancar(True))
coche1.estado()

coche2=Coche()
#no cambia la variable porque esta encapsulada
coche2.__ruedas=2
coche2.ruedas=2
print(coche1.arrancar(False))
coche2.estado()
#en caso de querer llamar al metodo encapsulado, tira error
#print(coche2.__chequeo_interno())
