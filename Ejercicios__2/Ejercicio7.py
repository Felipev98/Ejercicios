#7) Ingresar las temperaturas registradas a distintas horas de un día en grados hasta que
#ésta sea 100. Mostrar la temperatura máxima y la temperatura mínima.

temperaturaTotal = 0
temperatura = []

while temperaturaTotal < 100:
    temperaturadia = float(input('Ingresa la temperatura del día: '))
    temperaturaTotal = temperaturaTotal + temperaturadia
    mostrartemperatura = temperatura.append(temperaturadia)

print('La temperatura máxima es', max(temperatura))
print('La temperatura minima es: ',min(temperatura))