Xdebug soporta hasta la versión 7.4.20
[https://xdebug.org/docs/compat]

ms4w tiene instadado la versión 7.4.13

Descargar el archivo con la version 3.0.4 ts  [https://xdebug.org/files/php_xdebug-3.0.4-7.4-vc15-x86_64.dll]
Y renombrarlo a php_xdebug.dll

Pegarlo en la carpeta `C:/ms4w/Apache/php/ext`

Agregar en `C:/ms4w/Apache/cgi-bin/php.ini`

```ini
[xdebug]
zend_extension=php_xdebug.dll
;xdebug.remote_autostart=1
;xdebug.remote_enable=1
xdebug.mode=debug
xdebug.client_host=127.0.0.1
xdebug.client_port=9003
xdebug.start_with_request=trigger
```

Reiniciar Apache
