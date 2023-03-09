#  REEMPLAZAR MINIMO MAXIMO

#  Leer una línea de N enteros
#  imprimir los números depués de :
#   -encontrar el número mínimo en esos números
#   -encontrar el número máximo en esos números
#   -reemplazar CADA mínimo con su máximo y viceversa
# input                       output
# 4 1 3 10 8 10 10      4 10 3 1 8 1 1
#  Crear funcion "def cambiar_min_max_insitu(lst)"
#   - la función no retorna una lista. realiza modificaciones 'insitu' 
 
def reemplazar_min_max(lst):
    mn = min(lst) # encontrar el número MÍNIMO en esos números
    mx = max(lst) # encontrar el número MÁXIMO en esos números

    for idx, item in enumerate(lst): # REEMPLAZAR cada MÍNIMO con su MÁXIMO y viceversa
        if item == mn:
            lst[idx] = mx
        elif item == mx:
            lst[idx] = mn

if __name__ == '__main__':
    lst = list(map(int,input().split())) #  Leer una línea de N enteros
    print(reemplazar_min_max(lst))
    print(lst)

