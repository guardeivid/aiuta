### Instalación


#### Windows
<www.python.org/download>

- Agregar el a PYTHON a PATH
- Instalar
- Desactivar el límite de PATH


##### Entorno de desarrollo
Sublime Text 3
<www.sublime.text.com/3>

- Instalacion
- Menú Tools -> Command Palette
  - Install Package Control -> Aceptar
- Menu Tools -> Command Palette
  - Install Package
- Instalar sublimeREPL
- Menú Tools -> SublimeREPL -> Python -> Python

- Activar Tools -> Build System -> Python

- Para ejecutar el código **Ctrl+b** o Tools -> Build

- Para poder ejecutar en modo consola, hay que usar 
  - **Tools -> SublimeREPL -> Python -> Python - RUN Current File**
  - O asignar una combinacion de teclas (shortcout)
    - Preferences > Key Bindings - User
    - Agregar al archivo entre llaves y guardar ,
    ```config
    	{ "keys": ["ctrl+shift+p"], "command": "run_existing_window_command", "args": {
    		"id": "repl_python_run",
    		"file": "config/Python/Main.sublime-menu"
    	}}
    ``` 
    - (Preferences > Key Bindings - Default, muestra los atajos por defecto)
  - Con **Ctrl+w** cierra la ventana
  - O en Preferences → Keyboard → Shortcuts → App Shortcuts
  	- Click the + to add a new shortcut.
    - Set the Application to Sublime Text.app, the Menu Title to the exact name of the menu option, and choose a Keyboard Shortcut.


#### Linux

sudo apt-get install python3 