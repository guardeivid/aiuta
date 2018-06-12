# PSR-4

## Composer

### Instalación

[1- Instalacion Composer.md](1- Instalacion Composer.md)

### Crear proyecto Composer

#### Si no existe el directorio
[https://getcomposer.org/doc/03-cli.md#create-project](https://getcomposer.org/doc/03-cli.md#create-project)
```sh
composer create-project [options] nameproject
```

#### Si existe el directorio y no hay inicializado un proyecto composer
[https://getcomposer.org/doc/03-cli.md#init](https://getcomposer.org/doc/03-cli.md#init)

```sh
composer init
```

Y luego instalar
[https://getcomposer.org/doc/03-cli.md#install](https://getcomposer.org/doc/03-cli.md#install)
```sh
composer install
```

#### Si existe el directorio y ya hay inicializado un proyecto composer, solo hay que instalar las dependencias
Ya existe un archivo `composer.json`

```sh
composer install
```
### Incorporar autoload psr-4 en composer.json

En `composer.json`
```json
    "autoload": {
        "psr-4": {
            "NameSpace\\": "DirName/" [, "NameSpace\\": "DirName/"]
        }
    }
```

### Generar el array en autoload_psr4.php
[https://getcomposer.org/doc/03-cli.md#dump-autoload-dumpautoload-](https://getcomposer.org/doc/03-cli.md#dump-autoload-dumpautoload-)
```sh
composer dump-autoload
```

> Si se modifica el archivo `composer.json` en la sección **autoload**, se debe volver a ejecutar esta instrucción.

## PHP

### Crear directorio donde alojar la lógica de la applicación (*DirName*)
> Generalmente se usa **lib**, **src**, **app**, etc.

```
-NombreProyecto
 |-src
 | |-Subcarpeta1
 | |   |-Archivo1a.php
 | |   |-Archivo1b.php
 | |-Archivoa.php
 |
 |-vendor
 | |-autoload.php
 | |-composer
 |   |-autoload_*.php
 |
 |-www
   |-index.php
```

### Incorporar el espacio de nombres (**`namespace`**) en cada archivo de src
`src/Archivoa.php`

```php
<?php

namespace NameSpace;

class Archivoa {...}
```

`src/Subcarpeta1/Archivo1a.php`

```php
<?php

namespace NameSpace\Subcarpeta1;

class Archivo1a {...}
```

`src/Subcarpeta1/Archivo2a.php`

```php
<?php

namespace NameSpace\Subcarpeta1;

class Archivo2a extends Archivo2a {...}
```

### Si una clase extiende de otra clase, o si se utiliza otra clase en ella se debe llamar con (**`use`**)
`src/Archivoa.php`

```php
<?php

namespace NameSpace;

use NameSpace\Subcarpeta1\Archivo1a;

class Archivoa {...}
```

`src/Subcarpeta1/Archivo2a.php`

```php
<?php

namespace NameSpace\Subcarpeta1;

use NameSpace\Subcarpeta1\Archivo1a as A1a;

class Archivo2a extends A1a {...}
```
> Se puede utilizar un alias con **as** del nombre de la clase.

### Incluir el **`autoload.php`** en o los archivo/s principal/es que será/n llamado/s, y que clases serán cargadas con **`use`**
`www/index.php`

```php
<?php

require '../vendor/autoload.php';

use NameSpace\Archivo2a;
```