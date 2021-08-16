def costo_camion(nombre_archivo):
    import csv
    f = open(nombre_archivo)
    costo = 0
    rows = csv.reader(f)
    headers = next(rows)
    for line in f:
            row= line.split(',')
            precio = int(row[1])
            cajones = float(row[2])
            costo = costo + (precio * cajones)
            
    return costo
costo = costo_camion('./Data/camion.csv')
print('Costo total:', costo)


