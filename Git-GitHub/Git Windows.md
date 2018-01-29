## Configuracion básica entorno desarrollo en Windows

### Instalar Visual Code

> https://code.visualstudio.com/Download

### Instalar Git

> https://git-scm.com/download/win

1. (Licencia) *Siguiente*
2. (Seleccionar componentes) *Siguiente*
3. (Elegir el editor por defecto) [X] nano, [] vim, [] notepad++ *Siguiente*
4. (Ajustar variable de entorno PATH) [X] Git desde Git Bash, [] Git desde Consola de Windows , []Usar Git y opciones UNIX desde la Consola de Windows  *Siguiente*
5. (Elegir el ejecutable SSH) [X] Usar OpenSSH, [] Usar (Tortoise) Plink  *Siguiente*
6. (Elegir transporte bakend HTTPS) [X] Usar la librería OpenSSH, [] Usar la librería Windows Secure Channel *Siguiente*
7. (Configurando el fin de línea de archivos de texto) [X] Estilo Windows (LF->CRLF->LF) [] Estilo Unix (CRLF->LF), [] Sin conversión *Siguiente*
8. (Configurando el emulador para usar Git Bash) [X] Usar MinTTY, [] Usar la consola de Windows *Siguiente*
9. (Configurando opciones extras) [X] Activar sistema de cacheo de archivos, [] Activar Git Credential Manager, [] Activar enlaces simbólicos *Siguiente*
10. (Configurando opciones experimentales) [] Activar opciones experimentales *Siguiente*

### Instalar Node.js y npm

> https://nodejs.org/es/download/


### Git Credential Manager for Windows v1.14.0

> https://github.com/Microsoft/Git-Credential-Manager-for-Windows/releases/tag/v1.14.0


git --version
git config --global user.email "guardeividu@example.com"
git config --global user.name "Guardeivid"
git config --global credential.helper wincred

git status
git pull https://github.com/guardeivid/aiuta.git
git add *
git commit -m 'Gulp'
git push --set-upstream https://github.com/guardeivid/aiuta.git master

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

Descargar Git de la página [https://git-scm.com/downloads](https://git-scm.com/downloads), que incluye línea de comandos

También se puede descargar desde el cliente GUI [GitHub Desktop](http://windows.github.com)


### Instalación GitHub Desktop

1- (Ingresar en GitHub.com) **Nombre de usuario o email** **Contraseña** *Ingresar*
2- (Configurar Git) **Nombre**  **Mail** *Continuar*
3- (Hacer GitHub Desktop mejor) [] Enviar anónimamente datos de uso *Finalizar*

### Uso de GitHub Desktop

* Crear nuevo proyecto y publicarlo en GitHub **Create new repository**
* Agregar un proyecto existente en tu computadora y publicarlo **Add a local repository**
* Clonar un proyecto existente desde GitHub a tu computadora **Clone a repository**
  
  * Propio repositorio
  * Desde una URL (<<username>>/<<repository>>)
  
  - Seleccionar la carpeta de destino
  
### Flujo de trabajo

* Click en **Fetch origin** para copiar cambios desde el repositorio remoto al local
* Modificar o crear archivos en el proyecto (detecta cambios en local)
* Escribir en **Summary** y click en **Commit**
* Click en 