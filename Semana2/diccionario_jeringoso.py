def geringoso(clave):
        palabra_agregada = ""
        for letra in clave:
            if letra=="a":
                letra="apa"
            elif letra == 'e':
                letra ='epe'
            elif letra == 'i':    
                letra = 'ipi'
            elif letra == 'o':
                letra ='opo'
            elif letra == 'u':
                letra = 'upu'
            palabra_agregada += letra
        return palabra_agregada
lista = ['manzana','banana','mandarina']
cantidad = len(lista)
diccionario= {}
for i in range(cantidad):
    diccionario[lista[i]] = geringoso(lista[i])
print(diccionario)


