Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print ("Hola Alumnos")
Hola Alumnos
>>> # escribir siempre en una sola linea
>>> # para hacer en varias lineas
>>> print ("Hola alumnos");print("adios mundo cruel")
Hola alumnos
adios mundo cruel
>>> # comentarios con almohadilla
>>> # se puede separar una instruccion en varias lineas
>>> mi_nombre="mi nombre es Juan!"
>>> mi_nombre
'mi nombre es Juan!'
>>> mi_nombre="mi nombre es \"
SyntaxError: EOL while scanning string literal
>>> mi_nombre="mi nombre es \
Juan"
>>> mi_nombre
'mi nombre es Juan'
>>> # identacion, se recomienda hacer una pequeña tabulacion en cada bloque
>>> a=0
>>> for i in range(5):
	#automaticamente genera la identificacion
	a+=1
	print(a)

	
1
2
3
4
5
>>> 
