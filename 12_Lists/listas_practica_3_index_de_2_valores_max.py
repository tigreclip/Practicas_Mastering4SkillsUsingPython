# ENCUENTRA EL ÍNDICE MÁS ALTO DE 2 VALORES MÁXIMOS
# Leer una línea de N enteros (todos en la misma línea)
# Encontrar el índice del máximo valor y del 2º máximo valor
#   si hay más de una respuesta: encontrar la primera coincidencia
# input:
#   10 20 3 30 7
#   idx1 3 value 30
#   idx2 1 value 20

#   10 20 30 35 30 17
#   idx1 2 value 30
#   idx2 4 value 30

lst = list(map(int, (input().split())))  # Leer una línea de N enteros (todos en la misma línea)


def argmax(lista):  # encuentra el ÍNDICE de MÁXIMO valor.:
    if len(lista) == 0:  # si la lista está vacía, retorna None
        return None
    return lista.index(max(lista))  # Si no, retorna el máximo valor y después el índice


# input:
#   10 20 3 30 7
print(argmax(lst))  # 3


# ############################## DOS MÁXIMOS (lento) ###############################

def max2_argax_v1(lista):
    # Dada una lista: retornar los índices del primer y segundo máximo num
    if len(lista) < 2:
        return None, None
    # conseguir máximo índice y valor
    max1_idx = argmax(lista)
    max1_valor = lista[max1_idx]

    # reemplazar con un valor muy pequeño
    min_valor = min(lista)
    lista[max1_idx] = min_valor - 1

    max2_idx = argmax(lista)

    # deshacer el cambio a la lista
    lista[max1_idx] = max1_valor

    return max1_idx, max2_idx


print(max2_argax_v1(lst))  # input: 10 20 3 30 7 ---> (3, 1)

# ##############################  DOS MÁXIMOS (rápido)  ##############################


# Código iterable con un SIMPLE BUCLE (loop)
# 2 variables para los 2 máximos
# Iterar sobre la lista y actualizar a la vez
# Digamos que hasta ahora tenemos 20 10
#   - valor actual es 30 --> ahora debería ser 30 20
# Digamos que hasta ahora tenemos 20 10
#   - valor actual es 15 --> ahora debería ser 20, 15
# Digamos que hasta ahora tenemos 20 10
#   - valor actual es 20 --> ahora debería ser 20, 20

def max2_argax_v1(lst):
    # comprobar que la lista tiene dos o más elementos
    if len(lst) < 2:
        return None, None
    
    # usar las primeras dos posiciones para los dos máximos superiores
    pos_max1, pos_max2 = 0, 1
    if lst[pos_max1] < lst[pos_max2]:
        pos_max1, pos_max2 = 1, 0
        
    # ITERAR Y ACTUALIZAR índices basados en el actual elemento SI ES MAYOR
    for pos_actual in range(2, len(lst)):
        if lst[pos_max1] < lst[pos_actual]:
            pos_max1, pos_max2 = pos_actual, pos_max1
        elif lst[pos_max2] < lst[pos_actual]:
            pos_max2 = pos_actual

    return pos_max1, pos_max2


print(max2_argax_v1(lst))
