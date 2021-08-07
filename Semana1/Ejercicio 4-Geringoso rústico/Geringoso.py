#Usá una iteración sobre el string cadena para agregar la sílaba 'pa', 'pe', 'pi', 'po', o 'pu' según corresponda luego de cada vocal.
# cadena = 'Geringoso'
# cadena_n = ''
palabra = input('Ingresar palabra: ').lower()
palabra_agregada = ""
for letra in palabra:
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
print(palabra_agregada)