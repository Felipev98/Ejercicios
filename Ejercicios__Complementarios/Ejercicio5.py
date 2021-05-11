#Transformar una cantidad de pesos ingresada a dólares. Suponiendo que cuesta 20$
CantidadPesos = float(input('Ingrese la cantidad de pesos: '))
equivalenciaPesos = 40
dolar = 20
conversion = (equivalenciaPesos*CantidadPesos)/dolar
print(f'Su conversión da un resultado de:{conversion}$')

