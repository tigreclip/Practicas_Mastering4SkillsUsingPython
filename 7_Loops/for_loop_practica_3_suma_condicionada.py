"""
Leer 3 enteros N, M, W.
Encontrar número total de los  A + B <= C
donde:  1<=A<=N
        A<=B<=M
        1<=C<=W
inputs: 100 200 20
output: 745
"""

N, M, W = map(int, input('Ingresa tres números separados por espacio').split())

cont = 0
for a in range(1, N + 1):
    for b in range(1, M + 1):
        c = a + b
        if a <= c <= W:
            cont += W - a + 1
print(cont)
