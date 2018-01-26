## Instalar la distro-estable de **Node.js** en Ubuntu 16.04 

#### Privilegios de `root`
```sh
sudo su -
```

#### Quitar privilegios de `root`
```sh
sudo su <username>
cd
```


### Instalación
```sh
sudo apt-get update
sudo apt-get install nodejs
```


### Instalación del gestor de paquetes
```sh
sudo apt-get install npm
```

Debido a un conflicto con otro paquete, el ejecutable desde los repositorios de Ubuntu se llama __`nodejs`__ en lugar de __`node`__.


## Instalar mediante PPA, para obtener una versión más reciente
Desde el directorio personal
```
cd ~
curl -sL https://deb.nodesource.com/setup_9.x -o nodesource_setup.sh
```

Inspeccionar archivo
```
nano nodesource_setup.sh
```

Ejecutar el script
```
sudo bash nodesource_setup.sh
```

Luego instalar nodejs ynpm (incluido)
```
sudo apt-get install nodejs
```

Para que funcionen algunos paquetes que se compilan es necesario instalar
```
sudo apt-get install build-essential
```

> Alternativamente se puede simplificar en un paso
>
> curl -sL https://deb.nodesource.com/setup_9.x | sudo -E bash -

> Y luego
> sudo apt-get install build-essential







mkdir compartida_win
sudo mount -o uid=1000,gid=1000 -t vboxsf compartida ~/compartida_win

