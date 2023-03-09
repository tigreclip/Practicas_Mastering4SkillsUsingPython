# Leer un línea de N eneros. NO están ORDENADOS
# Imprimir la lista única de números, pero manteniendo el orden dado
# input: 1 5 5 2 5 7 2 3 3 3 5 2 7
# output: 1 5 2 7 3
#   nota: input no es una lista ordenada
#   nota: output mantiene el orden original: p. ej. 5 aparece antes que 2

""" 
############################  usando SET ################################
def get_num_unicos(lst):
    lst_unicos = []
    num_unicos = set(lst)
    for num in num_unicos:
        lst_unicos.append(num)
    return lst_unicos

if __name__ == '__main__':
    lst = list(map(int,input().split()))

    get_num_unicos(lst)
    print(get_num_unicos(lst)) """

############################  usando NOT IN ################################

def num_unicos_desordenados(lst):
    lst_unicos = []

    for item in lst:
        if item not in lst_unicos:
            lst_unicos.append(item)
    return lst_unicos

if __name__ == '__main__':
    lst = list(map(int,input().split()))

    lst = num_unicos_desordenados(lst)
    print(lst)

