### Comandos útiles

#### Extraer carpeta de una ruta (*`dirname`*), extraer carpeta y nombre de una ruta (*`split`*)
```python
import os

path="C:/path/to/file/filename.ext"

os.path.dirname(os.path.abspath(path))
'C:\\path\\to\\file'

os.path.split(os.path.abspath(path))
('C:\\path\\to\\file', 'filename.ext')
```