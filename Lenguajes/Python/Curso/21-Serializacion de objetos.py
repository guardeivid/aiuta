import pickle

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

coche1=Vehiculos("Mazda", "MX5")
coche2=Vehiculos("Seat", "Leon")
coche3=Vehiculos("Renault", "Megane")

coches=[coche1, coche2, coche3]

fichero_binario=open("21-objeto_binario", "wb")
pickle.dump(coches, fichero_binario, 2)
fichero_binario.close()
del fichero_binario

#-----leer-----
fichero_binario2=open("21-objeto_binario", "rb")
misCoches=pickle.load(fichero_binario2)
fichero_binario2.close()
#print(misCoches)

for c in misCoches:
	print(c.estado())
