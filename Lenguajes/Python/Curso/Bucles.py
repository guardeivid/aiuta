# lista, tupla, rango, texto, numero
"""
for i in [1,.2,3]:
	print("Hola")
"""
#imprime 3 veces el mensaje porque tiene tres elementos

"""
estaciones= ["primavera","Verano", "otono", "invierno"]
for i in estaciones:
	print(i)
"""

#--------------------------------------------------
# imprimir en una linea con print("", end="") python 3
"""
for i in ["pildoras", "informaticas", 3]:
	#print("Hola", end=" ")
	pass
"""

# recorrer caracteres de un texto
"""
for i in "asdhdhakdkajsldjs":
	print("Hola")
"""

"""
email=False
contador=0
for i in "asdhdha@kdkajsldjs":
	if i == "@":
		email=True
		contador+=1
		break

if email == True:
	print("el email es correcto")
else:
	print("el email no es correcto")
	print("Hola")

print(contador)
"""

"""
# en python 2 es una funcion, en python 3 crea una lista de 5 elementos
for i in range(5):
	print(i)

# en py3, funcion de formato, y con llaves
for i in range(5, 10):
	#print(f"valor de la variable {i}")
	print("valor de la variable : " + str(i))
# range acepta, el numero de elementos, o el rango entre elementos, y acepta un tercer valor que es de a cuanto tiene que aumentar
for i in range(5, 50, 3):
	print("valor de la variable : " + str(i))
"""

"""
valido=False
email=input("introduce tu email: ")
for i in range(len(email)):
	if email[i] == '@':
		valido = True

if valido:
	print("email correcto")
else:
	print("email incorrecto")
"""

#-----------------------------------
# WHILE
"""
i=1
while i <= 10:
	print(i)
	i+=1
"""

"""
edad=int(input("ingrese la edad: "))

while edad < 0:
	print("has introducido una edad negativa, vuelve a intentarlo")
	edad=int(input("ingrese la edad: "))

print("su edad es " + str(edad))
"""


#---------------------------------------------------------------------
import math

print("Programa de calculo de raiz cuadrada")
numero=int(input("ingrese un numero: "))
intentos=0
while numero < 0:
	print("no se puede hallar la raiz de un numero negativo")
	if intentos == 2:
		print("muchos intentos. el Programa ha finalizado")
		break
	numero=int(input("ingrese un numero: "))
	if numero < 0:
		intentos+=1

if intentos < 2:
	solucion = math.sqrt(numero)
	print("la raiz cuadrada de " + str(numero) + " es " + str(solucion))

#----------------------------------------------------------------

# Continue - pass - else
