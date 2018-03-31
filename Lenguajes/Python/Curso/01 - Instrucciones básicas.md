### Sintáxis básica

Tipos de datos

- Numericos
  - Enteros (int)
  - Decimales (float)
  - Complejos (list-Listas, tuple-Tuplas, dict-Diccionarios, obj-Objetos)
  - Textos (con comillas simples, dobles, triples)
  - Booleanos (True, False)

Operadores

- Aritméticos (+, -, *, /, **, //, %) (suma, resta, multiplicacion, division, exponente, division entera, modulo)
- Comparación (==, !=, >, <, >=, <=)
- Lógicos (AND, OR, NOT)
- Asignación (=, +=, -=, *=, /=, %=, **=, //=)
- Especiales (IS, IS NOT, IN, NOT IN)

Variable
```py
# Obtener el tipo de una variable 
type(variable)
```

##### Manejo de cadenas

```py
# Declaracion de variables con = "", ''
s1 = "hola"
s2 = "hola"
s3 = "hola mundo"

# Igualdad con ==
s1 == s2 ## True
s2 == s3 ## False

# Contiene una subcadena, con in
print s1 in s3 ## True

# Indexacion de caracteres con [], desde 0, 1, etc, y de atras desde -1, -2
s1[0] ## h

# Subcadenas con [i:f],
s1[:] ## copia desde 0 hasta el final, hola
s1[0:2] ## inicia en 0, hasta la 1, la 2 no se incluye, ho
s1[2:]  ## desde el caracter 2 hasta el final
s1[:-1] ## desde el inicio hasta menos 1 del final

# Funciones para manipular cadenas
# Devuelven True o False
s1.isalnum() ## si tiene letras y numeros
s1.isupper() ## si es todo mayusculas
s1.islower() ## si es todo minusculas
s1.isalpha() ## si es todo letras

# Devuelven la cadena modificada
s3.title() ## convierte a titulo, "Hola Mundo"
s3.upper() ## convierte a mayusculas, "HOLA MUNDO"
s3.lower() ## convierte a minusculas, "hola mundo"
s3.swapcase() ## invierte las letras, "HOLA MUNDO"
s3.capitalize() ## primera letra a mayusculas, "Hola Mundo"

str(x) ## convierte un numero a una cadena 

# Quitar espacios en blanco
cadena.strip()  ## quita espacios a ambos lados de la cadena
cadena.rstrip() ## quita a la derecha
cadena.lstrip() ## quita a la izquierda

# Encontrar el indice de la primera aparicion de una cadena o caracter, caso contrario devuelve -1
s3.find("a") ## 3

# Reemplazar una subcadena en una cadena
s3.replace("mundo", "universo") ## hola universo

# Separar una cadena de palabras en una lista, por un caracter, por defecto " "
s3.split() ## ["hola", "mundo"]

# Longitud de una cadena
len(s3) ## 10

```

##### Manejo de números
```py
# Funciones incorporadas
abs(x) ## devuelve el valor absoluto de un numero
int(x) ## convierte una cadena a un entero
float(x) ## convierte una cadena a un numero decimal
round(x,n) ## devuelve un numero decimal con n digitos decimales

# Funcionalidad avanzada en el modulo math
import math

math.ceil(x) ## redondea hacia arriba a x
math.floor(x) ## redondea hacia abajo a x
math.fabs(x) ## devuelve el valor absoluto de x

# funciones trigonometricas
math.acos(x)
math.asin(x)
math.atan(x)
math.cos(x)
math.sin(x)
math.tan(x)
math.hypot(x,y)

# funciones de potencia y logaritmicas
math.exp(x) ## exponente
math.log(x [, base])
math.log10(x)
math.pow(x,y) ## potencia
math.sqrt(x) ## raiz cuadrada

# conversion angular
math.degrees(x)
math.radians(x)
```

### Funciones

- Pueden o no devolver valores, en realidad si no se especifica **return** devuelve None (=null)
- Pueden tener parametros/argumentos de entrada
- Tambien se denominan "metodos" si estan definidas en una clase
- Se definen con la palabra **def**

```py
def nombre_funcion(parametros):
	instrucciones
	return (opcional)

nombre_funcion(parametros)
```
- Puede tener parámetros opcionales
```py
def nombre_funcion(url, data=None):
	instrucciones
	return result

nombre_funcion(parametros)
```

### Listas

- Similar a arrays
- Pueden guardar diferentes tipos de valores
- Se pueden expandir dinamicamente
- Son ordenadas por indice, desde 0, 1, etc

```py
nombreLista = [elem1, elem2, elem3...]
```
- Se localizan por un indice, comienza a enumerar por 0
```py
nombreLista[0]
```

- Se puede crear una nueva lista de otra
```py
nuevaLista = nombreLista[0:2]
```

- Cantidad de elkementos de una lista
```py
len(miLista)
```

Agregar elemento al final de una lista
```py
nombreLista.append(elem)
```

Eliminar elemento de una lista
```py
del nombreLista[2]
```

Ordenar una lista
```py
nombreLista.sort()   ## ascendente
nombreLista.reverse() ## descendente
```

Agregar elemento en un indice determinado
```py
nombreLista.insert(indice, elem)
```

Extender y concatenar listas
```py
nombreLista.extend( nombreLista2  )
nombreLista + nombreLista2
```

Obtener el inidice de un valor, siempre devuelve el primero que encuentra
```py
nombreLista.index( elem )
```

Determinar si un elemento se encuentra en una lista
```py
elem in nombreLista
```

Modificar contenido de las listas, sin necesidad de hacer una copia, por indice o secuencia
```py
nombreLista[1] = "nuevoValor"
nombreLista[0:2] = ["nuevoValorEnIndice0", "nuevoValorEnIndice1"] ## indice 2 no lo incluye
```

### Tuplas

- Son listas inmutables, no se pueden modificar
- No funciona append, extend, remove, del, sort, reverse
- Permiten extraer una porcion en una nueva tupla por secuencia

- Mas rápidas
- Menos espacio, mejor rendimiento
- Formatean strings
- Pueden utilizarse como claves en un diccionario (las listas no)

```py
nombreTupla = (elem1, elem2, elem3...)

#Permite concatenacion con 
tupla1 + tupla2
```


### Diccionarios

- Parecidos a objetos, array asociativos, clave unica:valor
- Los elementos no estan ordenados, por lo tanto no se pueden extraer por secuencia
- Permiten almacenar cualquier tipo de dato

```py
nombreDiccionario = { clave: valor, ...}

# acceder por medio de la clave
nombreDiccionario[clave]

# Determinar si existe una clave
nombreDiccionario.has_key(clave)

# Obtener una lista de claves
nombreDiccionario.keys()

# Obtener una lista de valores
nombreDiccionario.values()

# Con la lista de claves se puede iterar todos los elementos de un diccionario
listKeys = nombreDiccionario.keys()
for x in listKeys: print x
```


### Estructura de control

- Dos puntos en el extremo de cada condicion
- Dos signos de igual para probar una condicion de igualdad
- Sangria para las instrucciones siguientes, agrupando sentencias en un bloque
- Quitar sangria para finalizar la condicion

#### Condicionales

##### IF

```py
if condicion:
	instruccion
elif condicion:
	instruccion
else:
	instruccion
```

##### SWITCH no existe

##### Alternativas al Switch
Concatenacion de operadores de comparacion
```py
if condicion1 < condicion2 < condicion3 < condicion4:
	instruccion
else:
	instruccion
```

Comparacion AND OR

Comparacion IN ()

#### Bucles

##### FOR
Bucle determinado
```py
for variable in elemento_a_recorrer:
	instruccion

#Puede se contados con rangos, o por listas
```

Ejemplo para ArcGis
```py
import arcpy

arcpy.env_workspace = "C:\RutaALaCarpetaConShape\Data"
lfc = arcpy.ListFeatureClasses() #almacena una lista con todas las features clases del directorio de trabajo

for x in lfc:
	sr = arcpy.Describe(x).SpatialReference
	print x + ": " + sr.Name + "\n"

# x = nombre del archivo.shp
# sr.Name = nombre del sistema de referencia
```


##### WHILE
Bucle indeterminado, hasta que se deje de cumplir la condicion
```py
while condicion:
	instruccion
```


**Continue**
Salta a la siguiente iteración del bucle, ignorando las instrucciones siguientes

**Pass**
Devuelve null, como si no se ejecutara el bucle


**Else**
Como si fuera un condicional, cunado termo de recorrer el bucle


#### Generadores

- Extraen valores de una funcion de una manera de objetos iterable, como lista
- Se almacen de uno a uno, y no de a todos a la vez
- Cuando un generador almacena un valor, permanece pausado hasta que se solicita el siguiente (suspension de estado), devolviendo de uno en uno.
- Se declaran con **yield** en vez de *return*, aunque tambien puede llevar un return

```py
def funcion():
	yield valor
```
- Más eficientes, que las funciones, ya que en memoria solo se almacena el valor devuelto


- **yield from**, simplifica el codigo de los generadores cuando se usan bucles anidados, y permite a acceder al subelemento, similar a un array de 2 dimensiones


#### Excepciones
- Es un error en tiempo de ejecucion, de algo inesperado.
- Evita que el programa se detenga
```py
try:
	pass
except Exception e:
	raise e
finally:
```

- Lanzar una excepcion propia con **raise**, en clases POO

#### POO (Programacion orientada a objetos)
- Objetos de la vida real pasar al codigo de programacion
- Metodos (funciones) y atributos (propiedades)
- Se puede modularizar el codigo (dividir)
- Es muy reutilizable a través de Herencia
- El programa no cae si hay fallos.
- Encapsulamiento
- Polimorfismo
- Clase, Objeto, Instancia de clase, Modularizacion, Encapsulamiento, Herencia, Polimorfismo

- **Clase**: modelo donde se redactan las caracteristicas comunes de un grupo de objetos (ej, chasis, ruedas)
- **Instancia de clase**: objeto perteneciente a una clase (ej. coche1, coche2 con caracteristicas comunes de la clase y propias de cada objeto)
- Modularizacion: en app complejas pueden estar formadas por varias clases en donde cada modulo o clase tiene sus caracteristicas y funciones particulares, funcionan de manera independiente
- **Encapsulamiento**: funcionan de manera independiente aislados del exterior y nada sabe del funcionamiento interni de otra clase, 
- **Metodos de acceso**: permiten conectar las clases entre si a algunas funciones, pero no sabe del funcionamiento interno de la otra clase.

Para acceder se usa la nomenclatura del punto (objeto.propiedad, objeto.metodo())

- **Herencia**: se trata de trasladar la herencia de una clase a otra a traves de jerarquias (abuelo con casa, padre con coche, hijos con moto, etc)
  - Clase 1 (clase padre de clase 2 o superclase)
  - Clase 2 (sublase de clase 1 y clase padre de clase 3,4,5 o superclase de ellos)
  - Clase 3 - Clase 4 - Clase 5

Permite reutilizar clases similares, por medio de las caracteristicas y comportamientos en comun que comparten y englobarlos en una superclase o clase padre


#### Modulos

- Archivo con extensión .py, .pyc (python compilado), posee su propio espacio de nombres, con variables, funciones, clases e incluso oros módulos.

- Sirven para organizar y reutilizar el codigo (modularizacion, escribir en partes para poder reutilizarlo), ademas de facil mantenimiento, funcionan como un rompecabezas.

#### Paquetes

- Directorios donde se almacen los módulos relacionados entre sí.
- Sirven para organizar y reutilizar los módulos.
- Para crear paquetes, se crea una carpeta que incluye un archivo **__init__.py**

#### Paquetes distribuibles

- Se pueden empaquetar y enviarlo
- Instalar el paquete para luego utilizarlo, desde cualquier directorio

- Crear archivo **setup.py**, con una descripcion de lo que va a contener el paquete
```py
from setuptools import setup

setup(
	name="paquetecalculos", #nombre del paquete 
	version="1.0.0",
	description="Paquete de redondeo y potencia",
	author="Juan",
	author_email="cursos@pil.com",
	url="www.pil.com",
	#mas importante que se quiere empaquetar
	packages=[
		"calculos",
		"calculos.redondeo_potencia"
	] 

)
```

- Ejecutar desde la consola el archivo setup.py
```sh
cd C:\Users\VBox_da\Documents\aiuta\Lenguajes\Python\Curso

python setup.py sdist
```

- Crea dos carpetas
  - paquetecalculos.egg-info
  - dist

> En la carpeta dist se encuentra el paquete distribuible **paquetecalculos-1.0.0.tar.gz**

- Para instalar el paquete, ir al directorio donde esta el paquete
```sh
cd C:\Users\VBox_da\Documents\aiuta\Lenguajes\Python\Curso\dist

pip install paquetecalculos-1.0.0.tar.gz

#o pip3 si es python 3
```

- Desinstalar un paquete
```sh
#desde cualquier lugar
pip uninstall paquetecalculos
```



Acutalizar PIP
```sh
python -m pip install --upgrade pip
```

#### Gestión de Archivos Externos

- Para tener persistencia de datos
- Permiten intercambio
- Con el modulo estandar de Python **io**

- Hay diferentes tipos de archivos (texto plano, binario)
- Fases para guardar en archivos externos
1. Crear
2. Abrir **open()**
3. Manipular **read()**, **write()**, **readlines()**, **writelines()**
4. Cerrar **close()**

- Modos de apertura r=lectura, w=escritura vaciando el contenido al abrir, a=agregar contenido al final de un archivo existente
```py
f = open("ruta", "modo")

# Modos de apertura
## Leer
r
r+ (lee/escribe) - conserva el contenido

## Escribir
w
w+ (lee/escribe) - suprime el contenido

## Anexar
a
a+ (lee/escribe) - conserva el contenido

## Binario
b
Abre en modo binario. Además de r, w, a

## Universal
U
Utiliza el traductor universal de nueva línea a /n, Además de r, w, a
Ya que las aplicaciones pueden utilizar caracteres diferentes para el salto de linea
/r
/n
/r /n
```

Leer archivos de una sola vez a la memoria
```py
file = open("rutaArchivo", "r")
contenido = file.read() # almacena en una cadena todo el contenido

listaArchivo = file.readlines() # almacena cada linea en una lista

file.close()
```

Escribir datos en un archivo
```py
file = open("rutaArchivo", "w")
file.write(contenido) # escribe una cadena en el archivo

file.writelines(listaConContenido) # escribe cada elem de la lista en una nueva linea del archivo

file.close()
```

##### Gestión de archivos delimitados
- Con el uso del método **split()**
```py
f = open("archivo.txt", "r")
lista = f.readlines()

for x in lista:
	values = x.split(",")
	lat = float(values[0])
	lon = float(values[1])
	dint = int(values[8])
```

- Con el módulo **csv**
Permite leer correctamente, y que los archivos pueden variar según la aplicación que los crea. También permite escribir
```py
# Leer, con objeto reader(file)
import csv
import sys

f = open("archivo.csv", "r")
try:
	reader = csv.reader(f) # lee un archivo csv
	for row in reader:
		print row #lista con los elementos de la linea
finally:
	f.close()

#######################################################
# Escribir, con objeto writer(file) y funcion writerow(tupla_de_valores_para_guardar_en_una_linea)
import csv
import sys

f = open("archivo.csv", "wt")
try:
	writer = csv.writer(f) # genera un archivo csv
	writer.writerow( ("Col1", "Col2", "Col3") )
	for i in range(10):
		writer.writerow( (i+1, chr(ord("a")+i), "10/%02d/11" % (i+1)) )
finally:
	f.close()

print open("archivo.csv", "rt").read()
```

#### Serialización

- Guardar en un archivo externo codificado en codigo binario, colecciones, diccionarios y objetos
- Para distribuir, almacenar en disco o base de datos
- Se utiliza la biblioteca **Pickle**
  - **dump()** vuelca datos al fichero binario externo
  - **load()** carga los datos del fichero binario externo