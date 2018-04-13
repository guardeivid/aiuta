### Bash Shell
Obtener archivos bash y dirigirlos por una tuberia a less para que salgan pococ a poco
```sh
locate bash | less

# el primero que aparece es el que se va a usar
# /bin/bash
```

Crear archivo bash
```sh
mkdir scripts
# se pueden crear varias carpetas en el directorio actual separadas por un espacio

cd scripts
nano primer.sh
```

Editar archivo
```sh
#!/bin/bash
echo Hola Mundo
```
Guardar **Ctrl+o**, Salir **Ctrl+x**

Probar
```sh
source primer.sh
# o 
./primer.sh
```

#### Dar permisos de ejecucion al archivo
```sh
sudo chmod a+x archivo
```

#### Uso de comillas
- Simples: los caracteres especiales son nulos (**\* ; $**)
- Dobles: los caracteres se tienen en cuenta

El punto y coma permite unir en una linea varios comandos
```sh
#!/bin/bash
clear;echo Hola Mundo
```

#### Variables
Las variables no están definidas
- Se declaran sin $
- Se llaman con el $
```sh
nano variables.sh
```

```sh
#!/bin/bash
numero=4
echo $numero + 3

# imprime clear
echo clear

# borra la pantalla
echo $(clear)
```

Operaciones
```sh
nano notas.sh
```

```sh
#!/bin/bash

# pedir ingresar un valor y se guarde en la variable NOTAISO
read -p 'Introduce nota ISO: ' NOTAISO
read -p 'Introduce nota PARE: ' NOTAPARE
read -p 'Introduce nota BD: ' NOTABD

# el corchete es como un doble parentesis
suma=$[ $NOTAISO + $NOTAPARE + $NOTABD ]

# guardar la operacion aritmetica
# de esta manera da un valor entero
let media=suma/3

# numero decimal
media=$( echo " scale=2; $suma/3 " | bc -l )

echo "La media es $media"
```

#### Funciones
```sh
#!/bin/bash
function doble {
	echo "voy a doblar el valor de numero"
	let NUMERO=NUMERO*2
}


NUMERO=3
echo "NUMERO vale : " $NUMERO
doble 	# llamamos a la función
echo '$NUMERO vale : ' $NUMERO
```

```sh
#!/bin/bash
# variables locales y globales
function saludo {
	local NOMBRE="Jose Antonio"
	echo "Hola señor $NOMBRE encantado de conocerle"
}

NOMBRE="Juana"
saludo
echo "En el script principal, mi nombre es $NOMBRE"
```

#### Condicionales

IF...ELIF...ELSE...FI
Para cadenas
```sh
#!/bin/bash
# Edad para votar
edad=19

# dejar espacio entre el if los corchetes y la expresion
if [ $edad -lt 18 ]; then
	echo "No puedes votar"
else
	echo "Puedes votar"
fi
```

#### Varias expresiones en la condicion

if [ expr1 ] && [ expr2 ]; then
fi

if [ expr1 ] || [ expr2 ]; then
fi

#### CASE

```sh
case VARIABLE in
	valor1)
			se ejecuta si VARIABLE tiene el valor1 ;;
	valor2)
			se ejecuta si VARIABLE tiene el valor2 ;;
	*)
			Se ejecuta si VARIABLE tiene otro valor distinto ;;
esac 
```

```sh
VARIABLE=1400
case $VARIABLE in
	110*)
		echo "cadiz capital" ;;
	120*)
		echo "badajoz" ;;
	*)
		echo "no contemplado" ;;
esac 
```