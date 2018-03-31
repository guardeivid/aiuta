
def evaluacion(nota):
	valoracion="aprobado"
	if nota < 5:
		valoracion="desaprobado"
	return valoracion

print(evaluacion(8))

print("Programa de evaluacion de notas de alumnos")
# para sublime para poder ejecutar, en modo consola, hay que usar 
# Tools -> SublimeREPL -> Python -> Python - RUN Current File
nota_alumno=input("Introduce la nota del alumno: ")
print(evaluacion( int(nota_alumno) ))

#---------------------------------------------------
print("Programa de verificacion de acceso")
edad_usuario = int( input("Intruce tu edad: "))
def verificacion(edad):
	if edad < 18:
		acceso="No puedes pasar"
	elif edad > 100:
		acceso="Edad incorrecta"
	else:
		acceso="Puedes pasar"
	return acceso
print(verificacion( edad_usuario ))

#-------------------------------------------------
# concatenacion de operadores de comparacion
edad=-7
if 0 < edad < 100:
	print("La edad es correcta")
else:
	print("edad es incorrecta")


salario_presidente=int(input("introduce salario del presidente: "))
print("Salario presidente: " + str(salario_presidente))

salario_director=int(input("introduce salario del director: "))
print("Salario director: " + str(salario_director))

salario_jefe=int(input("introduce salario del jefe: "))
print("Salario jefe: " + str(salario_jefe))

salario_administrativo=int(input("introduce salario del administrativo: "))
print("Salario administrativo: " + str(salario_administrativo))

if salario_administrativo < salario_jefe < salario_director < salario_presidente:
	print("todo funciona correctamente")
else:
	print("algo falla en la empresa")

#-----------------------------------------------------------------
distancia_escuela=10
num_hermanos=40
salario_familiar=2000

if distancia_escuela > 40 and num_hermanos > 2 or salario_familiar <= 20000:
	print("Tienes derecho a beca")
else:
	print("No tienes derecho a beca")

#-----------------------------------------------------------------

print("Escribir una asignatura", "informatica", "redes", "matematica")
asignatura=str(input("ingrese una asignatura: "))
if asignatura.lower() in ("informatica", "redes", "matematica"):
	print("la asignatura elegida es " + asignatura)
else:
	print("la asignatura no esta disponible")