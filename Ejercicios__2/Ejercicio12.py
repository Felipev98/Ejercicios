#Calcular el importe  que debe pagar una persona cuando compra una heladera de pesos X y por pagar en efectivo le haen el 10% de descuento
#¿Cuánto abona?
precioheladera = float(input('¿Cuál es el costo de su heladera? '))
cantidadheladera = int(input('¿Cuántas heladera compró? '))
pagarEfectivo = input('¿Va a pagar en efectivo? ').lower()
importe = precioheladera * cantidadheladera

if pagarEfectivo == 'Si':
    print('Usted abonó una cantidad de: $', importe * 0.1)

else:
    print('Usted abonó una cantidad de: $',importe)