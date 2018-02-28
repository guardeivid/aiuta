# Deploy

## Local

#### Conectar a maquina remota
```
ssh root@139.59.20.85
Entre password:
```

#### Salir SSH
```
root@remoteserver:~# exit
```

#### Crear Clave publica-privada desde local
```
ssh-keygen -t -rsa -b 4096 -C 'anyIdentifyer'
Enter file (~/.ssh/id_rsa): ~/.ssh/id_rsa_server
Enter passphrase:
```

```
aiuta@localserver:~# cd ~/.ssh
ls
id_rsa_server	id_rsa_server.pub
```

Copiar en el portapapeles la clave publica para despues pegarla en remoto (**pbcopy** funciona sólo en Mac)
```
cat id_rsa_server.pub | pbcopy
```

## Remoto
```
root@remoteserver:~#
ll
cd ~/.ssh
ll
vim authorized_keys
```

Pegar en el archivo el contenido de la clave publica al principio del archivo

Escape para salir del modo insert y wq para guardar y salir de vim
```
:wq
```

```
exit
#(sale del remoto)
```

## Local
Probar conexion via SSH a remoto desde local, llamando con el parametro **`-i`** y la clave privada
```
aiuta@localserver:~# ssh -i ~/.ssh/id_rsa_server root@139.59.20.85
```

## Remoto

#### Agregar usuario que se puede conectar via SSH
```
sudo adduser aiuta
Enter new password:
```

#### Cambiar de usuario a aiuta
```
root@remoteserver:~# sudo su aiuta
aiuta@remoteserver:~# cd
```

#### Volver a root
```
sudo su root
# aiuta no esta en el archivo sudoers
```

Salir del usuario y vuelve al usuario anterior, para poder incluir en sudoers a aiuta
```
exit
```

Agregar usuario a sudoers
```
root@localserver:~# sudo usermod -aG admin aiuta
```

```
sudo su aiuta
aiuta@localserver:~# ll
mkdir .ssh
cd .ssh
vim authorized_keys
```
Pegar clave publica copiada con **`cat id_rsa_server.pub | pbcopy`** desde *local* y salir de vim **`esc :wq`**

Salir de remoto
```
exit
```

Probar conexion via SSH a remoto desde local, llamando con el parametro -i y la clave privada ahora con el usuario aiuta
```
aiuta@localserver:~# ssh -i ~/.ssh/id_rsa_server aiuta@139.59.20.85
```

#### Hacer que solo se puede conectar aiuta
Editar archivo **sshd_config**
```
aiuta@remoteserver:~# sudo vim /etc/ssh/sshd_config
```

```
PermitRootLogin no
...
PasswordAuthentication no
```

Para guardar y salir de vim `esc` y `:wq`

Reiniciar SSH
```
sudo service ssh restart
```

------------------------------------------
## Instalar LEMP (php nginx, mysql, git) en remoto

## Remoto
Loguearse en el server
```
aiuta@localserver:~# ssh -i ~/.ssh/id_rsa_server aiuta@139.59.20.85
```

Actualizar listas de repositorios
```
sudo apt-get update
```

Ver si esta instalado php
```
php -v
# o
sudo apt cache search php
```

#### Para instalar PHP 7.2 hay que agregar repositorio
```
sudo apt-add-repository ppa:ondrej/php

sudo apt-get update
# GPG Error la siguiente firma no se pudo verificar
```

#### Solucionar el problema agregar otro repositorio
```
sudo add-apt-repository ppa:nilarimogard/webupd8
sudo apt-get update
sudo apt-get install launchpad-getkeys
```

Correr el programa
```
sudo launchpad-getkeys
```

#### Ahora si ya se puede obtener el certificado firmado y se podra instalar
```
sudo apt-get update
```

#### Instalar PHP 7.2
```sh
sudo apt-get install php7.2-cli php7.2-fpm php7.2-mbstring php7.2-mysql php7.1-mcrypt php7.2-curl
# Chequear
php -v
```

#### Instalar MySQL
```
sudo apt-get install mysql-server
Password para root:
```

Chequear si es correcta la instalacion
```
mysql -u root -p
Enter password: ******

mysql> SHOW DATABASES;
exit;
```

#### Instalar NGINX
```
sudo apt-get install nginx
```

#### Instalar git
```
sudo apt-get install git
git --version
```

#### Instalar zip y unzip
```
sudo apt-get install zip unzip
```

Se puede hacer todo en una sola linea
> sudo apt-get install git zip unzip ...

--------------------------------------------------------------

Instalar Laravel via GitHub

## Ir a GitHub
> New repository <br>
> Propietario		Nombre del repositorio <br>
> aiuta	/	deploy<br>
> Create repository<br>

## En local
```
cd
mkdir desktop
cd desktop
```
#### Crear proyecto laravel
```
laravel new deploy
cd deploy
```
#### Iniciar git
```sh
git init
git add .
git commit -m "First commit"
```
#### Enviar a GitHub
```
git remote add origin git@github.com:{github-username}/{repository-name}.git
git push -u origin master
```

## Remoto
En remoto es necesario crear claves para conectarse a github
```sh
aiuta@remotoserver:~# ssh -i ~/.ssh/id_rsa_server aiuta@139.59.20.85
```

Crear clave
```sh
ssh-keygen -t -rsa -b 4096 -C 'github'
cat ~/.ssh/id_rsa.pub
```

Seleccionar la clave publica para pegarla en github

## En GitHub

Dentro del proyecto *aiuta/deploy* ir a Settings -> Deploy keys -> **Add deploy key**

1. Titulo
2. Key (pegar la clave publica generada en remoto)
3. Allow write access, permite hacer push desde remoto a github, no seleccionarlo
4. Add key

## Remoto

#### Comprobar si desde remoto accede a GitHub
```
ssh -T git@github.com
# o
git -T git@github.com
```

#### Clonar repositorio de GitHub en remoto con el nombre de html
> git clone git@github.com:{github-username}/{repository-name}.git html

```
git clone git@github.com:aiuta/deploy.git html
```
```
cd html
ll
```

Verificar si esta instalado composer
```
composer
# (no esta instalado)
```

#### Instalar Composer
```sh
curl -sS https://getcomposer.org/installer | sudo php -- --install-dir=/usr/local/bin --filename=composer
```

Chequear
```
composer
composer -v
```

#### Instalar composer en el proyecto ya que git no sube la carpeta vendor, y por lo tanto no esta en GitHub
```
:~/html $ composer install --no-dev
# (no-dev se usa en produccion)

ll
```
#### Cambiar archivo de configuracion de variables de entorno *.env.example* a *.env*
```sh
cp .env.example .env
```

#### Crear una clave para el proyecto de laravel
```
php artisan key:generate
```

------------------------------------

## Configurando nginx para laravel

## Remoto

Editar el archivo del servidor web
```
cd /etc/nginx
sudo vim sites-available/default
```

```config
server{

	root /var/www/html/public;
	
	index index-html index.htm index.php;
	
	location / {
		try_files $uri $uri/ /index.php$is_args$args;
	}
	
	location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/run/php/php7.2-fpm.sock;
    }
```
Salir de vim **esc** y **:wq**

#### Mover el proyecto de la carpeta *~/html* a la carpeta del servidor web */var/www*
Eliminar el contenido de la carpeta que viene por defecto
```
rm -rf /var/www/html
```

Mover
```
sudo mv ~/html /var/www/
```

#### Reiniciar nginx
```
sudo service nginx restart

# si hay error se puede usar
nginx -t
```

#### Cambiar permisos de la carpeta *storage*
```
sudo chmod -R 777 /var/www/html/storage
```

Chequear en el navegador si funciona correctamente


### Verificar y actualizar proyecto desde carpeta del servidor web en produccion
```
cd /var/www/html
git pull
```

----------------------------------------------------------

## Conectar a la Base de Datos

## Remoto

#### Ingresar al servidor MySQL y crear una base de datos
```
mysql -u root -p
Enter password: ******

mysql> CREATE DATABASE tutorial;

#Salir de mysql
exit;
```

#### Ir a la carpeta del proyecto
```
cd /var/www/html
```

#### Editar el archivo .env
```
sudo vim .env
```

En el archivo modificar los parametros de conexion, con la **`i`** entra en modo de inserccion
```config
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=tutorial
DB_USERNAME=root
DB_PASSWORD=123456
```
Salir con **esc** y **wq**

#### Crear *auth* de laravel (opcional)
```
php artisan make:auth
```

#### Migrar tablas del proyecto laravel a la base de datos
```
php artisan migrate
```


Link
- <https://bitfumes.com/blog/server/logging-into-digital-ocean-droplet-ssh>
