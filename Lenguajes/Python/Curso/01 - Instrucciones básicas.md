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

