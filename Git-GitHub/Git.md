#Instalación de Git
---

##Debian/Ubuntu

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
`git --version`

#Configurando su nombre de usuario  y email Git para todos los repositorio en su computadora
```sh
git config --global user.name "Guardeivid"
git config --global user.email "guardeivid@yahoo.com.ar"
```

Confirmar nombre y usuario
```sh
git config --global user.name
git config --global user.email
```

Para un repositorio individual cambiar al directorio del repositorio local
```sh
git config user.name "Guardeivid"
git config user.email "guardeivid@yahoo.com.ar"
```

> Esta información se guardará en un fichero en nuestro directorio home 
> (por defecto **~/.gitconfig**).

```git
[user]
	name = Guardeivid
	email = guardeivid@yahoo.com.ar
[color]
	status = auto
	branch = auto
	diff = auto
	interactive = auto
```

Otras configuraciones
```sh
git config --global color.status auto
git config --global color.branch auto
git config --global color.diff auto
git config --global color.interactive auto
```

##Clonar Repositorio de cero (*crea la carpeta del proyecto dentro del directorio actual*)
```sh
git clone https://github.com/guardeivid/aiuta.git
```

##Crear repositorio de cero
```sh
mkdir aiuta
cd aiuta
git init
```

##Actualizar repositorio desde la web
```sh
cd aiuta
git pull https://github.com/guardeivid/aiuta.git
```


#Autenticarse con GitHub desde Git
---







#GitHub
---

##Crear un nuevo repositorio

Nombre del repositorio
> auita

Descripción
> Breves ayudas y recordatorios de tareas realizadas

- Público

- Inicialice este repositorio con un README

- Añadir .gitignore

- Agregar una licencia




##Wiki
---

> **Crear la primer página**