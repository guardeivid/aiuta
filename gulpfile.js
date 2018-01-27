/*
* Dependencias
*/
var gulp = require('gulp'),
  concat = require('gulp-concat'),
  uglify = require('gulp-uglify'),
  debug = require('gulp-debug');

/*
* Configuración de la tarea 'demo'
*/
gulp.task('demo', function () {
  return gulp.src('Node.js/ej_gulp/src/js/*.js')
    //.pipe(debug( {verbose: true} )
    .pipe(concat('todo.js'))
    .pipe(uglify())
    .pipe(gulp.dest('Node.js/ej_gulp/build/'))
});

//Llamar gulp demo

gulp.task('default', function(){
    gulp.watch('Node.js/ej_gulp/src/js/*.js', ['demo'])
});

//llamar gulp (porque es la tarea por defecto)
//como tiene la funcion watch sera ejecutada cada vez que se modifique alguno de los archivos
//detener con  Ctrl+X