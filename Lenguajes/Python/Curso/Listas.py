miLista=["Maria", "Pepe", "Marta", "Antonio"]
#Imprimir la lista completa
print(miLista)
print(miLista[:])

# imprimir un elemento en concreto
print(miLista[2])

# error si se quiere acceder a un indice que no existe
#print(miLista[7])

# imprimir un elemento contando desde el final, -1 es el ultimo
print(miLista[-2])

# porcion de lista, [desde el indice inclusive:hasta el indice no inclusive]
print(miLista[0:3])
# igual si se omite
print(miLista[:3])

# otro, accede desde el 2 hasta el final
print(miLista[2:])

# agregar elementos al final a una lista
miLista.append("Sandra")
print(miLista[:])

# agregar elementos en un determinado indice a una lista
miLista.insert(3, "Sandro")
print(miLista[:])

# unir listas
miLista.extend( ["Ana", "Lucia"]  )
print(miLista[:])

# obtener el inidice de un valor, siempre devuelve el primero que encuentra
print(miLista.index( "Ana" ))

# saber si un elemento se encuentra en una lista
print("Pepess" in miLista)

# puede tener diferentes tipos de datos
miLista.extend( [5, True, 78.35] )
print(miLista[:])

# eliminacion elementos de una lista por nombre
miLista.remove("Ana")
print(miLista[:])

# eliminar el ultimo elemento de una lista
miLista.pop()
print(miLista[:])

# sumar listas, une en una nueva lista, concatenando las listas
miLista2 = [ "Carlos", "Juan"]
miLista3 = miLista + miLista2
print(miLista3)

# el asterisco, es un repetidor
print(miLista3*3)