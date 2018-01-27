## Gulp.js
Automatizar tareas de desarrollo 

Reuiere [Node.js](http://nodejs.org/),
 Ver [Guía](https://github.com/guardeivid/aiuta/edit/master/Node.js/Node.js.md)

### Instalar Gulp de manera global
```
npm install -g gulp
```
Ver versión
```
gulp -v
```

Iniciar proyecto node.js dentro de la carpeta `aiuta`
```
cd aiuta
npm init
```

Configurar opciones del proyecto que se van a encontrar en el archivo que se va a crear **`package.json`**


Instalar dependencias de desarrollo al proyecto con **`--save-dev`** y así se agregan al archivo package.json.

Primero será gulp
```
npm install --save-dev gulp
```

Luego otras que necesitemos

```
npm install --save-dev gulp-concat
npm install --save-dev gulp-uglify
```


Links
 - [GULP.JS EN ESPAÑOL – TUTORIAL BÁSICO Y PRIMEROS PASOS](https://frontendlabs.io/1669--gulp-js-en-espanol-tutorial-basico-primeros-pasos-y-ejemplos)
