import csv
import sys

def costo_camion(nombre_archivo):
    costo = 0
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    for line in f:
            row= line.split(',')
            precio = int(row[1])
            cajones = float(row[2])
            costo = costo + (precio * cajones)
            
    return costo

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = './Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)