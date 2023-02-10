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


# crea dos variables, usando MAP para convertir en INT las entrada numericas
num1, num2 = map(int,input("Ingresa el número dos numeros separados por espacio: ").split())

cnt_num1 = 1 # el primer operador


while cnt_num1 <= num1: # primer loop
    cnt_num2 = 1 # el segundo  operador vale 1

    while cnt_num2 <= num2: # segundo loop
        print(f'{cnt_num1} x {cnt_num2} = {cnt_num1}*{cnt_num2}') # enunciado y operacion matemática
        cnt_num2 += 1 # aumenta 1 al segundo operador
    
    cnt_num1 += 1 # auemnta 1 al primer operador
"""
##### HOMEWORK 4 Suma Especial #####

"""
Leer entero T para el número de casos testeados
- para cada caso testeado, leer entero N
- depués leer N enteros a, b, c, ... en lineas separadas
- calcular la suma de:
    (a, b*b, c*c*c, d*d*d*d, e*e*e*e*e)
    K-números se repiten K-veces
    no usar operador de potencia(**)

EXPLICACION:
- 2 casos para testear
- 3  5 7 2 
        (5 + 7*7 + 2*2*2 = 62)
- 2  1 2 3 4 
        (1 + 2*2 + 3*3*3 + 4*4*4* = 268)

"""
# Necesitamos 3 loops anidados
# Loop sobre casos a testear
#   loop sobre numeros leidos
#       loop para repetir el numero K veces(multiplicacion)

T = int(input('número de casos a testear')) # número de casos testeados
# loop sobre casos a testear
while T > 0:
    N = int(input())
    cnt_N, suma = 1, 0 # crea dos variables

    # loop sobre numeros leidos
    while cnt_N <= N:
        valor = int(input())
        cnt_deep, resultado = cnt_N, 1

        #loop para calcular la suma: a, b*b, c*c*c, d*d*d*d, e*e*e*e*e....
        while cnt_deep > 0:
            resultado *= valor
            cnt_deep -= 1

        suma += resultado
        cnt_N += 1
    
    print(f'La suma es {suma}')
    T -= 1


