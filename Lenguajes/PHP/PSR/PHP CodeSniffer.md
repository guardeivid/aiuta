### SublimeLinter
<http://www.sublimelinter.com/en/latest/settings.html>

#### SublimeLinter-php
<https://github.com/SublimeLinter/SublimeLinter-php>

```sh
# Ver el PATH de php
where php
# linux **which php**

# C:\ms4w\tools\php\php.exe
```

- Sublime Text 3 -> Preferences -> Package Settings -> SublimeLinter -> Settings
```json
    "linters":{
		"php": {
                "cmd": "C:\\ms4w\\tools\\php\\php.exe"
        }
	}
```

#### SublimeLinter-phpcs
<https://github.com/SublimeLinter/SublimeLinter-phpcs>
<https://github.com/squizlabs/PHP_CodeSniffer#installation>

```sh
composer global require "squizlabs/php_codesniffer=*"

# Ver el PATH que se debe incluir
composer global config bin-dir --absolute
# C:\Users\VBox_da\AppData\Roaming\Composer/vendor/bin
```

Agregar variable de entorno
- Ir a Equipo (Botón derecho) -> Propiedades -> Configuración avanzada del sistema -> (Opciones avanzadas) Variables de entorno
- (Variables del sistema) Editar PATH -> Agregar ruta separado con **;**

Comprobar que funciona
```sh
phpcs -h
phpcbf -h
```

Instalar **SublimeLinter**
> CMD-Shift-P -> Install Package -> SublimeLinter

Instalar **SublimeLinter-phpcs**
> CMD-Shift-P -> Install Package -> SublimeLinter-phpcs

#### SublimeLinter-phpmd
<https://github.com/SublimeLinter/SublimeLinter-phpmd>
<https://phpmd.org/documentation/index.html>
```sh
composer global require phpmd/phpmd
```

Instalar **SublimeLinter-phpmd**
> CMD-Shift-P -> Install Package -> SublimeLinter-phpmd

#### SublimeLinter-php-cs-fixer
<https://github.com/jhoff/SublimeLinter-contrib-php-cs-fixer>
<https://github.com/FriendsOfPHP/PHP-CS-Fixer>
```sh
composer global require "friendsofphp/php-cs-fixer:>=2.7"
```

Instalar **SublimeLinter-php-cs-fixer**
> CMD-Shift-P -> Install Package -> SublimeLinter-php-cs-fixer

Actualizar
```sh
composer global update friendsofphp/php-cs-fixer
```




---

<http://www.conasa.es/blog/php-codesniffer-sublime-text/>

#### Descargar 
- PHP Code Sniffer <http://pear.php.net/package/PHP_CodeSniffer/download/>
- PHP CS Fixer <https://github.com/FriendsOfPHP/PHP-CS-Fixer> [php-cs-fixer.phar](http://cs.sensiolabs.org/download/php-cs-fixer-v2.phar)
- PHP Beautifier <https://pear.php.net/package/PHP_Beautifier/download>
- PHP Mess Detector `wget -c <http://static.phpmd.org/php/latest/phpmd.phar>`

#### Instalar paquete en Sublime Text 3

- **Preferences** -> **Package Control**: Ingresar **Install Package** -> **[DEPRECATED]PHPCS**

#### Configuración en Sublime Text 3

- **Preferences** -> **Package Settings** -> **PHP Code Sniffer** -> **Settings - User**

```json
	// Rutas para el ejecutable de php:
	"phpcs_php_prefix_path": "C:\\ms4w\\tools\\php\\php.exe",
	"phpcs_php_path": "C:\\ms4w\\tools\\php\\php.exe",

	// Ruta al script de PHP CodeSniffer:
	"phpcs_executable_path": "C:\\ms4w\\tools\\php\\phpcs_dependencies\\PHP_CodeSniffer-3.2.3\\PHP_CodeSniffer-3.2.3\\bin\\phpcs.bat",

	// Ruta a PHP CS Fixer:
	"php_cs_fixer_executable_path": "C:\\ms4w\\tools\\php\\phpcs_dependencies\\php-cs-fixer-v2.phar",

	// Ruta a PHP Beautifier:
	"phpcbf_executable_path": "C:\\ms4w\\tools\\php\\phpcs_dependencies\\PHP_CodeSniffer\\PHP_Beautifier-0.1.15\\PHP_Beautifier-0.1.15\\scripts\\php_beautifier.bat",

	// Ruta a PHP Mess Detector:
	"phpmd_executable_path": "C:\\ms4w\\tools\\php\\phpcs_dependencies\\phpmd\\src\\bin\\phpmd.phar",

	// Otras configuraciones
    "extensions_to_execute": ["php"],
 
    // Extensiones a excluir de la revisión como por ejemplo ["twig.php"]
    "extensions_to_blacklist": [],
 
    // Deseas que se ejecute al guardar el archivo de forma automática ? 
    "phpcs_execute_on_save": true,
 
    // Deseas ver la lista de errores una vez guardado el archivo ?
    "phpcs_show_errors_on_save": true,
 
    // Deseas resaltar los errores ?
    "phpcs_show_gutter_marks": true,
 
    // Deseas ver la lista de errores ?
    "phpcs_outline_for_errors": true,
 
    // Quieres ver los errores en la barra de status ?
    "phpcs_show_errors_in_status": true,
 
    // Quieres ver los errores en el panel de acceso rápido con atajos ? 
    "phpcs_show_quick_panel": true,
```