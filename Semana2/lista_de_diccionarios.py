import csv
def leer_camion(nombre_archivo):
    camion =[]
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            diccionario ={}
            diccionario['nombre'] = row[0]
            diccionario['cajones'] = int(row[1])
            diccionario['precio'] = float(row[2])
            camion.append(diccionario)
            print(diccionario)
    return (diccionario)            
print(leer_camion('./Data/camion.csv'))
