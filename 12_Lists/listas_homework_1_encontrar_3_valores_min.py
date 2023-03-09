""" 
Leer un linea de N enteros
Encontrar lo 3 números mas bajos. Si hay menos de 3, tambien valen.
    · no cambiar el contenido de la lista o crear equivalente en memoria(p. ej. COPY)
    · no iterar sobre la lista más de una vez
Input       --> Output
4 1 3 10 8   -> 1 3 4
7 9 2        -> 2 7 9
1 -5         -> -5 1  
"""


def tres_mas_pequeños(lst):
    lst_peque = [] # creamos una lista para todos los num, es de ALCANCE LOCAL
                   # la idea: añadir todos los numeros a la lista
                   # ordenar y eliminar el 4º elementos(se piden solo 3 elementos)
                   # Así la lista siempre tendrá los 3 mínimos elementos
    for item in lst:
        lst_peque.append(item) # añadimos todos los elementos de lst a la nueva lista

        if len(lst_peque) > 3:
            lst_peque.sort() # el método .sort() ordena todos los elemetentos sin crear nueva memoria, 
            lst_peque.pop() # el método .pop() extrae el último elemento de una lista
                            # y lo muestra. OPCIONAL: indicar el indice a eliminar
    
    lst_peque.sort() # aseguramos que la lista está ordenada, sin añadir memoria!
    return lst_peque

if __name__ == '__main__':
    lst = list(map(int,input().split()))
    lst_peque = tres_mas_pequeños(lst)
    print(lst_peque)
    