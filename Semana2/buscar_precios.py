def buscar_precio(fruta):
    with open('./Data/camion.csv') as f:
        try:   
            headers = next(f)
            for line in f:
                row= line.split(',')
                if fruta == row[0]:
                    resultado = row[2]
                    print(f'El precio de un camion de',fruta, 'es de:',resultado)
                    break
        except NameError:
                print(fruta,'no figura en el listado')         

print(buscar_precio("Naranja"))            
