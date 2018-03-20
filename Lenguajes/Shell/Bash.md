### Alias

Se puede usar **`.bash_profile`**, aunque es recomendable usarlo en **`.bashrc`**. 
Para eso hacer crear un archivo de perfil:

```sh
touch ~/.bash_profile
nano ~/.bash_profile

#.bash_profile
test -f ~/.profile && . ~/.profile
test -f ~/.bashrc && . ~/.bashrc
```

Y crear alias permanentes en:
```sh
touch ~/.bashrc
nano ~/.bashrc

#.bashrc
#alias ai='cd;cd C:/Users/<username>/Documents/aiuta;winpty python.exe a.py'
alias css='cd ~/apps/gis/build;python css.py'
```
