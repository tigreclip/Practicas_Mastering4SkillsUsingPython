mi_lista = [1, 2, 3, 4]
# REVERSE, metodo que modifica la lista original,
mi_lista.reverse()
print(mi_lista)  # [4, 3, 2, 1]

mi_lista += ['holi']
# REVERSED, Función que DEVUELVE UN OBJETO ITERABLE
nueva_lista = reversed(mi_lista)  # no devuelve list
print(nueva_lista)  # <list_reverseiterator object at 0x000001DF0B809FF0>
# PODEMOS TRANSFORMAR EL OBJETO EN UNA LISTA:
nueva_lista_rev_1 = list(reversed(mi_lista))
print(nueva_lista_rev_1)  # lista REVERSEITERATOR

# COPY() Y .REVERSE(): esto es un poco tonto, ya que es mejor la opción anterior
nueva_lista_rev_2= mi_lista.copy()  # Copia de mi_lista
nueva_lista_rev_2.reverse()  # copia con MÉTODO .REVERSE

