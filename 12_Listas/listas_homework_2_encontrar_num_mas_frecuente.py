""" 
Leer un línea de N enteros. Cada entero es -50 <= valor <= 270
Encontrar el valor que se repite mas número de veces
    · si hay varias soluciones, encontrar el valor más pequeño

Input             --> Output
-1 2 -1 3 -1 5 5  - Valor -1 repetido 3 
"""

def mas_frecuente(lst):
    # cambiamos todos los datos para empzar de CERO(asi indexamos con normalidad)
    # mas tarde desharemos el efecto
    # para hacer esto: sólo restar el mínimo
    # p. ej. si input es -10 20 -2 9 20
    # el mínimo es -10
    # restado de todos: 0 30 8 19 30
    # encontramos el máx. 30 
    mn, mx = min(lst), max(lst)
    lst_frequente = [0] *(mx - mn +1)

    for valor in lst:
        print(valor - mn)
        lst_frequente[ valor - mn] += 1

    valor_max = lst_frequente.index(max(lst_frequente))

    return valor_max + mn, lst_frequente[valor_max]






lst = list(map(int,input().split()))