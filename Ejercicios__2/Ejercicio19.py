#Ingresar las edades de 2 persona. Si una de ellas es mayor y la otra menor de edad, calcular y mostrar su promedio. En caso contrario
#mostrar las 2 edades
edad1 = int(input('Ingrese su edad: '))
edad2 = int(input('Ingrese su edad: '))
promedio = (edad1+edad2)/2

if edad1 >=18 and edad2 <=18:
    print('El promedio de edad de las 2 personas es: ', promedio)

else:
    print(edad1,edad2)