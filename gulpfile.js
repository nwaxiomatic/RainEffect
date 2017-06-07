var gulp = require('gulp'),
  fs = require('fs'),
  source = require('vinyl-source-stream'),
  browserify = require('browserify'),
  uglify = require('gulp-uglify'),
  streamify = require('gulp-streamify'),
  babelify = require("babelify");
	gsap = require("gsap");
	glslify = require("glslify");

function compileJS(file){
  browserify('src/'+file+'.js',{debug:true})
    .bundle()
    .on("error", function (err) { 
      console.log("Error : " + err.message);
      console.log("File : " + file); 
    })
    .pipe(source(file+'.min.js'))
    .pipe(gulp.dest('demo/js'));
}
gulp.task('default',['js1','js2','js3'],function(){});
gulp.task('js1',function(){
  compileJS('index');
});
gulp.task('js2',function(){
  compileJS('index2');
});
gulp.task('js3',function(){
  compileJS('index3');
});
