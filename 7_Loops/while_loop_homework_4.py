###### HOMEWORK 1 Encontrar "NO" ######
"""
Leer entero(int) N, depués leer N cadena de caracteres(string)
    - Imprimir solo los strings ( de dos caracteres)
    - Esos dos caracteres deben ser "N" y "O" (indistinto mayúsculas o minúsculas)
        p.e. imprimir "No", "ON", "no" pero ignorar p.e. "YEs", "Noooo"
        solo palabra con los dos caracteres N y O


# Leer entero(int) N,
total_variaciones = int(input('Indica las veces que quieres comparar las entradas de texto: '))

cnt = 0

while cnt < total_variaciones:
    txt = input('Ingresa caracteres a comparar: ')

    # Hay 8 maneras diferentes de combinar 2 letras
    if txt == 'no' or txt == 'No' or txt == 'nO' or txt == 'NO' or \
            txt == 'on' or txt == 'oN' or txt == 'On' or txt == 'ON':  # \ permite partir el codigo y seguir funcionando
        print('Coincidencia: ', txt)

    cnt += 1
"""

###### HOMEWORK 2 Número inverso ######

"""
Leer un entero N, después  encontrar el número inverso R
    imprimir R R*3

"""

num = int(input('Ingresa un número para saber su inverso: '))
contador = 0
while num > 0:
    # inverso = 1 \ num
    # print(inverso)
# input   output
#  123      321 963
