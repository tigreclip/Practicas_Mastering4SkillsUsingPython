"""
Leer un entero N(<500)
imprimir SI, si es primo*.
Imprimir NO, si no es primo*.

*PRIMO: número > 1 , no es multiplicable por dos números pequeños
 --> número%loquesea != 0
 --> los primeros números primos son:
 2, 3, 5, 7, 9, 11, 13, 17, 19, 23 y 29

 input output
 13     SI
 12     NO (p.e. 12=2*6, asi es divisible entre 2 y 6)
"""

num = int(input())

if num <= 1:
    print('NO')
else:
    is_ok = True

    for i in range(2, num):
        if num % i == 0:
            is_ok = False
            break
    if is_ok:
        print('SI')
    else:
        print('NO')
