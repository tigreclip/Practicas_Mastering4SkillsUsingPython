# Leer una línea de N enteros.
# Cada entero es 0<= valor <= 150.
# Encontrar el valor con más repeticiones:
#   · si hay varias soluciones: encontrar el valor más pequeño.
# Input          --->     Output
# 1 2 1 3 1 5 5       Valor 1 repetido 3
#   Observar:
#   1, repetido 3 veces: el que más se repite
#   2, repetido 1 vez
#   5, repetido 2 veces


# ############## Número más frecuente (LENTO) #############

def mas_frecuente_lento(lst):
    mas_valor, frecuencia = None, 0
    for valor in lst:
        cnt = lst.count(valor)
        if cnt > frecuencia:
            mas_valor, frecuencia = valor, cnt
        elif cnt == frecuencia:
            mas_valor = min(mas_valor, valor)
        return mas_valor, frecuencia


if __name__ == '__main__':
    lst = list(map(int, input().split()))  # Leer una línea de N enteros.
    mas_valor, frecuencia = mas_frecuente_lento(lst)
    print('Valor', mas_valor, 'repetido ', frecuencia)

# ############## Número más frecuente (RÁPIDO) #############
# 5 5 5 5 2 3 3 3 3 --> Valor 3 repetido 4
# lst = list(map(int, input().split()))  # Leer una línea de N enteros.
#
# lst = list(map(int, input().split()))  # Leer una línea de N enteros.
# def mas_frecuente(lst):
#     for i in lst:
#         if i < 0 and i < 150:
#             cont = lst.count(i)
#             return (f'{i} se repite {cont}')
#
# mas_frecuente(lst)

# Usamos otra lista
# Por ahora: piensa que la palabra ARRAY = LIST
# Usaremos un truco llamado 'FREQUENCY ARRAY'
