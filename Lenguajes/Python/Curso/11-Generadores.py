#funcion tradicional, devuelve la lista completa
"""
def generaPares(limite):
	num=1
	miLista=[]
	while num<limite:
		miLista.append(num*2)
		num+=1
	return miLista

print(generaPares(10))
# [2, 4, 6, 8, 10, 12, 14, 16, 18]
"""

"""
# con un generador, devuelve de a uno en uno, a medida que se llama a la funcion
def generaPares2(limite):
	num=1
	while num<limite:
		yield num*2
		num+=1

# imprimir toda la lista, no tiene diferencia con return
devuelvePares=generaPares2(10)
for i in devuelvePares:
	print(i)

# imprimir 3 valores de la lista
devuelvePares=generaPares2(10)
print(next(devuelvePares))
print("entra en suspension y ahorra recursos")
print(next(devuelvePares))
print("mas codigo")
print(next(devuelvePares))
"""

#----------------------------
# yield from
#un asterisco significa que va a recibir un numero indefinido de argumentos en forma de tupla
def devuelve_ciudades(*ciudades):
	for elem in ciudades:
		yield elem

ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")
# devuelve 2 elementos
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))


# sintaxis de bucles anidades
def devuelve_ciudades2(*ciudades):
	for elem in ciudades:
		for subelem in elem:
			yield subelem

ciudades_devueltas = devuelve_ciudades2("Madrid", "Barcelona", "Bilbao", "Valencia")
# devuelve 2 subelementos del primer elemento
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))


# sintaxis simplificada, en python 3
def devuelve_ciudades3(*ciudades):
	for elem in ciudades:
		#for subelem in elem:
		yield from elem

ciudades_devueltas = devuelve_ciudades3("Madrid", "Barcelona", "Bilbao", "Valencia")
# devuelve 2 subelementos del primer elemento
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))


#-------------------------------------
def factorial(n):
	i = 1
	while n > 1:
		i = n*i
		yield i
		n -= 1

for e in factorial(5):
	print e