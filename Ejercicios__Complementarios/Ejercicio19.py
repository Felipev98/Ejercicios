# Escribir un programa que pregunte al usuario su edad
# y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

añosCumplidos = int(input('Escriba su edad: '))

for i in range(1, añosCumplidos + 1):
    print('Su edad actual es: ', i)
