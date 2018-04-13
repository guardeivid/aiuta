### Comandos básicos

#### Cambiar de directorio
```bash
cd ruta_a_carpeta_o_archivo_abosulta_o_relativa

# ir a la carpeta del usuario ~
cd

# ir una carpeta abajo
cd ..

# ir a dos carpetas abajo
cd ../..
```

#### Saber en que directorio me encuentro
```bash
pwd
```

#### Crear directorios
```sh
mkdir scripts

# se pueden crear varias carpetas en el directorio actual separadas por un espacio
```

#### Crear archivos
```bash
touch [ruta/]nombrearchivo

# o directamente usando un editor, si el archivo no existe
[sudo] nano|vim|emacs [ruta/]nombrearchivo
```

##### Controles de *`nano`*
- Para *guardar* **Ctrl+O** luego **Enter**.
- Para *salir* **Ctrl+X**.
- *Buscar* texto **Ctrl+W**, y luego posiciona en la primera aparicion del texto buscado.
- Para *cortar* una línea donde se está posicionado **Ctrl+K**
- Para *pegar* una línea cortada o copiada **Ctrl+U**
- Para *copiar* la línea actual **Mayus+Ctrl**
- Mostrar *manual* **Ctrl+G**
- Ir página siguiente **Ctrl+V**
- Ir página anterior **Ctrl+Y**

Establecer editor por defecto
```bash
expot EDITOR="nano"
```

#### Listar archivos y carpetas en el directorio actual
```bash
ls

# se puede obtener mayor detalle sobre propietarios y permisos
ls -l
```

#### Copiar, Mover, Eliminar archivos
```bash
# Copiar
cp <ruta_archivo_a_copiar> <ruta_a_carpeta_destino>

# Mover
mv <ruta_archivo_a_mover> <ruta_a_carpeta_destino>

# Eliminar
rm <ruta_archivo_a_eliminar>
```

### Comandos extras del sistema

#### Apagar PC
```bash
shutdown

# cancelar apagado
shutdown -c

init 0
```

#### Reiniciar PC
```bash
reboot
```

#### Ver el espacio en discos duros
```bash
df

# se puede ver el % ocupado en cada particion, por ejemplo en /
```

#### Ver el estado de utilización de memoria RAM y SWAP (memoria temporal, recomendable minimo 2GB)
```bash
free
```

### Permisos a archivos y carpetas

#### Dar permisos de ejecucion al archivo
 x=ejecucion
 r=lectura
 w=escritura

 -rwx-xr-x  nombreusuario nombregrupo

 Primeros 3 son los permisos del usuario
 Segundos 3 son los permisos del grupo
 Terceros 3 son los permisos de otros usuarios

 Cambio de permisos para ejecutar archivos
##### Modo octal
r=4, w=2, x=1

```sh
# para cambiar permisos debe ser el superusuario
sudo su

# Permiso de lectura para todos los usuarios
chmod 444 nombrearchivo

# Permiso lectura-escritura para usuario actual y a otros lectura
chmod 644 nombrearchivo

# Permiso total a todos
chmod 777 nombrearchivo

# ejecucion a todos unicamente
chmod 111 nombrearchivo

```

##### Con letras
u=usuario, g=grupo, o=otros, a=todos

Operadores
+ agrega, - quita, = asigna un permiso

```sh
# para cambiar permisos debe ser el superusuario
sudo su

# lectura a usuario actual
chmod u=r nombrearchivo

#todos total
chmod a=rwx nombrearchivo

# quitar lectura a todos con -
chmod a-r nombrearchivo

# agregar un permiso y dejar lo que ya tiene actualmente
chmod a+r nombrearchivo
```


##### setuid
Agregar permisos de superusuario a un usuario
```sh
# para cambiar permisos debe ser el superusuario
sudo su

# agregar permisos de superusuario a un archivo
chmod u+s /sbin/fdisk

# quitar permisos
chmod u-s /sbin/fdisk

chmod 4700 nombrearchivo
```

##### setgid
Agregar permisos de superusuario a un grupo
```sh
# para cambiar permisos debe ser el superusuario
sudo su

# agregar permisos de superusuario a un archivo
chmod g+s /sbin/fdisk

# quitar permisos
chmod g-s /sbin/fdisk

chmod 2700 nombrearchivo
```

##### sticky
Deniega que otros usuarios puedan borrar lo que ha modificado un usuario por mas que tengan permisos de escritura
```sh
# para cambiar permisos debe ser el superusuario
sudo su

# agregar permisos de superusuario a un archivo
chmod o+t /sbin/fdisk

# quitar permisos
chmod o-t /sbin/fdisk

chmod 1777 nombrearchivo
```

### Cambio de dueño de un archivo o carpeta
```bash
chown -R nombre_usuario[:nombre_grupo] archivo carpeta ...
```

### Usuarios

Cambio de usuario
```bash
sudo su [nombre_usuario]
```

Sin especificar el **nombre_usuario** cambia a **`root`**.

Para cerrar la sesión
```bash
exit
```


#### Cambio de contraseñas
```bash
sudo passwd [nombre_usuario]

sudo passwd root
# ahora se puede ingresar a root con
su
# ingresar la contraseña

# Eliminar contraseña, es recomendable que no tenga
sudo passwd -l root
```

#### Que usuario soy
```bash
whoami
```

Para usuarios *normales* aparece **`$`**.
Para usuario *root* aparece **`#`**

#### Ver manual
```bash
man [applicacion]

# salir
q
```

### Enlaces simbólicos (accesos directos)
```bash
ln -s ruta_absoluta_del_archivo_o_carpeta ruta_absoluta_a_link

ln -s /home/usuario/carpeta/ejemplo /home/usuaio/link
ls
# se muestra de color celeste
```
