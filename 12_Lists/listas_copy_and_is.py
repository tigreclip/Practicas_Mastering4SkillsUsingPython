# list(iterable)= constructor
# CREAMOS UNA LISTA iterable con 'list'
lst = list('Miguel')
print(len(lst))  # 6
print(lst)  # ['M', 'i', 'g', 'u', 'e', 'l']

nueva_lst = lst.copy()  # CREAMOS UNA NUEVA LISTA a partir de una copia(COPY)

# COMPROBAR SI APUNTAN A LA MISMA DIRECCIÓN DE MEMORIA
print(lst is nueva_lst)  # False, copy crea una nueva dirección en memoria

print(nueva_lst is nueva_lst + [1]) # False, tiene dirección de memoria diferente
