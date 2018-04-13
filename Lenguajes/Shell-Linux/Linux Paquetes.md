### Ayuda
```sh
apt --help
```

### Ver si hay novedades en los repositorios
```sh
sudo apt update
```

### Actualizar paquetes instalados
```sh
sudo apt upgrade
```

### Instalar un paquete
Desde la version 14, **`apt-get`** se puede escribir directamente **`apt`**
```sh
sudo apt-get install <packagename>
```

### Actualizar un único paquete
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

### Instalar paquetes descargados con extensión `.deb`
```sh
sudo dpkg -i <nombre_paquete.deb>
```

Los paquetes se instalan en la carpeta **`/opt`**

### Remover un paquetes instalado con extensión `.deb`
```sh
sudo dpkg -r <nombre_paquete>
```

### Instalar paquetes descargados con extensión `.rpm`
```sh
# convertir en ejecutable
sudo alien <nombre_paquete.rpm>
```

### Instalar paquetes descargados con extensión `.run`
```sh
# Asignar permisos de ejecucion
sudo chmod +x <nombre_paquete.run>

# instalar, normalmente son asistentes gráficos
sudo <nombre_paquete.run>
```


### Instalar compilando paquetes del código fuente comprimidos en `.tar.gz`
```sh
# Descomprimir archivo
tar -xvf <nombre_paquete.tar.gz>

# Ingresar a la carpeta
cd <nombre_paquete>

# Buscar el archivo de configuración y ejecutarlo
./configure
# en el archivo aca se puede configurar las opciones

# Preparar la instalación
make

# Instalar
sudo make install
```

### Instalar paquetes desde un script `.sh`
```sh
# Asignar permisos de ejecucion
sudo chmod +x <nombre_script.sh>

# Ejecutar
./<nombre_script.sh>
```

### Ejecutar archivos dentro de carpeta `bin`
```sh
# Asignar permisos de ejecucion y
# Ejecutar
./<nombre_archivo>
```