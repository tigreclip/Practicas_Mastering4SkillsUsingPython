#COMPROBAR QUE UN VALOR ESTÁ CRECIENDO, más 'pythonic style"

def valor_creciente(lst):

    # Creamos una lista que no permitaa comparar elemento por elemento
    ultimo_num = lst[len(lst) - 1]
    lista_desplazados = lst.copy()
    lista_desplazados.pop(0) # se elimina el primero, porque no hay nada antes con que comparar
    lista_desplazados.append(ultimo_num) # se añade el último a la lista para que se pueda comparar consigo mismo y cuadre
    
    #input      [10 20 30 40]
    #output --> [20 30 40 40] todo lo anterior es para dejar una lista como esta, quitando el primer elemento (10) y añadiendo el ultimo elemento(40), otra vez, para tener dos listas con la misma longitud.
    print(lst)
    print(lista_desplazados)

    return lst <= lista_desplazados



if __name__ == '__main__': # Si es el programa principal, continuar
    lst = list(map(int,(input().split()))) # crea una lista de enteros separados desde un input
    
    status = valor_creciente(lst) # almacena la respuesta de  la funcion valor_creciente

    if status: # si estatus es True 
        print('YES')  # imprimir YES
    else: # si no, 
        print('NO')  # imprimir NO