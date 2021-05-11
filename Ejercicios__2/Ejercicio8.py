#Leer un número y calcular la suma de los números naturales hasta ese número.
#Modificar el algoritmo para que se pueda procesar muchos números. Dar por terminada la
#entrada cuando el número sea 0

numero = int(input('Ingrese un número: '))
numerosuma = 0

while True :
    if numerosuma >=numero or numero != 0:
        break
    else:
        numero1 = int(input('Ingrese un número: '))
        numero2 = int(input('Ingrese un número: '))
        numerosuma = numerosuma+ numero1+numero2     
        print(f'La sumatoria de {numero1} y {numero2} es igual a {numerosuma}')
