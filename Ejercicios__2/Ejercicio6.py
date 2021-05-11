#  Leer dos números, mostrar el siguiente Menú pudiendo seleccionar alguna opción y
# repetir esta operación hasta que seleccione 5.
#  Menú principal
# 1. Sumar
# 2. Restar
# 3. Multiplicar
# 4. Dividir
# 5. Salir
#  Seleccione una opción:
numero1 = int(input('Ingrese un número: '))
numero2 = int(input('Ingrese un número: '))
sumar = numero1 + numero2
resta = numero1 - numero2
multiplicar =  numero1 * numero2
dividir = numero1 / numero2
while True:
    menu = int(input('Ingrese un número del 1 al 5: '))
    if menu == 1:
        print('El resultado es: ',sumar)
    elif  menu == 2:
        print('El resultado es: ',resta)
    elif  menu == 3:
        print('el resultado es: ', multiplicar)
    elif menu == 4:
        print('El resultado es: ', dividir)
    elif menu == 5:
        break
    else:
        print('Número invalido(mayor a 5)')    