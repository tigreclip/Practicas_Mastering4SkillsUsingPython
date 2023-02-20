mi_lista = [1, 5, 10, 17, 2]

# APPEND, EXTEND AND INSERT

# APPEND:recomendado para añadir un elemento, añade el elemento al final de la lista.
mi_lista.append('holaa')
print(mi_lista)  # [1, 5, 10, 17, 2, 'holaa']

# EXTEND: recomendado para añadir varios elementos, extiende la lista
# añadiendo los elementos de un ITERABLE(de algo más que un elemento, una secuencia...)
otra_lista = [3, 1]  # ojo, hay más de un elemento en la lista y es ITERABLE (se puede recorrer con un bucle FOR)
mi_lista.extend(otra_lista)
print(mi_lista)  # [1, 5, 10, 17, 2, 'holaa', 3, 1]
# TypeError: 'int' object is not iterable
# mi_lista.extend(2) # ERROR, NO SE PUEDE AÑADIR UN SOLO OBJETO CON extend, es para más de uno.

# INSERT: inserta un elemento en una posición determinada
mi_lista.insert(2, 'wow')
print(mi_lista)  # [1, 5, 'wow', 10, 17, 2, 'holaa', 3, 1]
mi_lista = [1, 5, 'wow', 10, 17, 2, 'holaa', 3, 1]

# POP: ELIMINA DE LA LISTA por índice de un elemento y LO RETORNA
print(mi_lista.pop())  # 1, por defecto es el último elemento
print(mi_lista.pop(6))  # 'holaa# '

# DEL: ELIMINA el elemento de una posición determinada
del mi_lista[0]
print(mi_lista)  # [5, 'wow', 10, 17, 2, 3]

# REMOVE: ELIMINA EL PRIMER VALOR QUE ENCAJE, no el índice.
mi_lista.remove(17)
print(mi_lista)  # [5, 'wow', 10, 2, 3]

# ValueError: list.remove(x): x not in list
# mi_lista.remove('kih') # error, NO EXISTE el elemento

# INDEX: BUSCA y RETORNA EL PRIMER index
print(mi_lista.index('wow'))  # 1

# ValueError: 'yiuuS' is not in list
# print(mi_lista.index('yiuuS'))ç

# CLEAR: VACIA la lista
mi_lista.clear()
print(mi_lista)