### Procesos

Se identifican con el identificador **PID**

El padre de los procesos es el **PPID**

Si se termine un padre para que un proceso no quede huerfano el proceso **Init**, que se ejecuta cuando se arranca el sistema

#### Ver recursos utilizados por el sistema (Administrador de tareas)
```bash
top

# se actualiza cada 3-5 segundos
######################################################################
#PID   USUARIO  PR   NI   VIRT    RES   SCR  %CPU   %MEM  HORA   ORDEN

# para parar la vista CTRL+C
```

#### Terminar un proceso
```bash
kill <pid>
```

#### Manipular procesos
```bash
ps
```

#### Ver procesos en modo arbol
```bash
pstree
```

### Tareas en segundo plano (Programador de tareas) `CRON`
Permite especificar una tarea o script que se ejecute periodicamente en segundo plano.

```bash
# manual
man crontab

# Listar tareas
crontab -l

# Eliminar todas las tareas
crontab -r

# Crear o modificar tareas para el usuario actual
crontab -e
```

El archivo **crontab** contiene
- m 	minuto (0-59)
- h 	hora (0-23)
- dom 	dia del mes (1-31)
- mon	mes (1-12) o (jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec)
- dow	dia de la semana (0-6) (domingo=0=7) o (sun,mon,tue,wed,thu,fri,sat)
- command	comando a ejecutar

```config
# ejecutar todos los dias a cada minuto
#	m 	h 	dom 	mon 	down 	command
	*	*	*		*		*		date >> /home/usuario/cronCE.txt

# ejecutar en el minuto 49 de las 13 en los meses de enero y febrero, y dias de la semana los viernes
	49	13	*		1,2		5		date >> /home/usuario/cronCE.txt

# ejecutar en el minuto 49 de las 13 en los meses de enero y febrero, en los dias 3.
	49	13	3		1,2		*		date >> /home/usuario/cronCE.txt
```

