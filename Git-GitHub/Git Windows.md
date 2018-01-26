## Configuracion básica entorno desarrollo en Windows

### Instalar Visual Code

> https://code.visualstudio.com/Download

### Instalar Git

> https://git-scm.com/download/win

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