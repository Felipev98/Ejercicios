#Ingresar una letra y decir si es vocal o no

letra = input('Ingrese una vocal: ').lower()
vocal = ['a','e','i','o','u']

if letra in vocal:
    print(f'{letra} si es una vocal')