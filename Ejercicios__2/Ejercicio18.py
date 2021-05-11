#Hallar la longitud de una hipotenusa de un triángulo dada la medida de sus catetos
cateto1 = 20
cateto2 = 40
catetosTotal = (cateto1**2 + cateto2**2)
teoremaPitagoras = round(catetosTotal**(1/2),2)
print(teoremaPitagoras)
