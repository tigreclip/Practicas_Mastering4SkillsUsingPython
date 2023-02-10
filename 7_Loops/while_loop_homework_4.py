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
    if txt == 'no' or txt == 'No' or txt == 'nO' or txt == 'NO' or '\'-->QUITAR COMILLAS!!
            txt == 'on' or txt == 'oN' or txt == 'On' or txt == 'ON':  #'\' permite partir el codigo y seguir funcionando
        print('Coincidencia: ', txt)

    cnt += 1
"""

###### HOMEWORK 2 Número inverso ######

"""
Leer un entero N, después  encontrar el número inverso R
    imprimir R R*3

N = int(input('Ingresa un número para saber su inverso: '))
numero = 0

while N > 0:
    ultimo_digito = N % 10  # halla el último digito
    N //= 10  # quita el último dígito

    numero = numero * 10 + ultimo_digito

print(numero, numero * 3)
# En el futuro aprenderemos cómo hacer lo de arriba sin las matemáticas
N = 1234
str_num = str(N)  # convierte a string
str_num = str_num[::-1]  # invierte el string
N = int(str_num)
print(N, N*3)
"""

# input   output
#  123      321 963

##### HOMEWORK 3 Tabla de multiplicar #####

"""
Leer un entero N y M , depues imprimir NxM lineas para su tabla de multiplicación.

"""
# crea dos variables, usando MAP para convertir en INT las entrada numericas
num1, num2 = map(int,input("Ingresa el número dos numeros separados por espacio: ").split())

cnt_num1 = 1 # el primer operador


while cnt_num1 <= num1: # primer loop
    cnt_num2 = 1 # el segundo  operador vale 1

    while cnt_num2 <= num2: # segundo loop
        print(f'{cnt_num1} x {cnt_num2} = {cnt_num1}*{cnt_num2}') # enunciado y operacion matemática
        cnt_num2 += 1 # aumenta 1 al segundo operador
    
    cnt_num1 += 1 # auemnta 1 al primer operador
    
