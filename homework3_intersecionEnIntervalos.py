# Leer 4 enteros que representes 2 intervalos, imprimir su intervalo de inserciò(los nùmeros que tienen en comùn)
# si no está, imprimir -1
# inputs
# 1 6  3 8  -> 3 8

# Leer 4 enteros que representes 2 intervalos, imprimir su intervalo de inserciò(los nùmeros que tienen en comùn)
s1, e1, s2, e2 = map(int, input("Ingresa cuatro números: ").split())

# si no está, imprimir -1
if e1 < s2 or e2 < s1:
    print(-1)
# inputs
# 1 6  3 8  -> 3 8
else:
    if s1 < s2:
        s1 = s2 # màximo de (s1, s2)
    if e1 > e2:
        e1 = e2 # mínimo de (e1, e2)
    print(s1, e1)
    
    """
    Test
    1 15 20 30 -> -1
    20 30 1 15 -> -1
    1 6 1 6 -> 1 6
    1 6 1 3 -> 1 3
    1 6 2 3 -> 2 3
    1 6 3 8 -> 3 6
    3 8 1 6 -> 3 6
    """