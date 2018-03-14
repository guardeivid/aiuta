### Actualizar un paquete
```sh
sudo apt-get install --only-upgrade <packagename>
```

### Conocer que versión tiene un paquete antes de instalarlo
```sh
apt show <packagename>
```

### Desinstalar paquete

- Desinstalar paquete
```sh
sudo apt-get remove <packagename>
```

- Borrar archivos de configuración del paquete
```sh
sudo apt-get purge <packagename>
```

- Eliminar del disco los archivos descargados para la instalación
```sh
sudo apt-get clean <packagename>
```

- Paso 1 y 2 en uno
```sh
sudo apt-get --purge remove <packagename>
```
### Ver programas instalados
```sh
dpkg --list
```

