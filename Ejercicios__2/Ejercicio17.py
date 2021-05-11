# Ingresar dos números, calcular y mostrar el cociente del primero por el segundo, siempre que el divisor no sea cero. En este último caso mostrar la leyenda “no se puede realizar el cociente”. 
numero1 = int(input('Ingrese un número: '))
numero2 = int(input('Ingrese un número: '))
if(numero2 == 0):
    print('No se puede realizar el cociente')
else:
    print('El resultado es: ', round(numero1/numero2,2))
