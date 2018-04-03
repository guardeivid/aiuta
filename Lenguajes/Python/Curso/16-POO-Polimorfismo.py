
class Coche(object):
	def desplazamiento(self):
		print("me desplazo con 4 ruedas")

class Moto(object):
	def desplazamiento(self):
		print("me desplazo con 2 ruedas")

class Camion(object):
	def desplazamiento(self):
		print("me desplazo con 6 ruedas")

#tienen el mismo metodo
"""
miVehiculo=Moto()	
miVehiculo.desplazamiento()

miVehiculo2=Coche()	
miVehiculo2.desplazamiento()

miVehiculo3=Camion()	
miVehiculo3.desplazamiento()
"""

#con polimorfismo, cambia de forma, entonces sabe a que metodo tiene que llamar
def desplazamientoVehiculo(vehiculo):
	vehiculo.desplazamiento()

miVehiculo=Camion()
desplazamientoVehiculo(miVehiculo)