#Haz una tabla de multiplicar utilizando el ciclo for

tablaMultiplicar = int(input('Escriba el número de la tabla: '))
for i in range(1,11):
    tablas = tablaMultiplicar * i
    print('El resultado es: ', tablas)