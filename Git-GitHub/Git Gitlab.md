### Git en GitLab

#### Clave SSH

```sh
# Crear clave
ssh-keygen -t rsa -b 4096 -C "gitlab"
# Enter file in which to save the key (~/.ssh/id_rsa): 
~/.ssh/id_rsa_gitlab
```

Crear archivo si no existe **~/.ssh/config** y escribir
```config
Host glab 
	HostName                    gitlab.com
	User                        git
	PreferredAuthentications    publickey
	IdentityFile                ~/.ssh/id_rsa_gitlab
```

Configurar en GitLab
- Ir a <https://gitlab.com/profile/keys>
- En **Key** pegar el contenido de **`~/.ssh/id_rsa_gitlab.pub`**, agregar un título y click en **Add Key**

Chequear conexión
```sh
ssh -T git@gitlab.com 
```

#### Agregar Remoto individual a GIT

```sh
# Agregar remoto
git remote add gitlab git@gitlab.com:guardeivid/aiuta.git

# Ver remotos configurados
git remote -v

# Eliminar remoto
git remove gitlab

# Comandos útiles
git status
git add .
git commit
git push gitlab master
git pull gitlab master
```

#### Agregar múltiples Remotos a `origin`

```sh
# Agregar remoto sólo para poder hacer push
git remote set-url --add --push origin git@gitlab.com:guardeivid/aiuta.git

# Hacer push a todos los origin/master
git push
```

