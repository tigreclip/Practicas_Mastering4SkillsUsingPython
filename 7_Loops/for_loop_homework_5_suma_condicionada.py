"""
Leer tres enteros N, A, B.
Imprimir la suma de los números entre 1 y N
cuya suma está entre A y B

input   output
20 2 5 -> 84

10 1 2 -> 13
100 4 16 -> 4554
"""
n, a, b = map(int, input().split())
total = 0

for i in range(1, n+1):
    tmp = i
    suma_num = 0

    while tmp > 0:
        suma_num += tmp % 10
        tmp //= 10

    if a <= suma_num <= b:
        total += 1
print(total)
