# LIST ES MUTABLE

# Podemos cambiar el valor y la lista origen(lst) es cambiado
def f1(lst):
    lst[0] = 10


def f2(lst):
    lst = [7, 8, 9]  # variable de alcance local,
    return lst


mi_lista = [1, 2, 3, 4, 5]
otra_lista = mi_lista
print(otra_lista is mi_lista)  # True , IS comprueba que apuntan a la misma memoria

f2(mi_lista)
print(mi_lista[1])  # 2 , SIN CAMBIOS

mi_lista = f2(mi_lista)  # SE REEMPLAZA UNA LISTA POR OTRA, diferente memoria
print(mi_lista[1])  # 8 - NUEVA LISTA
print(otra_lista[1])  # 2 - NO AFECTA


