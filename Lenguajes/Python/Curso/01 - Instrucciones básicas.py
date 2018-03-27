Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 5+6
11
>>> # modulo, es el resto de una division
... 10/3
3
>>> 10%3
1
>>> # exponente, la potencia 5 al cubo
... 5**3
125
>>> # division entera, devuelve el numero entero de una division
... 9//4
2
>>> # variable, empieza con una letra minuscula o mayuscula, puede tener guion bajo y puede combinarse con numeros
... # el tipo lo establece el contenido
... numero=5
>>> # todo en python es un objeto
... # devolver el tipo de dato
... type(numero)
<type 'int'>
>>> nombre="Juan"
>>> type(nombre)
<type 'str'>
>>> nombre=5.2
>>> type(nombre)
<type 'float'>
>>> # triple comillas, para poner saltos de lineas en textos
... mensaje=""" Esto es un mensaje
... con tres saltos
... de lineas"""
>>> print(mensaje)
 Esto es un mensaje
con tres saltos
de lineas
>>> # Condicionales
... n1=5
>>> n2=7
>>> # operadores de comparacion
... if n1 > n2:
... 	print("El numero 1 es mayor")
... else:
... 	print("El numero 2 es mayor")
... 
El numero 2 es mayor
>>> 