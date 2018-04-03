import pickle

class Persona(object):
	def __init__(self, nombre, genero, edad):
		self.nombre = nombre
		self.genero = genero
		self.edad = edad
		print("Se ha creado una persona con el nombre de " + self.nombre)

	def __str__(self):
		return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas(object):
	personas=[]

	def __init__(self):
		listaDePersonas=open("22-ficheroexterno", "ab+")
		listaDePersonas.seek(0)

		try:
			self.personas=pickle.load(listaDePersonas)
			print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
		except:
			print("El fichero esta vacio")
		finally:
			listaDePersonas.close()
			del(listaDePersonas)

	def agregarPersonas(self, p):
		self.personas.append(p)
		self.guardarPersonasEnFicheroExterno()
		
	def mostrarPersonas(self):
		for p in self.personas:
			print(p)

	def guardarPersonasEnFicheroExterno(self):
		listaDePersonas=open("22-ficheroexterno", "wb")
		pickle.dump(self.personas, listaDePersonas, 2)
		listaDePersonas.close()
		del(listaDePersonas)


#-------------------------------------------
miLista=ListaPersonas()
"""
#cargar informacion
p=Persona("Sandra", "Femenino", 29)
miLista.agregarPersonas(p)
#print(p.__str__())
p=Persona("Antonio", "Masculino", 39)
miLista.agregarPersonas(p)
p=Persona("Ana", "Femenino", 19)
miLista.agregarPersonas(p)


"""
#leer informacion
miLista.mostrarPersonas()
