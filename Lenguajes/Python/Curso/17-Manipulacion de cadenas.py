# Documentacion de Python  http://pyspanishdoc.sourceforge.net/

# upper() letras a mayusculas
print("juan".upper()) 

# lower() letras a minusculas
print("JUAN".lower())

# capitalize() primera letra a mayusculas
print("JUAN".capitalize())

# count() cuenta la aparicion de alguna subcadena
print("JUANuuuu".count("u"))


# find() encuentra la posicion de una subcadena

# isdigit() si es numerico
edad=str(input("introduce la edad: "))
while edad.isdigit() == False:
	print("por favor introduce un valor numerico")
	edad=str(input("introduce la edad: "))

if int(edad)<18:
	print("no puede pasar")
else:
	print("puede pasar")
	
# isalum() si es alfanumerico

# isalpha() si es solo letras

# split() divide una cadena por espacios en blanco

# strip() remueve espacios en blanco a los lados

# replace() reemplaza una cadena por otra

# rfind() encuentra el indice contando desde atras

# join() une una secuencia -lista, tupla- por un delimitador
tupla = ("H", "o", "l", "a")
delimitador = ";"
print delimitador.join(tupla)