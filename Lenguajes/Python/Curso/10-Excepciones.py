def evalueEdad(edad):

	if edad <0:
		# se especifica el tipo de excepcion
		raise TypeError("no se permiten edades negativas")

	if edad< 20:
		return "eres muy joven"
	elif edad<40:
		return "eres joven"
	elif edad<65:
		return "eres maduro"
	elif edad<100:
		return "cuidate..."

# no existe edades negativas
#print(evalueEdad(4))

# las siguientes lineas no se ejecutarian 


#-------------------------------------
# no se puede calcular la raiz cuadrado de un numero negativo
import math

def calculaRaiz(n1):
	if n1<0:
		raise ValueError("el numero no puede ser negativo")
	else:
		return math.sqrt(n1)

op1=(int(input("introduce un numero: ")))
try:
	print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
	print(ErrorDeNumeroNegativo)

# manera general de capturar cualquier tipo de error
try:
	print(calculaRaiz(op1))
except Exception as e:
	print e

print("programa terminado")