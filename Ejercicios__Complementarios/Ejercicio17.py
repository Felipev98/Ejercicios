#Ingresar una nota del 1 al 10. Se mostrará por pantalla alguno de los siguientes valores:
# 1-4 Reprobado
# 5: Regular
#6-7 Bien
# 8-9: Muy bien
#10 Exelente

nota = int(input('Ingrese el valor de su nota(1 al 10): '))

if nota > 10 or nota < 0:
    print('Número invalido')

elif nota <= 4:
        print('Reprobado')
elif nota == 5:
        print('Regular')
elif nota <= 7:
        print('Bien')
elif nota <= 9:
        print('Muy bien')
else:
    print('Excelente')    