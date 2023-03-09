# Leer una linea de N enteros. ESTÁN ORDENADOS
#   -la solucion previa puede funcionar. ¿Pero podemos hacer un código más rápido?
#  Imprimir la lista de números únicos, pero manteniendo el orden dado
# Input: 1 1 2 2 2 5 6 6 7 8 9 9
# Output: 1 2 5 6 7 8 9
# Nota: la entrada es una lista ordenad

########### usando NOT IN ###############
def num_unicos_desordenados(lst):
    num_unicos = []

    for idx, item in enumerate(lst):
        # en una lista ordenada: si el num previo es != a mi --> soy el nuevo num
        if idx == 0 or lst[idx] != lst[idx-1]: # si es el primero o no es el último
            num_unicos.append(item)
    
    return num_unicos

if __name__ == '__main__':
    lst = list(map(int,input().split()))

    lst = num_unicos_desordenados(lst)
    print(lst)


   


