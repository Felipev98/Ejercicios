#2) Ingresar números hasta que el último sea cero. Calcular la cantidad de positivos.

positivos = 0
numero =1
while True:
    if numero != 0:
        numero = int(input('Ingresa un número distinto a cero: '))
        if numero > 0: 
            positivos = positivos + 1 
    else:
        break    

print(f'Escribiste un total de {positivos} positivos')