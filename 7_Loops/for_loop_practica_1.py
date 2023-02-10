"""
Leer T para número de test
para cada test, leer entero N
depués leer N enteros a, b, c...en líneas separadas
calcular la suma de:
    (a, b*b, c*c*c*, d*d*d*d, e*e*e*e*)
    (número k repetido k veces
"""

# ##### RECORDANDO: SUMA ESPECIAL #####

# test_cases = int(input())  # Leer T para número de test
# for case in range(test_cases):  # para cada test, leer entero N
#     n, suma = int(input()), 0
#     for pos in range(1, n+1):  # depués leer N enteros a, b, c...en líneas separadas
#         suma += pos
#         print(f'La suma de 1 a {n} = {suma}')


casos_totales = int(input())

for caso in range(casos_totales):
    N, suma = int(input()), 0

    for pos in range(N):
        valor, resultado = int(input()), 1

        # loop para calcular la suma: a, b*b, c*c*c
        for i in range(pos + 1):
            resultado *= valor
        suma += valor
    print(f'La suma es {suma}')
