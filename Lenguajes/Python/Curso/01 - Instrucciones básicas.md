### Sintáxis básica

Tipos de datos

- Numericos
  - Enteros (int)
  - Decimales (float)
  - Complejos
  - Textos (con comillas simples, dobles, triples)
  - Booleanos (True, False)


Operadores

- Aritméticos (+, -, *, /, **, //, %) (suma, resta, multiplicacion, division, exponente, division entera, modulo)
- Comparación (==, !=, >, <, >=, <=)
- Lógicos (AND, OR, NOT)
- Asignación (=, +=, -=, *=, /=, %=, **=, //=)
- Especiales (IS, IS NOT, IN, NOT IN)

Variable


### Funciones

- Pueden o no devolver valores
- Pueden tener parametros/argumentos
- Tambien se denominan "metodos" si estan definidas en una clase

```py
def nombre_funcion(parametros):
	instrucciones
	return (opcional)

nombre_funcion(parametros)
```

### Listas

- Similar a arrays
- Pueden guardar diferentes tipos de valores
- Se pueden expandir dinamicamente

```py
nombreLista = [elem1, elem2, elem3...]
```
- Se localizan por un indice, comienza a enumerar por 0

Agregar elemento
```py
nombreLista.append(elem)
```

Agregar elemento en un indice determinado
```py
nombreLista.insert(indice, elem)
```

Extender listas
```py
nombreLista.extend( nombreLista2  )
```

Obtener el inidice de un valor, siempre devuelve el primero que encuentra
```py
nombreLista.index( elem )
```

Determinar si un elemento se encuentra en una lista
```py
elem in nombreLista
```

### Tuplas

- Son listas inmutables, no se pueden modificar
- No funciona append, extend, remove
- Permiten extraer una porcion en una nueva tupla

- Mas rápidas
- Menos espacio, mejor rendimiento
- Formatean strings
- Pueden utilizarse como claves en un diccionario (las listas no)

```py
nombreTupla = (elem1, elem2, elem3...)
```

### Diccionarios

- Parecidos a objetos, array asociativos, clave unica:valor
- Los elementos no estan ordenados
- Permiten almacenar cualquier tipo de dato

```py
nombreDiccionario = { clave: valor, ...}
```


### Estructura de control

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
```


##### WHILE
Bucle indeterminado
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

#### Archivos externos

- Para tener persistencia de datos
- Con el modulo estandar de Python **io**

- Hay diferentes tipos de archivos (texto plano, binario)
- Fases para guardar en archivos externos
1. Crear
2. Abrir
**open()**
3. Manipular
**read()**, **write()**, **readlines()**, **writelines()**
4. Cerrar
**close()**

#### Serialización

- Guardar en un archivo externo codificado en codigo binario, colecciones, diccionarios y objetos
- Para distribuir, almacenar en disco o base de datos
- Se utiliza la biblioteca **Pickle**
  - **dump()** vuelca datos al fichero binario externo
  - **load()** carga los datos del fichero binario externo