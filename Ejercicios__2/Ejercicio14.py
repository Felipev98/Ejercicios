#9. Se ingresa el código de tipo de llamada: 1. Local 2. Interurbana 3. Internacional y la duración en minutos de la misma. Si el minuto cuesta $0.25 para la llamada local, $0.40 para la llamada interurbana y $1.05 para la llamada internacional, diseñar un algoritmo que permita calcular el monto a pagar por dicha llamada.

codigo = int(input('Ingrese el código de su llamada: '))
minutos = int(input('Ingrese la cantidad de minutos de su llamada: '))

if codigo == 1:
    print('El costo total de su llamada es: ', minutos * 0.25)
    
elif codigo == 2:
    print('El costo total de su llamada es: ',minutos * 0.40)

else:
    print('El costo total de su llamada es: ',minutos *1.05 )
            