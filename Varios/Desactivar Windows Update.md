### Windows Update

Para desactivar rápidamente

- Guardar en un archivo con extensión **.bat** las siguientes instrucciones, y ejecutarlo como **Administrador**

```sh
sc config wuauserv start= disabled
%windir%\system32\net.exe stop wuauserv
```

