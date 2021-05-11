#Pasar una medida de kms a metros y también a centimetros
numero = float(input('Escriba el número que desea convertir: '))
conversionMetros = int(numero* (1000/1))
conversioncentimetros = int(numero* (1000/1)*(100/1))
print(f'La conversión de su número {numero} a metros es de {conversionMetros} m')
print(f'La conversión de su número {numero} a metros es de {conversioncentimetros} cm')

