miTupla=("Juan", 13, 1 , 1995)
print(miTupla[1])

# Convertir una lista en tupla, imprime con corchetes
milista = list(miTupla) 
print(milista)

# Convertir una tupla en lista, imprime con parentesis
miTupla2 = tuple(milista) 
print(miTupla2)

# saber si hay un elemento en una tupla
print("Juan" in miTupla2)

# cuantos elemtos se encuentran dentro de una tupla, count(elem)
print(miTupla2.count(13))

# saber cuantos elementos tiene una tupla
print(len(miTupla2))

# tuplas unitarias, con un solo elemento, lleva una coma
tuplaUnitaria=("Juan",)
print(len(tuplaUnitaria))

# se puede crear una tupla sin los parentesis, pero puede llevar a confusion,(empaquetado de tupla)
miTupla3="Juan", 13, 1 , 1995
print(miTupla3)

# desempaquetado de tupla, almacenando los valores de la tupla en cada variable
miTupla4=("Juan", 13, 1 , 1995)
nombre, dia, mes, agno = miTupla4
print(nombre)
print(mes)
print(agno)
print(dia)

# no se puede modificar, por ejemplo con append, remove, extend