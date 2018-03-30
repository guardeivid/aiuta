class Coche(object):
	#propiedades
	largoChasis=250
	anchoChasis=120
	ruedas=4
	enmarcha=False

	#metodos
	#self (explicito): hace referencia a la instancia de la clase (=this implicito)
	def arrancar(self):
		self.enmarcha=True

	def estado(self):
		if(self.enmarcha):
			return "el coche esta en marcha"
		else:
			return " el coche esta parado"

# construir un objeto, instanciando a la clase (no se usa new)
coche1=Coche()
print("El largo del coche es: ", coche1.largoChasis)
print("El coche tiene: ", coche1.ruedas, " ruedas")
print("el coche esta: ", coche1.enmarcha)
print(coche1.estado())
coche1.arrancar()
print("el coche esta: ", coche1.enmarcha)	
print(coche1.estado())