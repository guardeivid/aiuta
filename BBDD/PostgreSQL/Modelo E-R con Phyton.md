## Crear Modelo Entidad-Relación (PostgreSQL) con Python


### Instalación en Ubuntu

#### Instalar `pip` (si no está instalado)
```sh
sudo apt-get update
sudo apt-get upgrade

sudo apt-get install python-pip
```

#### Instalar `eralchemy`
> Si está bajo un proxy se debe utilizar **`--proxy=http://[user:passwd@]server:port`**

```sh
sudo apt-get install graphviz-dev python-pygraphviz python-psycopg2
sudo pip --proxy=http://196.1.1.1:3128 install eralchemy

# Para tablas que tienen campos geométricos (PostGis)
sudo pip --proxy=http://196.1.1.1:3128 install geoalchemy2
```

#### Crear script

```sh
sudo nano ~/er.py
```

Agregar el contenido
```phyton
__author__ = 'anthony'
# -*- coding: 850 -*-
from eralchemy import render_er
import getpass
import psycopg2
import geoalchemy2
 
salida = False
 
while not salida :
 print 'Entre las credenciales del servidor--->'
 servidor = raw_input("Entre servidor : ")
 puerto = raw_input("Entre el puerto : ")
 basedatos = raw_input("Entre el la base de datos: ")
 usuario = raw_input("Entre el usuario: ")
 contrasena = getpass.getpass('Password')
 try:
 
  cadena = 'postgresql+psycopg2://'+usuario+':'+contrasena+'@'+servidor+':'+puerto+'/'+basedatos
  render_er(cadena, 'salida.png')
  print 'El modelo se encuentra en el archivo salida.png'
  salida=True
 except Exception, e:
  print u'Verifique los parametros de conexión'
  print str(e)
```

> Parámetros a tener en cuenta en la función **render_er**

```phyton
render_er(input, output, mode='auto', include_tables=None, include_columns=None, exclude_tables=None, exclude_columns=None, schema=None)

    """
    Transform the metadata into a representation.
    :param input: Possible inputs are instances of:
        MetaData: SQLAlchemy Metadata
        DeclarativeMeta: SQLAlchemy declarative Base
    :param output: name of the file to output the
    :param mode: str in list:
        'er': writes to a file the markup to generate an ER style diagram.
        'graph': writes the image of the ER diagram.
        'dot': write to file the diagram in dot format.
        'auto': choose from the filename:
            '*.er': writes to a file the markup to generate an ER style diagram.
            '.dot': returns the graph in the dot syntax.
            else: return a graph to the format graph
    :param include_tables: lst of str, table names to include, None means include all
    :param include_columns: lst of str, column names to include, None means include all
    :param exclude_tables: lst of str, table names to exclude, None means exclude nothing
    :param exclude_columns: lst of str, field names to exclude, None means exclude nothing
    :param schema: name of the schema
    """
```



Links
- [ERAlchemy](https://github.com/Alexis-benoist/eralchemy)
- [GeoAlchemy2](https://geoalchemy-2.readthedocs.io/en/latest/)
- <https://anthonysotolongo.wordpress.com/2015/05/25/obtener-el-diagrama-relacional-desde-una-bases-de-datos-postgresqlingenieria-inversa/>


## Crear Modelo Entidad-Relación (PostgreSQL) con postgresql_autodoc

### Instalación
```sh
sudo apt-get install postgresql-autodoc dia GraphViz
```

```sh
postgresql_autodoc -d ada -f ~/er/ada -h localhost -u gis_user --password


sudo dot -T jpeg -o ~/er/ada.jpeg ~/er/ada.dot

sudo dot -T svg -o ~/er/ada.svg ~/er/ada.dot
```