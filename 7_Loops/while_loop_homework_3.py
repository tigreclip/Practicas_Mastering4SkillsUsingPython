
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

vamos a desarrolar fórmulas para el número de espacio y el número de estrellas
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

###### Múltiplos de 2 especiales ######

"""
Leer un entero N(1<=30): Imprimir los primeros numeros N que:
    -sean múltiplos de 3 pero no multiplos de 4

"""

#input  output
# 11     3 6 9 15 8 21 27 30 33 39 42
# Aviso: 12 es divisible por ambos 3 y 4 --> asi que excluidos