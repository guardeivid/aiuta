### Composer 
> Instala dependencias de PHP y actualizaciones de seguridad en un proyecto
<https://getcomposer.org/download/>

> Repositorio de paquetes PHP
<https://packagist.org/>

#### Instalación de Composer
- Instalar la versión rápidamente
```sh
# Linux
curl -sS https://getcomposer.org/installer | php
mv composer.phar /usr/local/bin/composer

## version de instalacion en web
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
php -r "if (hash_file('SHA384', 'composer-setup.php') === '544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
php composer-setup.php
php -r "unlink('composer-setup.php');"
```

- Comprobar con
```
php composer.phar
```

https://getcomposer.org/doc/00-intro.md

#### Hacerlo global (recomendado)
Mover el archivo y que se ejecute directamente con composer

```
sudo mv composer.phar /usr/local/bin/composer
```

> Ahora desde cualquier directorio se puede ejecutar **composer**
```
composer update
```
Actualiza las dependencias del proyecto


#### Instalar programaticamente en Unix
El instalador contiene una firma que cambia, para eso se puede usar un script
```sh
#!/bin/sh

EXPECTED_SIGNATURE=$(wget -q -O - https://composer.github.io/installer.sig)
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
ACTUAL_SIGNATURE=$(php -r "echo hash_file('SHA384', 'composer-setup.php');")

if [ "$EXPECTED_SIGNATURE" != "$ACTUAL_SIGNATURE" ]
then
    >&2 echo 'ERROR: Invalid installer signature'
    rm composer-setup.php
    exit 1
fi

php composer-setup.php --quiet
RESULT=$?
rm composer-setup.php
exit $RESULT
```

#### En Windows
Descargar y correr [Composer-Setup.exe](https://getcomposer.org/Composer-Setup.exe)

> Problema al instalar en MS4W

- Copiar el archivo **php.ini** a la carpeta **ms4w/tools/php**
```sh
cp \ms4w\Apache\cgi-bin\php.ini \ms4w\tools\php
```


### Iniciar proyecto composer
- Crear un archivo **`composer.json`**, en Node.js está package.json.
Comandos que puedes utilizar con composer:

```sh
composer about
composer archive
composer browse
composer clear-cache
composer config --list
composer create project laravel/laravel
composer depends vendor/package
composer diagnose
composer dump-autoload --optimization
composer global
composer help
composer init
composer install
composer licenses
composer list
composer remove
composer require vendor/package
composer run-script
composer search my keywords
composer self-update
composer show
composer status
composer update
composer validate
```

```sh
composer init
```
Al ejecutar este comando solicitará cierta información que servirá para crear el archivo composer.json, la información requerida es básica para el archivo, como el nombre del paquete, descripción, autor(es), página del proyecto, y las dependencias.
```json
{
   "name": "guardeivid/tutorial-composer",
   "require": {
       "phpmailer/phpmailer": "5.2.*",
       "raveren/kint": "0.9.*@dev"
   }
}
```
En este archivo estamos indicando que nuestro proyecto se llama "guardeivid/tutorial-composer". Siempre se utilizan dos nombres, uno el nick de la empresa o creadores y otro el nombre del proyecto en sí.

Luego con el campo require estamos indicando que vamos a usar dos librerías, por un lado el phpmailer de phpmailer y el kint de ravener con una versión requerida. Por ejemplo en phpmailer declaramos como versión "5.2.*". Eso quiere decir que te instale siempre la versión 5.2.x (la más reciente de la 5.2). Pero podrías haber declarado "5.*". Existen varios operadores para especificar la versión.


```sh
composer install
```
Este comando procesa el archivo composer.json y resuelve las dependencias, normalmente las instala en un directorio llamado /vendor, pero podemos especificar cualquier otro.

```sh
composer update
```
Actualiza las dependencias de tu proyecto a la última versión y también actualiza el archivo composer.lock Esto se puede hacer de varias maneras, imagina que solo quieres actualizar un dependencia en específico, para hacer eso tienes que indicar el nombre del paquete, de la siguiente manera:
```sh
composer update vendor/package another-vendor/another-package vendor-x/package-x

Esto solo actualizará las dependencias especificadas, si quieres actualizar todas las dependencias de un cierto paquete puede ahorrar muchos carateres utilizando un comodín *, de la siguiente manera:
```sh
composer update vendor-x/*

El comando require instala las dependencias especificadas, este lo explicaré más detalladamente en el siguiente tutorial, la sintaxis es la siguiente:
```sh
composer require vendor/package:*

El comando search busca el paquete indicado en Packagist, solo tienes que pasarle el nombre del paquete.
```sh
php composer search monolog

El comando show muestra los paquetes disponibles y también puedes ver los detalles de un paquete en específico. Basta con pasarle un argumento, este tiene que ser el nombre del paquete:
```sh
php composer show vendor/package

Desplegará información como: el nombre del paquete, versiones, el tipo de paquete, el código fuente, el zip del código fuente, licencia, etc.

El comando depends muestra la lista de paquetes de los cuales depende el paquete indicado. Sí, me estoy refiriendo a las librerías de terceros. Muestra los paquetes de tipo require y require-dev
```sh
php composer depends vendor/package

Para asegurarnos que nuestro archivo composer.json está escrito correctamente y que alguno no tendrá errores al descargarlo y tampoco tener problemas al instalar las dependencias, como algún caracter mal escrito, podemos utilizar el comando validate para verificar que todo está correctamente bien.
```sh
php composer validate

Si a menudo realizas cambios en tus dependencias y las has instalado mediante el código fuente del repositorio, el comando status te permite comprobar si has hecho cambios en alguna de ellas, así como el git status nos indica qué archivos hemos modificado, este comando funciona de la misma manera:
```sh
php composer status -v

Si añadimos la opción **-v** nos brinda información más detallada sobre los cambios producidos.
```sh
You have changes in the following dependencies:
vendor/seld/jsonlint:
M README.mdown

El comando self-update actualiza el propio Composer a la versión más reciente, no tienes que realizar ningún otro paso más escribir en la consola lo siguiente:
```sh
php composer self-update

Tendrás disponible la versión más actualizada del manejador.

El comando config te permite editar varias opciones de Composer, tanto en el archivo local del proyecto como en el archivo global.
```sh
php composer config --list

El comando create-project crea un nuevo proyecto, es necesario pasar como parámetros el vendor y package correspondiente. Esto es lo mismo que descargar el proyecto y después ejecutar el archivo composer.json que venga en él, el siguiente ejemplo crea un proyecto de laravel.
```sh
php composer create-project laravel/laravel mi-proyecto

Ahora, si necesitas actualizar tu archivo autoloader porque tienes nuevas clases puedes hacerlo con el comando dump-autoload, es como ejecutar install o update, pero la ventaja es que puedes especificar que se cree un arreglo de todas las clases del proyecto con sus respectivos archivos, de la siguiente manera:
```sh
php composer dump-autoload --optimize

El comando run-script permite ejecutar manualmente alguno de los scripts definidos por algún paquete.
```sh
php composer run-script nombre-script --no-dev

Hemos agregado –no-dev para desactivar el modo de desarrollo.

Utiliza el comando help para ver información sobre el comando solicitado.
```sh
php composer help install
```

El comando remove sirve para eliminar alguna dependencia que ya no utilicemos, de la siguiente manera:
```sh
php composer remove vendor/package

