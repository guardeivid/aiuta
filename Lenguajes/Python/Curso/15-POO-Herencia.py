# -*- coding: utf-8 -*-
#super

class Persona(object):
	def __init__(self, nombre, edad, lugar_residencia):
		#super(Persona, self).__init__()
		self.nombre = nombre
		self.edad = edad
		self.lugar_residencia = lugar_residencia

	def descripcion(self):
		print("Nombre: " + self.nombre + " Edad: " + str(self.edad) + " Residencia: " + self.lugar_residencia)


class Empleado(Persona):
	def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
		#p2
		super(Empleado, self).__init__(nombre_empleado, edad_empleado, residencia_empleado)
		#p3
		#super().__init__("Antonino", 22, "Francia")
		self.salario = salario
		self.antiguedad = antiguedad

	def descripcion(self):
		super(Empleado, self).descripcion()
		print("Salario: " + str(self.salario) + " Antigüedad: " + str(self.antiguedad))

antonio=Persona("Antonio", 55, "España")
antonio.descripcion()

antonio2=Empleado(1500, 15, "Antonino", 22, "Francia")
antonio2.descripcion()
		
# principio de sustitucion, un objeto de una clase hija es siempre un/a objeto de la superclase
#isinstance, permite saber de que clase es (devuelve True o False)

print(isinstance(antonio2, Empleado))
print(isinstance(antonio2, Persona))
#si hereda es siempre 

#no siempre una persona no es un empleado
print(isinstance(antonio, Empleado))