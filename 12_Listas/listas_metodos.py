# mi_lista = [1, 5, 10, 17, 2]

# APPEND, EXTEND AND INSERT

# APPEND:recomendado para añadir un elemento, añade el elemento al final de la lista.
#mi_lista.append('holaa')
# print (mi_lista)  # [1, 5, 10, 17, 2, 'holaa']

# EXTEND: recomendado para añadir varios elementos, extiende la lista
# añadiendo los elementos de un ITERABLE(de algo más que un elemento, una secuencia...)
# otra_lista = [3, 1]  # ojo, hay más de un elemento en la lista y es ITERABLE (se puede recorrer con un bucle FOR)
# mi_lista.extend(otra_lista)
# print(mi_lista)  # [1, 5, 10, 17, 2, 'holaa', 3, 1]
# TypeError: 'int' object is not iterable
# mi_lista.extend(2) # ERROR, NO SE PUEDE AÑADIR UN SOLO OBJETO CON extend, es para más de uno.

# INSERT: inserta un elemento en una posición determinada
# mi_lista.insert(2, 'wow')
# print(mi_lista)  # [1, 5, 'wow', 10, 17, 2, 'holaa', 3, 1]
