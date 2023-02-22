# ENCUENTRA EL ÍNDICE MAS ALTO DE 2 VALORES MÁXIMOS
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

lst = list(map(int, (input().split())))
