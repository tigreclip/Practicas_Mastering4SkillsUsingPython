lst = [5, 7, 2]

# Algoritmo: procedimiento paso a paso para cálculos.
# MÉTODO SORT: ORDENA DE MENOR A MAYOR, por defecto,
# ALGORITMO INCORPORADO(in-place): NO CREA nueva MEMORIA, MODIFICA LA EXISTENTE.
lst.sort()
print(lst)  # [2, 5, 7]

# SORT: ordena de MAYOR A MENOR
lst.sort(reverse=True)
print(lst)  # [7, 5, 2]

# ERROR COMÚN, OJO: NO asignar el valor ordenado a la variable --->None
# lst = lst.sort()
print(lst)  # lst ahora es NONE!


# FUNCIÓN SORTED, Toma cualquier valor iterable(una secuencia de elementos) lo ordena,
lst_sorted = sorted(lst)  # lst_sorted [2, 5, 7]
# lst = NO CAMBIA

# ORDENAR UN STR, ORDENAR INVERSAMENTE UN STR
mi_str = 'zacb'
nueva_lista = sorted(mi_str)
print(nueva_lista)  # ['a', 'b', 'c', 'z']
nueva_lista = sorted(mi_str, reverse=True)
print(nueva_lista) # ['z', 'c', 'b', 'a']


sorted = sorted(mi_str) # SORTED es palabra reservada, evitar usarla en variables, ERROR
print(sorted)


