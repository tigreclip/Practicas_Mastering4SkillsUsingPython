"""
IMPRIMIR X
Leer un entero N, después imprimir una X  usando *, como en el ejemplo
*     *
 *   *
  * *
   *
  * *
 *   *
*     *
"""

num = int(input('Ingresa un nùmero impar: '))

for i in range(num):
    for j in range(num):
        if i == j or num - (i - 1) == j:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()
