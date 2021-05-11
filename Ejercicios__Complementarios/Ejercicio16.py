#Ingresar 3 números y mostrar cuál es el mayor
numero1 = float(input('Ingresa un número: '))
numero2 = float(input('Ingresa un número: '))
numero3 = float(input('Ingresa un número: '))

if numero1 > numero2 and numero1 > numero3:
    print(f'El número mayor es {numero1}')

elif numero2 > numero1 and numero2 > numero3:
        print(f'El número mayor es {numero2}')
else:
    print(f'El número mayor es {numero3}')

