# python provee de LISTA DE DATOS ESTRUCTURADA que nos permite tener diferentes objetos de manera cómoda
# LISTA es una secuencia ordenada de elementos:
#     - Pueden ser de varios tipos
#     - Es una clase MUTABLE

# CREACIÓN DE LISTA
mi_lista = [1, 2, 3, 4]

# LEN method,para saber la logitud(n.º elementos) de una lista.
print(len(mi_lista))  # 4

# IN, comprueba que exista un elemento en la lista: True o False
print((2 in mi_lista))  # True
print((9 in mi_lista))  # False

# LISTA: VER TODOS LOS ELEMENTOS:
#    1) FOR LOOP, bucle "for", lo hace ITERANDO (pasa por cada elemento de una secuencia y lo devuelve)
for item in mi_lista:
    print(item, end=' ')
print()  # 1 2 3 4

#    2) PRINT, muestra TODOS los elementos de la lista
print(mi_lista)  # [1, 2, 3, 4]

# LISTA con diferentes tipos datos:
mi_lista = [1, "gallifante", 4.5]
# IndexError: list assignment index out of range ( que no existe ese indice indicado)
mi_lista = [1, "gallifante", 4.5]  # indices--> [0, 1, 2]
mi_lista[3] = 0  # Dá error porque el índice[3] no existe

# INDEXING, indexar
# ITERAR UNA LISTA:
# 1) de 1 a n de 0 hasta len(lista-1)
# 2) 0 to n-1 de n+1 hasta n
