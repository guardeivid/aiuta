## Laravel 5.5 LTS

Requerimientos

PHP >= 7.1.3

OpenSSL PHP Extension

PDO PHP Extension

Mbstring PHP Extension

Tokenizer PHP Extension

XML PHP Extension

#### Verificar versión de php instalada
>php -v


### Composer 
> Instala dependencias de PHP y actualizaciones de seguridad en un proyecto
<https://getcomposer.org/download/>

#### Instalación de Composer
```sh
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
php -r "if (hash_file('SHA384', 'composer-setup.php') === '544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
php composer-setup.php
php -r "unlink('composer-setup.php');"
```

Comprobar con
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


### Instalar programaticamente en Unix
El instalador contiene una firma que cambia, para eso se ouede usar un scrpt
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

### En Windows
Descargar y correr [Composer-Setup.exe](https://getcomposer.org/Composer-Setup.exe)


## Instalación de Laravel localmente
Con Composer se instala Laravel, dentro del directorio actual

```
composer create-project --prefer-dist laravel/laravel nombre-proyecto
```
La opción **--prefer-dist** descarga los archivos del repositorio de distribución

```
cd nombre-proyecto
php artisan serve
```
Inicia un servidor de desarrollo (http;//127.0.0.1;8000/)
> Con **Ctrl + C** cierra el servidor

## Instalación de Laravel globalmente

```
composer global require "laravel/installer"
```

Luego agregar la ruta a la variable de entorno PATH

- En Linux se puede definir en **`~/.bashrc`** o **`~/.bash_profile`** donde la ruta a añadir al final de lo que tiene asignado la variable es: **:$HOME/.composer/vendor/bin**
```
touch ~/.bash_profile
nano ~/.bash_profile
```
Y dentro escribir
```
export PATH=/usr/local/bin:$HOME/.composer/vendor/bin:$PATH
```
Guardar con **Ctrl + X** luego **Y** y despues **ENTER**
> **En Ubuntu** el PATH es $HOME/.config/composer/vendor/bin en vez de $HOME/.composer/vendor/bin

Reiniciar consola
```
source ~/.bash_profile
```

- En Windows agregar **;%UserProfile%\AppData\Roaming\Composer\vendor\bin**


Ahora para crear desde cualquier directorio se puede ejecutar y crear un proyecto

```
laravel new nombre-proyecto
```

Eliminar proyecto desde el directorio padre
```
rm -rf nombre-proyecto
```

## Instalar una versión específica

```
composer create-project larave/laravel nombre-proyecto "5.5.*"
```


### Configuración

Habilitar **mod_rewrite**

El **patrón de diseño Front Controller** consiste en que un solo componente de la aplicación es el responsable de manejar de todas las peticiones HTTP que ésta recibe. Es decir, hay un solo punto de acceso para todas las peticiones.

A través del archivo **index.php** que se encuentra en el directorio **public**. Con el servidor web Apache, el archivo **.htaccess** se encarga de redirigir todas las peticiones a **index.php**



Muestra las vistas que están dentro de **resources/views/**, utilizando la extensión **.blade.php** ej **welcome.blade.php**


### Rutas
Las URL se especifican en **routes/web.php** para la web o en **web.php** para la api

Se específican tantas como sean necesarias
> Clase *Route* que llama al método HTTP, (**get, post, any**)
```php
Route::get('/', function () {
    return view('welcome');
});
```

#### Rutas de múltiples tipos que apuntan a la misma URL

```php
Route::get('user', function () {
    return "foo";
});
 
Route::post('user', function () {
    return "bar";
});
```

#### Rutas con parametros
Las rutas se leen de arriba para abajo y cuando coincide con una especificada retorna su función anónima.
```php
Route::get('/usuarios/{id}', function ($id) {
    return "Detalles del usuario: {$id}";
});
```
Los parametros dinámicos deben estar encerrados entre llaves `{}`

La URL para llamar puede ser http://127.0.0.1:8000/usuarios/1

Ahora si se crea la siguiente ruta abajo
```php
Route::get('/usuarios/nuevo', function ($id) {
    return "Detalles del usuario: {$id}";
});
```
Se crea un error porque nuevo puede ser el id, entonces llama a la primer ruta y no a la segunda.

- Se puede solucionar indicando una condición con **`where`** de que el id sea solamente numérico con una expresión regular ej **\d+**
```php
Route::get('/usuarios/{id}', function ($id) {
    return "Detalles del usuario: {$id}";
})->where('id', '[0-9+]');
```
> El **where** puede pasarse un array de variable, expresion regular 
> ->where(['id', '\w+'])

- Otra opción es colocar las rutas más específicas estén declaradas al principio del archivo

#### Parámetros opcopnales
Se indica agregando el caracter `?` despúes del nombre del parámetro, y debe indicarse un valor por defecto en la función
```php
Route::get('saludo/{name}/{nickname?}', function ($name, $nickname = null) {
    if ($nickname) {
        return "Bienvenido {$name}, tu apodo es {$nickname}";
    } else {
        return "Bienvenido {$name}, no tienes apodo";
    }
});
```


Si uno esc