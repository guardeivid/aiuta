# declarar una funcion
def mensaje():
	print("Estamos aprendiendo Python")
	print("Estamos aprendiendo instrucciones basicas")
	print("Poco a poco iremos avanzando")

# llamar a una funcion
mensaje()
mensaje()
print("Ejecutando codigo fuera de funcion")
mensaje()

###---------------------------------------------
def suma():
	num1=5
	num2=7
	print(num1+num2)

suma()

# con parametros
def suma2(num1, num2):
	print(num1+num2)

suma2(5, 7)
suma2(2, 3)


# Funciones con return
def suma3(num1, num2):
	return num1+num2

resultado=suma3(15, 27)
print(resultado)
# python pasa los valores siempre por referencias


