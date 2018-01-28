## Gulp.js
Automatizar tareas de desarrollo

Reuiere [Node.js](http://nodejs.org/),
 Ver [Guía](https://github.com/guardeivid/aiuta/blob/master/Node.js/Node.js.md)

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

### Bower
Obtiene los paquetes necesarios para el desarrollo de nuestra plantilla (Bootstrap, jQuery, etc.)
Para usar Bower necesitamos git y si estamos trabajando en Windows necesitamos instalar correctamente msysgit. Durante la instalación de msysgit tenemos que elegir la opción "Run Git from the Windows Command Prompt".

Bower nos instalará automáticamente los paquetes en la carpeta "bower-components"

```
npm install -g bower
```

Se creará un archivo de configuración **bower.json** y cada vez que instalemos un paquete usando `-save-dev` se agregará la dependencia en la configuración.
```
bower init
```

Se pueden hacer búsquedas de paquetes

```
bower search bootstrap
```
Y para instalar

```
bower install bootstrap --save-dev
bower install font-awesome --save-dev
```

Luego se instalan otras dependencias que necesitemos

#### GULP-CONCAT
Sirve para concatenar archivos. Concatena archivos usando el salto de línea (newLine) desde el sistema operativo.

```
npm install --save-dev gulp-concat
```

Ej

```js
var gulp = require('gulp'),
    concat = require('gulp-concat');

gulp.task('concatenar', function() {
    gulp.src(['./lib/1.js', './lib/2.js', './lib/3.js'])
        .pipe(concat('libs.js'))
        .pipe(gulp.dest('./dist/js/'))
});
```

Ejecutar
```
gulp concatenar
```

#### GULP-RENAME
Sirve para renombrar archivos, especialmente de extensiones

```
npm install --save-dev gulp-rename
```


```js
var gulp = require('gulp'),
    jade = require('gulp-jade'),
    rename = require('gulp-rename');

var path = {
    jade: ['jade/**/*.jade'],
    html: 'public/'
};

gulp.task('html', function() {
    return gulp.src(path.jade)
    .pipe(jade({
        pretty: true
    }))
    .pipe(rename({extname: '.phtml'}))
    .pipe(gulp.dest(path.html))
});
```
#### GULP-UGLIFY

```
npm install --save-dev gulp-uglify
```


```js
var gulp = require('gulp'),
    uglify = require('gulp-uglify');

gulp.task('min', function() {
    return gulp.src('source/scripts/*.js')
        .pipe(uglify())
        .pipe(gulp.dest('dist/scripts/'))
});
```

```
gulp min
```

#### GULP-IF
Plugin de Gulp.js que sirve para controlar condicionalmente el flujo de la ejecución de subtareas.

```
npm install --save-dev gulp-if
```

```js
var gulp = require('gulp'),
    uglify = require('gulp-uglify'),
    if = require('gulp-if');

var comprimir = false;

gulp.task('min', function() {
    return gulp.src('source/scripts/*.js')
               .pipe(if(comprimir, uglify()))
               .pipe(gulp.dest('dist/scripts/'))
});

```

#### GULP-DEBUG
sirve para ver información de archivos formato vinyl (el formato que tienen los archivos que pasan por el método gulp.src()).

```
npm install --save-dev gulp-debug
```

```js
var gulp = require('gulp'),
    uglify = require('gulp-uglify'),
    debug = require('gulp-debug');

gulp.task('min', function() {
    return gulp.src('source/scripts/*.js')
               .pipe(debug({verbose: true})
               .pipe(gulp.dest('dist/scripts/'))
});
```
#### GULP-MINIFY-CSS
Plugin de Gulp.js que sirve para minificar archivos css con clean-css.

```
npm install --save-dev gulp-minify-css
```


```js
var gulp = require('gulp'),
    minifyCSS = require('gulp-minify-css');

gulp.task('mincss', function() {
    gulp.src('./source/css/*.css')
        .pipe(minifyCSS())
        .pipe(gulp.dest('./dist/css/'))
});
```

#### GULP-IMAGEMIN
Plugin de Gulp.js que sirve para minificar imágenes PNG, JPEG, GIF y SVG con imagemin.

```
npm install --save-dev gulp-imagemin
```

```js
var gulp = require('gulp');
var imagemin = require('gulp-imagemin');

gulp.task('imagenes', function () {
    return gulp.src(['src/images/*.*'])
        .pipe(imagemin())
        .pipe(gulp.dest('dist/images/'));
});
```

#### Inject
Injecta rutas de archivos dentro de archivos específicos delimitados por ciertos Tags

```
npm install --save-dev gulp-inject
```

```html
<!DOCTYPE html>
<html>
<head>
  <title>My index</title>
  <!-- inject:css -->
  <!-- endinject -->
</head>
<body>

  <!-- inject:js -->
  <!-- endinject -->
</body>
</html>
```


```js
var gulp = require('gulp');
var inject = require("gulp-inject");

gulp.task('index', function () {
  var target = gulp.src('./index.html');
  var sources = gulp.src(['./js/*.js', './css/*.css'], {read: false});

  return target.pipe(inject(sources))
    .pipe(gulp.dest('./src'));
});
```

#### gulp-autoprefixer
Agrega los prefijos necesarios para distintos navegadores en los estilos css

```
npm install gulp-autoprefixer --save-dev
```

#### gulp-notify
Para mostrar errores

```
npm install gulp-notify --save-dev
```


```js
var notify = require('gulp-notify');

gulp.task('cssdev', function(){
return gulp.src('assets/less/simple.less')
.pipe(less())
.on('error',function (err) {
console.log(err.toString());
this.emit('end');
})
.pipe(autoprefixer('last 20 version'))
.pipe(notify('cssdev done'))
.pipe(gulp.dest(targetCss))
.pipe(reload({stream:true}));
});
```

#### browser-sync
Nos actualiza el navegador automáticamente cada vez que hacemos un cambio en los archivos de la plantilla

```
npm install browser-sync --save-dev
```

Links
 - [GULP.JS EN ESPAÑOL – TUTORIAL BÁSICO Y PRIMEROS PASOS](https://frontendlabs.io/1669--gulp-js-en-espanol-tutorial-basico-primeros-pasos-y-ejemplos)
 -[https://github.com/contra/gulp-concat](https://github.com/contra/gulp-concat)
 - [https://github.com/hparra/gulp-rename](https://github.com/hparra/gulp-rename)
 - [https://github.com/sindresorhus/gulp-imagemin](https://github.com/sindresorhus/gulp-imagemin)
 - [https://github.com/klei/gulp-inject](https://github.com/klei/gulp-inject)
 - [https://magazine.joomla.org/es/ediciones-anteriores/item/2800-como-utilizar-gulp-en-el-desarrollo-de-plantillas](https://magazine.joomla.org/es/ediciones-anteriores/item/2800-como-utilizar-gulp-en-el-desarrollo-de-plantillas)
