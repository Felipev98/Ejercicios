#Ingresar 3 precios, y calcular el IVA de esos productos. (21%)
i = 0
iva = 0.21
while i != 3:
    precio = float(input('Ingrese el precio de su producto: '))
    precioIva = precio * iva
    precioivaTotal =precioIva+precio
    i+=1
    print(f'El precio de su producto es {precio} con el IVA incluido es igual a: {precioivaTotal} Bsf')

