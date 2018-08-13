

### Crear clave pública-privada
```sh
ssh-keygen -t rsa -b 4096 -C 'xxx'

# Generating public/private rsa key pair.
Enter file in which to save the key (/c/Users/<user>/.ssh/id_rsa): /c/Users/<user>/.ssh/id_rsa_xxx

Enter passphrase (empty for no passphrase): ******
Enter same passphrase again: ******
Your identification has been saved in /c/Users/<user>/.ssh/id_rsa_xxx.
Your public key has been saved in /c/Users/<user>/.ssh/id_rsa_xxx.pub.
The key fingerprint is:
SHA256:4aExV64JEKu0EN6OO7L7WL0NHrW7qxb2rNrTBIowE0M prod
The key's randomart image is:
+---[RSA 4096]----+
|+E. +.o . .      |
|o. = = . o       |
|..o + + +        |
|oo +. .* o       |
|+o..oo..S        |
|oo+..+= +        |
| +..o=oo .       |
|. . o=. .        |
| ooo+ooo.        |
+----[SHA256]-----+

```

### Agregar clave publica al servidor remoto en ~/.ssh/authorized_keys
Con la opción **-n** simula la operación pero no la realiza
```sh
ssh-copy-id -i ~/.ssh/id_rsa_xxx.pub -n <username>@<host> -p <port>
```
> **-i** especifica la clave publica, por defecto es ~/.ssh/id_rsa.pub

> **host** direccion ip o nombre de dominio


### Configuración previa 
Para retener la configuracion se guarda en `~/.ssh/config`.

```sh
cd ~/.ssh/
touch config
```

Al archivo agregar
```config

Host <host>
	HostName                <host>
	Users/<user>/           <username>
	PubkeyAuthentication    yes
	IdentityFile 			~/.ssh/id_rsa_xxx
	TCPKeepAlive 			yes
	IdentitiesOnly 			yes
	Port					<port>
```


### Conectarse por Git Bash a server
```sh
ssh <username>@<host> -p <port>

# Al estar en el archivo config ahora se puede conectar directamente con
ssh <host>
```



### Deploy automático
En Home crear un repositorio sin el `workspace` porque no se va a modificar desde acá.
```sh
cd ~
mkdir -p <root-folder>/<repository-name>.git
cd <root-folder>/<repository-name>.git
git init --bare
```

### Crear script para deploy
En hooks se encuentran las tareas que realiza el repositorio. Con **post-receive** se ejecutará cuando se haga un push a éste repositorio de éste servidor.
```sh
cd hooks
nano post-receive
```

Escribir
```config

```

Permisos de ejecución al script
```sh
chmod +x post-receive
```


#### Agregar el servidor remoto
Desde local
```sh
git remote add origin ssh://<username>@<host>:<port>/home/<username>/<root-folder>/<repository-name>.git
```

Probar push
```sh
git push --set-upstream origin master
```


---

### Conectarse a GitLab
Activar `ssh-agent`.

```sh
eval $(ssh-agent -s)
```

Agregar la clave al registro de SSH
```sh
ssh-add ~/.ssh/id_rsa_xxx
```

Para retener la configuracion se guarda en `~/.ssh/config`.
Si no existe el archivo se crea
```sh
cd ~/.ssh/
touch config
```

Al archivo agregar
```config
# GitLab.com server
Host gitlab.com
	HostName                gitlab.com
	Users                   git
	PubkeyAuthentication    yes
	IdentityFile 			~/.ssh/id_rsa_xxx
	TCPKeepAlive 			yes
	IdentitiesOnly 			yes
```

Copiar la clave publica en el repositorio
```sh
cat ~/.ssh/id_rsa_xxx.pub | CLIP
```

Ir a <https://gitlab.com/<username>/<repository-name>/settings/repository>
Luego a **Repository** -> **Deploy Keys** -> **Add key**



Desde el proyecto local
```
git push origin_gitlab
```


### Para GitHub

```sh
ssh-keygen -t rsa -b 4096 -C 'github'
Enter file in which to save the key (/c/Users/<user>/.ssh/id_rsa): /c/Users/<user>/.ssh/id_rsa_xxx

eval $(ssh-agent -s)

ssh-add ~/.ssh/id_rsa_xxx
```

```config
# GitHub.com server
Host github.com
	HostName                github.com
	User                    git
	PubkeyAuthentication    yes
	IdentityFile 			~/.ssh/id_rsa_xxx
	TCPKeepAlive 			yes
	IdentitiesOnly 			yes
```

Copiar la clave publica en el repositorio
```sh
cat ~/.ssh/id_rsa_xxx.pub | CLIP
```

Probar conexion
```sh
ssh -T git@github.com
```




### Tener multiples Host en origin para push únicamente

Agregar a origin 
```sh
git remote set-url --add --push origin git@github.com:<usergithub>/<repository-name>.git
git remote set-url --add --push origin git@gitlab.com:<usergitlab>/<repository-name>.git
```

Para eliminar
```sh
git remote set-url --delete --push origin git@github.com:<usergithub>/<repository-name>.git
```
<https://mirrors.edge.kernel.org/pub/software/scm/git/docs/git-remote.html>