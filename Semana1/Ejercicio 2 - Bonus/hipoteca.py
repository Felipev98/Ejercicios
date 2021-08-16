
#Ya que estamos, corregí el código anterior de forma que el pago del último mes se ajuste a lo adeudado.
#Asegurate de guardar en el archivo hipoteca.py esta última versión en tu directorio ejercicios_python/Clase01/. Vamos a volver a trabajar con él.
saldo = 500000.0
tasa = 0.05
total_pagado = 0.0
mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
while saldo > 0:
    mes+=1
    pago_mensual = 2684.11
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        pago_mensual +=pago_extra
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    print(mes,round(total_pagado,2),round(saldo,2))
print('Total pagado: ',round(total_pagado,2))
print('Meses',mes)
