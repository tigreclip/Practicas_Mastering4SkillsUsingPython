# Leer una línea de N enteros( N>1)
# Encontrar un par de índices cuyas SUMAS DE VALORES SEAN  MÁXIMAS
# Input         -->     Output
# 2 15 10 3 50  -->     65 (de 50 +15)
#       Hacerlo con bucles anidados(nested loops)
#       ¿Puedes hacerlo con un bucle lineal?
#           P. ej. sin anidar pero varios bucles de un giro

lst = input('ingresa número').split()
print(lst)


def par_maxsuma(lst):
    pos1, pos2 = 0, 1

    for i in range(len(lst)): # por cada elemento de la lista
        for j in range(i + 1, len(lst)): # por cada elemento + 1 de la lista (asi no se solapan valores de i y j)
            if lst[pos1] + lst[pos2] < lst[i] + lst[j]: # si pos1 + pos2 < que i + j
                pos1, pos2 = i, j  # pos1 = i, pos2= j
    return pos1, pos2

print(par_maxsuma(lst))
