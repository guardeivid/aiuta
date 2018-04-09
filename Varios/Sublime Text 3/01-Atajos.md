### Sublimt Text 3

#### Atajos

- Abrir archivo **_Ctrl + O_**
- Nuevo archivo **_Ctrl + N_**
- Cerrar archivo **_Ctrl + W_**
- Guardar archivo **_Ctrl + S_**
- Guardar archivo como **_Ctrl + Shift + S_**

Característivas
View-> Show/Hide Minimap

Mostrar Consola **_Ctrl +\`_**

Layouts **Alt + Shift + [1|2|3|4]w_**

- Selecciona la linea de arriba **_Ctrl + Alt + Up_** 
- Selecciona la linea de abajo **_Ctrl + Alt + Down_**
- Selecciona todo **_Ctrl + A_**
- Seleccionar palabra(s) que coinciden con una seleccion previa **_Ctrl + D_**
- Seleccionar todas las palabras que coinciden con una seleccion previa **_Ctrl + G_**
- Seleccionar línea(s) **_Ctrl + L_**
- Seleccionar todo el contenido dentro del documento **_Ctrl + A_**
- Seleccione todo dentro de las llaves ({ } cuando se trabaja con CSS o JavaScript) **_Ctrl + Shift + M_**

- Selección de múltiples cursores **_Ctrl + Shift + L_**
ej Copiar, luego seleccionar multiples cursores y pegar

- Múlpiples cursores **_Ctrl + click_**
- Línea dentada (en 1 linea) **_Ctrl + J_** 
- Duplica la línea **_Ctrl + Shift + D_**
- Cerrar una etiqueta **_Alt +_**
- Muestra todas las abreviaturas y listas de etiqueta por orden alfabético **_Ctrl + espacio_**

- Busca etiquetas en el código **_Ctrl + F_**
- Reemplaza una etiqueta **_Ctrl + H_**
- Muestra la consola **_Ctrl +_**

- Mover la linea donde se encuentra el cursor hacia arriba **_Ctrl + Shift + Up_**
- Mover la linea donde se encuentra el cursor hacia abajo **_Ctrl + Shift + Down_**


- Tiene herramientas tipo vim, para habilitarlas
Preferences -> Setting - Default
Comentar #ignored_packages=["vintage"]


##### Ir Goto
- Muestra los archivos abiertos **_Ctrl + p_**
- Muestra las funciones en el archivo **_Ctrl + r_**
- Ir a una linea en el archivo **_Ctrl + g_**

- Paleta de comandos
Tools->Command Palette, **_Ctrl + Shift + p_**

Desde aquí se pueden instalar paquetes, primero instalar package control y despues con la herramienta con install para cada paquete en particular
1-Package Control
2-Package Control Install Package

Abre una lista con los paquetes disponibles para instalar

- Para ver paquetes instalados
Package Control List Package, y abre la carpeta donde está instalado

#### Snippets
1-Posicionar el cursor en el código
2-Tools->Snippets... muestra una lista de los snippets disponibles instalados para el tipo de archivo, al seleccionarlo, se desplega el código asociado a ese snippet

Crear Snippets
- Permite incluir contenido desde una abreviatura y **TAB**
Tools -> Developer -> New Snippets...
```xml
<snippet>
	<content><![CDATA[
Hello, ${1:this} is a ${2:snippet}.
]]></content>
	<!-- Optional: Set a tabTrigger to define how to trigger the snippet -->
	<!-- <tabTrigger>html</tabTrigger> -->
	<!-- Optional: Set a scope to limit where the snippet will trigger ej tiene alcance solo en archivos html-->
	<!-- <scope>source.html</scope> -->
</snippet>
```
- Se guardan en la carpeta **~/AppData/Roaming/Sublime Text 3/Packages/User** con la extension **.sublime-snippet**
- Para usarlo desde Tools->Snippets... o Tools->Command Palette y buscar y Enter

- Se puede usar por TabTrigger
ej html + TAB
```html
<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>

</body>
</html>
```

El **${1:this}** indica donde se va a posicionar el cursor al ir pulsando la tecla TAB, permitiendo sobreescribir

Se puede usar cursores múltiples especificando **${1:this}** varias veces


#### Macros
- Guardan procesos repetitivos
Tools -> Record Macro, **_Ctrl + Q_**
- Realizar una acción
- Tools -> Stop Macro
- Tools -> Save Macro, yguardar con la extension **.sublime-macro**


#### Atajos de teclado personalizados
**Preferences -> Key Bindings - User**

- Identacion
```json
{ "keys": ["ctrl+t"], "command": "run_macro_file", "args": {"file": "Packages/User/convert_tabs_to_spaces.sublime-macro"} },
{ "keys": ["ctrl+shift+f"], "command": "reindent" , "args": {"single_line": false}}
```

- Atajo A SublimeREPL-> Phyton-> Phyton - RUN current file
```json
{ "keys": ["ctrl+alt+b"], "command": "run_existing_window_command", "args":{"id": "repl_python_run","file": "config/Python/Main.sublime-menu"}}
```

#### Configuración general

- Encoding
> **Preferences > Settings - Users**
```json
	"show_encoding" : true,
```



<https://manuais.iessanclemente.net/index.php/Tutorial_sobre_editor_Sublime_Text_3>
#### Plugins recomendados <https://packagecontrol.io/>
- **MapfileSyntax** <https://packagecontrol.io/packages/MapfileSyntax>
Run Package Control: Install Package in the Command Palette (Super+Shift+P) -> Install MapfileSyntax
- **AutoFilename(https://packagecontrol.io/packages/AutoFileName)**, vincula archivos mediante sugerencias, para href, src, include , etc.
- **MatlabFilenameAutoComplete(https://packagecontrol.io/packages/MatlabFilenameAutoComplete)** en ST3
- **DocBlockr(https://packagecontrol.io/packages/DocBlockr)** 
Permite insertar comentario para la documentación, para usar escriba las primeras lineas  /** presione la tecla tab.
- **PHPManualer** 
Este plugin permite mostrar al pulsar las teclas ctrl + alt + d – ctrl + alt + s la documentación de las funciones nativas de PHP
- **ColorPicker** 
Permite seleccionar en la paleta de color un color especifico, muy bueno al escribir código CSS. Para usar presione **ctrl+alt+c**.
- **jQuery** 
Plugin para ayudar la sugerencia de JQuery, al escribir código puede mostrar casi la totalidad de los métodos que existen en JQuery en forma de fragmentos.
- **Terminal(https://packagecontrol.io/packages/Terminal)** permite abrir una ventana de terminal en la misma carpeta en donde se encuentra el fichero con el que estás trabajando.
con **ctrl+shift+t**, y a la carpeta del proyecto con **ctrl+alt+shift+t**.
- **Apacheconf.tmLanguage(https://packagecontrol.io/packages/ApacheConf.tmLanguage)** 
Resaltado de sintaxis para los archivos de configuración de Apache. (.htaccess)
- **Color Highlighter(https://packagecontrol.io/packages/Color%20Highlighter)** colorea las variables de color. Es compatible con diferentes tipos de valores de color como hexadecimal, rgb, RGBA, HSL, HSLA.
- **Console Wrap(https://packagecontrol.io/packages/Console%20Wrap)** Añade tus variables a la segunda línea en los logs de la consola, soporta Javascript, Python, Php. 
Seleccionar una variable (o poner el cursor en ella) y presionar **ctrl+shift+q**. The log line will appear on the next line. Press "ctrl+shift+q" again to change wrapping (info,warn etc.)

You can Also remove, comment or remove commented log statements from your selsection or from all document you can find that functionality in context menu (right click) or Command Palette (command+shift+p on OS X, control+shift+p on Linux/Windows).
- **Sublime Linter 3** Es un complemento que admite programas “lint” (conocidos como “linters”). SublimeLinter resalta las líneas de código que el linter considera que contienen errores (potenciales). También admite resaltar anotaciones especiales (por ejemplo: TODO) para que puedan ubicarse rápidamente. Admite casi todos los idiomas populares.
- **SublimeREPL** 
Ejecute un intérprete dentro de ST3 (Clojure, CoffeeScript, F #, Groovy, Haskell, Lua, MozRepl, NodeJS, Python, R, Ruby, Scala, shell o configure uno usted mismo).
```json

```

- **JSLint** 
JSLint es una herramienta de calidad de código Javascript creada por Douglas Crockford, desarrollador de JavaScript hardcore. Esta herramienta lo ayuda a saber qué partes de su código necesita cambiar para tener un mejor código. Hasta ahora, solo podías hacerlo en línea, pero con este complemento puedes hacerlo directamente en ST2. Si es serio acerca de Javascript necesita esto.
- **SideBarEnhancements(https://packagecontrol.io/packages/SideBarEnhancements)** Amplía las opciones de gestión de archivos de la barra lateral.
- **SublimeCodeIntel**
- **PHP CodeSniffer**(http://www.conasa.es/blog/php-codesniffer-sublime-text/)