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
Ver comandos disponibles
```sh
git
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
mkdir proyectos
cd proyectos

mkdir aiuta
cd aiuta
```

Crear repositorio
```sh
git init
```

> Operaciones Dentro del proyecto **aiuta** `cd aiuta`

### Ver como se encuentra el repositorio, verificar lo que se añadió al índice del repositorio
```sh
git status
	> branch initial
	> commit initial
	> nothing in commit
```

### Áreas dentro del repositorio

1. Directorio de trabajo
> **`ls`**, si hay archivos modificados, nuevos o eliminados se encuentran en estado no registrado **unstage**
2. Área de Stage (índice)
> **`git add .`**, archivos registrados para ser enviados al próximo commit
3. Commit
> **`git commit`**

### Agregar archivos nuevos o modificados al índice del repositorio para versionar en el próximo _**commit**_
No incluye las excepciones del archivo _**.gitignore**_
```sh
git add file1 file2 file3
```

O utilizando un comodín para agregar todos los archivos
```sh
git add *

# Alternativa
git add .
```

## Mostrar los cambios entre diferentes commits, etc

### Ver los cambios que se han realizado en el directorio de trabajo y el último commit
```sh
git diff
```

### Ver los cambios que se han realizado en el stage y el último commit
```sh
git diff --cached
```

### Ver los cambios que se han realizado entre distintos commits **`git diff <hash> <hash>`**
```sh
git diff f5f0388 b4844be

# De manera relativa
git diff HEAD~1 HEAD
```
>Alt+126 **`~`**


## Guardar los cambios en el repositorio

### Pasar los cambios a la versión actual del repositorio local con `git commit` (confirma los cambios)
```sh
git commit
```
> Muestra un editor para cargar en la primera línea el **`título del mensaje`**

> Se pueden agregar más líneas para colocar una **`descripción`**

> Para guardar si el editor es **`vim`** escribir **`Escape`** y luego **`:wq`**

> Si el editor es **`nano`** escribir **`Ctrl+X`** y luego **`Y`**

Con *-m* se puede ingresar un mensaje para llevar control de los cambios realizados en una sola línea
```sh
git commit -m 'Subo la estructura del proyecto al repositorio de GitHub'
```

### Una manera rápida de actualizar el repositorio local sin utilizar `git add ...`
Sólo sirve para los archivos modificados, para los nuevos si hay que utilizar `git add ...`
```sh
git commit -a -m 'Cambios en el proyecto'
```


## Ver commits realizados

### Muestra información del hash, autor, fecha, título, descripción, rama.
```sh
git log
```

### Muestra información en una sola línea
```sh
git log --oneline
```

### Muestra información en una sola línea con color y nombres de ramas
```sh
git log --oneline --decorate
```

### Muestra información de los commits con dibujos de las bifurcaciones de las ramas
```sh
git log --graph
```

### Muestra información de todos los commits de todas las ramas
```sh
git log --all
```

### Se pueden combinar
```sh
git log --oneline --decorate --graph --all
```


## Deshacer cambios

### Deshacer cambios en el directorio de trabajo (unstage->último commit del archivo)
> Revierte un cambio guardado en el archivo
```sh
git checkout -- <file>
```

### Deshacer cambio del stage al directorio de trabajo (stage->unstage del archivo)
> Revierte un **`git add .`** o **`git add <file>`**

```sh
git reset HEAD <file>

# y luego para deshacer cambios locales
git checkout -- <file>
```

## Deshacer commits de manera destructiva (RESET)
> No es recomendable utilizar **RESET** para deshacer commits en entornos compartidos<br>
> Sólo para deshacer cambios locales, **`git commit`** sin haber realizado **`git push`**

### Deshacer commit (commit->stage)
> Revierte un `git commit` o `git -a commit` a `stage` con los archivos que han sido modificados desde el **HEAD~x** o **hash** pasado por parámetro hasta el HEAD actual

```sh
git reset --soft HEAD~1
# o
git reset --soft <hash>

# para deshacer algún archivo al directorio de trabajo
git reset HEAD <file>

# y luego para deshacer cambios locales
git checkout -- <file>
```

### Deshacer commit (commit->stage->unstage ó directorio de trabajo con cambios locales)
> Revierte un `git commit` o `git -a commit` a `unstage`

```sh
git reset HEAD
# o
git reset <hash>

# y luego para deshacer cambios locales
git checkout -- <file>
```

### Deshacer commit (commit actual->stage->unstage->hasta commit pasado por parámetro)
> Revierte un `git commit` o `git -a commit` a el estado de otro commit pasado por parámetro<br>
> Éste será el nuevo **HEAD**
```sh
git reset --hard HEAD 
# o
git reset --hard <hash>
```


## Deshacer commits de manera no destructiva (REVERT)
> Revierte a un estado anterior realizando un nuevo commit.
> Modifica cada cambio con su contrario para revertirlo, ej si eliminó una línea ahora la agrega como estaba antes

```sh
git revert <hash>
# o
git revert HEAD

# y luego muestra el editor para escribir el mensaje de éste nuevo commit
```

----------------------------------------------------------------

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

#### Crear nueva rama (branch) y cambiar a esa rama
```
git branch branch_tmp [basado en rama_existente]
git checkout branch_tmp
```
Atajo para crear y cambiar a la nueva rama creada
```
git checkout -b branch_tmp
```
> Todo cambio será realizado sobre la rama actual

#### Comprobar en que rama se encuentra
```
git branch
```

#### Comprobar diferencias entre ramas
```
git diff --stat master branch_tmp
```


#### Mezclar archivos de diferentes ramas
Paso 1: En repositorio local, traer los cambios y testearlos
```
git fetch origin
git checkout -b branch_tmp origin/branch_tmp
git merge master
```

Paso 2: Unir **Merge** los cambios y actualizar en repositorio remoto
```
git checkout master
git merge --no-ff branch_tmp
git push origin master
```

#### Eliminar rama
```
git branch -d branch_tmp
```

#### Resolver conflictos
Si se edita un archivo sin antes hacer merge y/o push, en diferentes ramas o de diferentes repositorios (local,remoto)



### Actualizando repositorio local desde el remoto
```
git pull https://github.com/guardeivid/aiuta.git
```

### Ver que cambios se han realizado
```
git log
```

Pero se puede hacer más legible y resumido
```
git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
```

Para no tener que escribir toda esa línea se puede crear un alias y luego llamarla con el nombre del alias `git lg`
```
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
git lg
```

> Para salir del log apretar **`Ctrl`**+**`C`** o **`q`** 


### Ver la url del repositorio remoto asociada a distintos alias `origin` y otros
```
git remote
git remote -v
```


### Inspeccionando un repositorio remoto
> git remote show [nombre]
```
git remote show origin
```

### Eliminado git de un proyecto
```
cd path_proyecto
rm -rf .git
```


## Links de interés
- [Pro Git book en español](https://git-scm.com/book/es/v1/)
- [git - la guía sencilla](http://rogerdudler.github.io/git-guide/index.es.html)
- [practical-git.md](https://gist.github.com/juanghurtado/7a819d4f07619e944b56)
- [Usando git de manera local](http://adrianmoya.com/2012/07/usando-git-de-manera-local/)
- [Usando git de manera remota](http://adrianmoya.com/2013/01/usando-git-de-manera-remota/)

<!--
---
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
-->