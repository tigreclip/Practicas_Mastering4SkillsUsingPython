# Homework 1: is increasing array? ('¿es una matriz creciente?)
# Leer una linea de N enteros

def valor_creciente(lst): # creamos la función con argumento ->lista 
    #COMPARAR CADA ELEMENTO CON EL ÚLTIMO
    for pos in range(1, len(lst)): # para cada posición en un rango entre 1 y longitud de la lista...
        if lst [pos]<= lst[pos-1]: # si lista[posicion] es menor o igual a lista[posicion - 1]
            return False # retorna Falso
        return True # Si no, retorna verdadero (return no necesita tener indicado "else:")


if __name__ == '__main__': # Si es el programa principal, continuar
    lst = list(map(int,(input().split()))) # crea una lista de enteros separados desde un input
    
    status = valor_creciente(lst) # almacena la respuesta de  la funcion valor_creciente

    if status: # si estatus es True 
        print('YES')  # imprimir YES
    else: # si no, 
        print('NO')  # imprimir NO

