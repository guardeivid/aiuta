# Instalación de Git

## Debian/Ubuntu

Para la última versión estable para tu release de Debian/Ubuntu
```sh
sudo apt-get install git
```

Para Ubuntu, este PPA proporciona la última versión estable de Git upstream
```sh
sudo add-apt-repository ppa:git-core/ppa 
sudo apt update; sudo apt install git
```

Version
```sh
git --version
```

## Configurando su nombre de usuario  y email Git para todos los repositorio en su computadora
```sh
git config --global user.name "Guardeivid"
git config --global user.email "guardeivid@example.com"
```

Confirmar nombre y usuario
```sh
git config --global user.name
git config --global user.email
```

Para un repositorio individual cambiar al directorio del repositorio local
```sh
git config user.name "Guardeivid"
git config user.email "guardeivid@example.com"
```

Otras configuraciones
```sh
git config --global color.status auto
git config --global color.branch auto
git config --global color.diff auto
git config --global color.interactive auto
```

> Esta información se guardará en un fichero en nuestro directorio home 
> (por defecto **~/.gitconfig**).

```git
[user]
	name = Guardeivid
	email = guardeivid@example.com
[color]
	status = auto
	branch = auto
	diff = auto
	interactive = auto
```
## Operaciones básicas con Git

### Clonar Repositorio de cero desde la web a local 
Importa un repositorio externo dentro del directorio actual
```sh
git clone https://github.com/guardeivid/aiuta.git
```
```
| directorio_actual
  		   |
		   | aiuta
```

### Crear repositorio de cero en local
Crear un directorio y dentro iniciar el gestor de git
```sh
mkdir aiuta
cd aiuta
git init
```

> Operaciones Dentro del proyecto **aiuta** `cd aiuta`

### Agregar archivos nuevos o modificados al índice del repositorio para versionar en el próximo _**commit**_
No incluye las excepciones del archivo _**.gitignore**_
```sh
git add file1 file2 file3
```

O utilizando un comodín para agregar todos los archivos
```sh
git add *
```

### Para saber lo que está pendiente de hacer commit
```sh
git diff --cached
```

### También se puede verificar lo que se añadió al índice del repositorio
```sh
git status
```

### Pasar los cambios a la versión actual del repositorio local con `git commit` (confirma los cambios)
Con *-m* se puede ingresar un mensaje para llevar control de los cambios realizados
```sh
git commit -m 'Subo la estructura del proyecto al repositorio de GitHub'
```

### Una manera rápida de actualizar el repositorio local sin utilizar `git add ...`
Sólo sirve para los archivos modificados, para los nuevos si haty que utilizar `git add ...`
```sh
git commit -a -m 'Cambios en el proyecto'
```

### Subir y unir la nueva versión del repositorio local hacia el repositorio remoto central
> git push [url] [branch]
```sh
git push https://github.com/guardeivid/aiuta.git
```

#### Se puede crear un alias de la URL añadiendo un repositorio remoto
> git remote add [nombre] [url]
```
git remote add origin https://github.com/guardeivid/aiuta.git
git push -u origin master
```

Otros comandos útiles
`git remote` `git remote -v`

### Actualizando repositorio local desde el remoto
```
git pull
o
git pull https://github.com/guardeivid/aiuta.git
```


### Inspeccionando un repositorio remoto
> git remote show [nombre]
```
git remote show origin
```



## Links de interés
- [Pro Git book en español](https://git-scm.com/book/es/v1/)




# Autenticarse con GitHub desde Git
---


# GitHub
---

## Crear un nuevo repositorio

Nombre del repositorio
> auita

Descripción
> Breves ayudas y recordatorios de tareas realizadas

- Público

- Inicialice este repositorio con un README

- Añadir .gitignore

- Agregar una licencia




## Wiki
---

> **Crear la primer página**
