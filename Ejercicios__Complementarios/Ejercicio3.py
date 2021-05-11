#Ingresar el precio unitario de un producto  y la cantidad comprada y que devuelva el precio total

precio = float(input('Ingrese el precio de su producto'))
cantidad = float(input('Ingrese la cantidad su producto'))
precioTotal = precio * cantidad
print(f'El precio total de su productos es de: {precioTotal} Bsf')