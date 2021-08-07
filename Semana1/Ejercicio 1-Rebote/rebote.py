#Este es el primer conjunto de ejercicios en el que vas a tener que crear un archivo de Python y correrlo. A partir de aca, vamos a asumir que estás trabajando en el subdirectorio ejercicios_python/. Para ayudarte a organizar los archivos de diferentes clases y a ubicar el lugar correcto ya creamos algunos subdirectorios y un par de archivos en el directorio correpondiente a esta clase. Buscá en tu terminal el archivo ejercicios_python/Clase01/rebotes.py (cambiando de directorio como vimos recién). Lo vamos a usar en este ejercicio.

#Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que toca el piso salta 3/5 de la altura desde la que cayó. Escribí un programa rebotes.py que imprima una tabla mostrando las alturas que alcanza en cada uno de sus primeros diez rebotes.

i=0
saltos = 3/5
altura = 100
while i != 10:
    resultado = saltos * altura
    altura = resultado
    i+=1
    print(i, round(resultado,4))
