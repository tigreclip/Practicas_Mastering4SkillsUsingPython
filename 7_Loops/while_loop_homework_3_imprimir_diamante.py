###### IMPRIMIR DIAMANTE ######
"""
Leer un entero N. Imprimir diamante de 2N rows(filas) como abajo

         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
*******************
 *****************
  ***************
   *************
    ***********
     *********
      *******
       *****
        ***
         *

imprimir el triángulo superior primero:
Asumimos que N = 4, cuántos espacios imprimiremos
Row 1	Espacios 3	Estrellas 1
Row 2	Espacios 2	Estrellas 3
Row 3	Espacios 1	Estrellas 5
Row 4	Espacios 0	Estrellas 7

vamos a desarrollar fórmulas para el número de espacio y el número de estrellas
dado un row:
Los espacios son: N - rows   	(3, 2, 1, 0)
Los espacios son: 2*row -1	(1, 3, 5, 7)

Ahora iteramos por cada row(fila)
Imprimimos espacios
depués imprimimos las estrellas
"""

"""
n  = int(input('ingrese un número: '))

row = 1

while row <= n:
    #imprimr n - row espacios
    contador_stars = 1
    while contador_stars <= n - row:
        print(' ', end='')
        contador_stars += 1

    #imprimir 2*row -1 espacio
    contador_stars = 1
    while contador_stars <= 2 * row - 1:
        print('*', end='')
        contador_stars +=1
    
    print()
    row += 1 

row = n
while row > 0:
    # Imprimir N - row espacios
    contador_stars = 1
    while contador_stars <= n - row:
        print(' ', end='')
        contador_stars += 1
    
    # Imprimir 2*row - 1 espacios
    contador_stars = 1
    while contador_stars <= 2 * row-1:
        print('*', end='')
        contador_stars += 1
    
    print()
    row -= 1
"""

###### Múltiplos especiales 2 ######
"""
Leer un entero N: imprimir todos los numeros <= N que :
    - sea divisible entre 8
    - o sea divisible entre 4 y entre 3 


n = int(input('Ingresa un número: ')) #Leer un entero N: imprimir todos los numeros <= N
cnt = 0

while cnt <= n:
    #sea divisible entre 8 o que sea divisible entre 4 y 4
    if cnt % 8 == 0 or cnt % 3 == 0 and cnt % 4 == 0:
        print(cnt, end='')
    cnt += 1 # suma un bucle a contador

# test
# input: 96
# output: 0 8 12 16 24 32 36 40 48 56 60 64 72 80 84 88 96
"""

###### Múltiplos especiales 2 ######

"""
Leer un entero N(1<=30): Imprimir los primeros numeros N que:
    -sean múltiplos de 3 pero no múltiplos de 4


n = int(input('Ingresa un número: ')) # Leer un entero N(1<=30)

cnt = 0
numero_actual = 0

while cnt < n:
    if numero_actual % 3 == 0 and numero_actual % 4 != 0:  # Imprimir los primeros numeros N  múltiplos de 3
                                                           # pero no múltiplos de 4
        print(numero_actual, end=' ')
        cnt += 1
    numero_actual += 1
cnt += 1
# input  output
# 11     3 6 9 15 8 21 27 30 33 39 42
# Aviso: 12 es divisible por ambos 3 y 4 --> asi que excluidos

"""

###### MÍNIMO DE VALORES ######

"""
-Leer T para el número total de casos testeados
-Para cada caso testeado leer el número de enteros a leer 
-Depués leer N enteros, cada uno en linea separada
-Para cada caso testeado, imprimir el  mínimo the los enteros N
"""
# Leer T para el número total  de casos testeados
total_casos = int(input("Ingres los casos totales: "))
# bucle exterior para caos
while total_casos > 0:
    numeros_cnt = int(input("Número de enteros a leer: "))  # Para cada caso testeado leer el número de enteros a leer
    pos = 0
    resultado = 0
    # Bucle interior para leer un caso
    while pos < numeros_cnt:
        valor = int(input("indique un valor"))
        if pos == 0:
            resultado = valor
        elif resultado > valor:
            resultado = valor
        pos += 1
    print(f'El valor mínimo es {resultado}')

# input
# Ingres los casos totales: 10
# Número de enteros a leer: 8
# enteros: 2, 8, 6, 4, 9, 7, 3, 1

# output
# El valor mínimo es 1
