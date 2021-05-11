#Ingresar un número.Si es positivo,  calcular su raiz cuadrada, si es negativo mostrar su cuadrado y si es cero mostrar : "Error. Ha ingresado un valor nulo"
numero = float(input('Ingrese un número'))
if numero == 0:
    print('Error ha ingresado un valor nulo')

elif numero > 0:
    print('La raiz cuadrada es: ', round(numero**(1/2),2))

else:
    print('El cuadrado del número es:  ', numero **2)

