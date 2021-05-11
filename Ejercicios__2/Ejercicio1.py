#1 Calcular el promedio semanal de gastos en un mes, ingresando como datos: Semana númeroGasto semanal 
# El proceso termina cuando “semana número” es igual a 5.

semanaNumero = 1
gastoTotal = 0
while semanaNumero <= 4:
    gastoSemana = float(input('Ingrese el gasto: '))
    gastoTotal = gastoTotal + gastoSemana
    semanaNumero+=1
print('El promedio de gasto semanal fue: ', (gastoTotal/semanaNumero-1))