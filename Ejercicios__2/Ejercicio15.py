#8. Calcular el importe que debe pagar un auto en un estacionamientoteniendo en cuenta como datos las horas y minutos de uso. El valor de la hora es de $45 y si los minutos exceden de 15 se incrementa una hora al importe. El mínimo a cobrar es de una hora.

hora = int(input('Ingrese hora: '))
minutos = int(input('Ingrese minutos: '))
hora = 45
valorFinalImporte = hora * hora +hora
ValorFinalNoImporte = hora*hora
if minutos > 15:
    print('Usted se ha extendido mas de 15 minutos, es por que ello que tiene un importe de una hora adicional',valorFinalImporte)

else:
    print('Su importe final es: ',ValorFinalNoImporte)
