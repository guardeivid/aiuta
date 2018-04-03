# -*- coding: utf-8 -*-

#para trabajar con archivos externos
#import io
from io import open

#crear si no existe y abre archivo, nombre, modo de apertura (r= lectura, w= escritura, a= agregar informacion a un archivo que ya existe)
archivo_texto=open("19-archivo.txt", "w")
#en p2 requiere que el texto sea unicode, en p3 todo es unicode
frase=u"Estupendo día para estudiar Python \n el miércoles"
#manipular
archivo_texto.write(frase)
#cerrar
archivo_texto.close()

#---------------------
#Abrir en modo lectura
archivo_texto2=open("19-archivo.txt", "r")
#leer el contenido
texto=archivo_texto2.read()
archivo_texto2.close()

print(texto)

#-----------------------
#tambien se puede leer linea a linea con el metodo readlines, y almacena en una lista
archivo_texto3=open("19-archivo.txt", "r")
lineas_texto=archivo_texto3.readlines()
archivo_texto3.close()

print(lineas_texto)

#acceder a la primera linea
print(lineas_texto[0])
# recorrer la lista, combinar con condicional, etc


#------------------------
#agregar informacion
archivo_texto4=open("19-archivo.txt", "a")
archivo_texto4.write(u"\n siempre es una buena ocasion para seguir estudiando")
archivo_texto4.close()


#-----------------------
#Puntero, es como el cursor dentro del archivo, se puede desplazar, por defecto, es al principio, y cuando termina de leer es al final
archivo_texto2=open("19-archivo.txt", "r")
print(archivo_texto2.read())

#para modificar la posicion del puntero es con el metodo seek(numero de caracteres)
#volver al principio
archivo_texto2.seek(0)
print(archivo_texto2.read())

#los primeros 10 caracteres no los va a tener en cuenta
archivo_texto2.seek(11)
print(archivo_texto2.read())

# tambien se puede hacer con read, 
#desde la posicion en donde se encuentra el puntero hasta la posicion dada
archivo_texto2.seek(0)
print(archivo_texto2.read(10))

#poner el puntero a la mitad del contenido del archivo
archivo_texto2.seek(0)
archivo_texto2.seek(len(archivo_texto2.read())/2)
print(archivo_texto2.read())


# cursor al final de cada linea
archivo_texto2.seek(0)
archivo_texto2.seek(len(archivo_texto2.readlines()))
print(archivo_texto2.read())

#------------------------------------
#abrir en varios modos
archivo_texto=open("19-archivo.txt", "r+") #lectura y escritura
#sobreescribe los primeros caracteres, porque el cursor esta al inicio
archivo_texto.write(u"Comienzo del texto")
archivo_texto.close()


#-------------------------
#con readlines y writelines
archivo_texto=open("19-archivo.txt", "r+")
#devuelve una lista
#print(archivo_texto.readlines())
lista_texto=archivo_texto.readlines()

lista_texto[1]=u"Esta linea ha sido incluida desde el exterior\n"
archivo_texto.seek(0)
#escribir de a lineas
archivo_texto.writelines(lista_texto)
archivo_texto.close()