## Configuracion básica entorno desarrollo en Windows

### Instalar Visual Code

> https://code.visualstudio.com/Download

### Instalar Git
Descargar Git de la página [https://git-scm.com/downloads](https://git-scm.com/downloads), que incluye línea de comandos

1. (Licencia) ***Siguiente***
2. (Seleccionar componentes) ***Siguiente***
3. (Elegir el editor por defecto) y ***Siguiente***
	- [x] nano
	- [ ] vim
	- [ ] notepad++
4. (Ajustar variable de entorno PATH) y ***Siguiente***
	- [x] Git desde Git Bash
	- [ ] Git desde Consola de Windows
	- [ ] Usar Git y opciones UNIX desde la Consola de Windows  
5. (Elegir el ejecutable SSH) y ***Siguiente***
	- [x] Usar OpenSSH 
	- [ ] Usar (Tortoise) Plink
6. (Elegir transporte bakend HTTPS) y ***Siguiente***
	- [x] Usar la librería OpenSSH,
	- [ ] Usar la librería Windows Secure Channel
7. (Configurando el fin de línea de archivos de texto) y ***Siguiente***
	- [x] Estilo Windows (LF->CRLF->LF) 
	- [ ] Estilo Unix (CRLF->LF)
	- [ ] Sin conversión
8. (Configurando el emulador para usar Git Bash) y ***Siguiente***
	- [x] Usar MinTTY
	- [ ] Usar la consola de Windows
9. (Configurando opciones extras) y ***Siguiente***
	- [x] Activar sistema de cacheo de archivos
	- [ ] Activar Git Credential Manager
	- [ ] Activar enlaces simbólicos
10. (Configurando opciones experimentales) y ***Siguiente***
	- [ ] Activar opciones experimentales 


### Git Credential Manager for Windows v1.14.0

> https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/tag/v1.14.0

```sh
git --version
git config --global user.email "guardeividu@example.com"
git config --global user.name "Guardeivid"
git config --global credential.helper wincred

git status
git pull https://github.com/guardeivid/aiuta.git
git add *
git commit -m 'Gulp'
git push --set-upstream https://github.com/guardeivid/aiuta.git master
```

### Almacenar usuario y contraseña

#### Cache
Se almacena por un periodo de tiempo, por defecto es 900 segundos o 15 minutos
git config --global credential.helper cache --timeout <seconds>
> git config --global credential.helper cache

#### Store
Almacena en un archivo de texto las credenciales
--file <path> defecto ~/.git-credentials).
> git config --global credential.helper 'store --file ~/.my-credentials'



## GitHub Destokp en Windows

> Cliente GUI [GitHub Desktop](http://windows.github.com)


### Instalación GitHub Desktop

1. (Ingresar en GitHub.com) **Nombre de usuario o email** y **Contraseña** luego ***Ingresar***
2. (Configurar Git) **Nombre** y **Mail** luego ***Continuar***
3. (Hacer GitHub Desktop mejor) - [ ] Enviar anónimamente datos de uso, click en ***Finalizar***

### Uso de GitHub Desktop

* Crear nuevo proyecto y publicarlo en GitHub **Create new repository**
* Agregar un proyecto existente en tu computadora y publicarlo **Add a local repository**
* Clonar un proyecto existente desde GitHub a tu computadora **Clone a repository**
  
  * Propio repositorio
  * Desde una URL (<<username>>/<<repository>>)
  
  - Seleccionar la carpeta de destino
  
### Flujo de trabajo

* Click en **Fetch origin** para ver si hay diferencias entre el repositorio remoto y el local (*`~ git fetch [url]`*)
* Click en **Pull origin** para copiar cambios desde el repositorio remoto al local (*`~ git pull [url]`*)
* Modificar o crear archivos en el proyecto (detecta cambios en local) (*`~ git add *`*)
* Escribir en **Summary** y click en **Commit** (*`~ git commit -m mensaje`*)
* Click en **Push Origin** para enviar las modificaciones al repositorio remoto (*`~ git push [origin] [branch]`*)

## Git Extensions GUI

<https://gitextensions.github.io/>

### Instalación

1. Descargar [Git Extensions](https://github.com/gitextensions/gitextensions/releases/)
2. Requiere **Windows 7SP1+**, **.NET Framework 4.6.1+** y éste requiere **D3DCompiler_47.dll**
   1. **D3DCompiler_47.dll** [W7x86](http://go.microsoft.com/fwlink/?LinkId=848159) o [W7x64](http://go.microsoft.com/fwlink/?LinkId=848158) 
   2. **NET 4.7** [W7x86](http://www.microsoft.com/downloads/details.aspx?familyid=219c1fed-8214-431d-85a5-49e675436501) o [W7x64](http://www.microsoft.com/downloads/details.aspx?familyid=e934e251-8ada-442b-b3ad-34d051f18c37) 

<!--
## GitKraken
1. Descargar en <https://www.gitkraken.com/download/windows>
2. Instalación
	1. Licencia -> Ir a Atlassian
	2. Registrar Cuenta en <https://id.atlassian.com/signup?application=mac&continue=https://my.atlassian.com>:
-->