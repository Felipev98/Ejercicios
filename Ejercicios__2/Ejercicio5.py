#5) Ingresar 10 números mayores a 3 y menores a 8. Mostrar el valor ingresado en
#número y letras.

i = 0
while i != 10:
    numeros = int(input('Ingrese un número: '))
    if numeros > 3 and numeros < 8:
        print(numeros)
    else:
        print('Número invalido, número tiene que ser mayor a 3 y menor a 8')    
    i+=1    