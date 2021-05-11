# 4) Leer el número de mes y mostrar cuantos días tiene ese mes (año actual)

mes = int(input('Escriba el número del mes: '))
dias = 0

while dias !=31:
    dias+=1
    if mes == 2:
        print('El número de días de su mes es de: ', dias-3)
    elif mes == 4 or mes == 5 or mes == 9 or mes == 11:
            print('El número de días de su mes es de: ', dias-1)
    else:
        print('El número de días de su mes es de: ',dias)        
                        


