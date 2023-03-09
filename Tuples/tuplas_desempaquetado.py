
########### DESEMPAQUETADO DE TUPLAS ###########
lst = 1, 2, 4, 5
print(lst)

a, b, c, d = lst # desempaquetado normal
a, _, _, _ = lst # si da igual el parámetro, usamos _ 

# si no estoy seguro del número total? 
# USAMOS *

a, b, *c = lst 
# a = 1, b = 2, c = [4, 5]
print(c) # [4, 5] 

*a, b, c = lst
# a = [1, 2], b = 4, c = 5
print(a) # [1, 2]

a, *b, c = lst
# a = 1, b = [2, 4], c = 5
print(b) # [2, 4]

# Aunque podemos hacer lo mismo con "slicing"
# el operador * es mas elegante y hace el código más simple

def f(*items): # * indica que puede recibir interminables parámetros
    print(items)

f(1, 2, 3, 4, 5) # 1, 2, 3, 4, 5)

########### MÁS DESEMPAQUETADO DE TUPLAS ###########

lst = [1, 2, 3]
print(lst) # [1, 2, 3] IMPRIME UNA LISTA
print(*lst) # 1 2 3 primero DESEMPAQUETA, DEPUES IMPRIME 3 ARGUMENTOS RECIBIDOS, NO 1 !!!

def f(a, b):
    print(a + b)

# f(*lst)  TypeError: f() takes 2 positional arguments but 3 were given
# f pide 2 argumentos(a, b) y 
# le pasamos *lst que son 3 argumentos[1, 2, 3]: ERROR
lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]

unir = [*lst_1, *lst_2]
print(unir) # [1, 2, 3, 4, 5, 6]

###########  DESEMPAQUETADO PROFUNDO DE TUPLAS ###########

lst = 1, 2, (5, 6) # tupla dentro de una tupla

# a, b, c, d = lst --> ValueError: not enough values to unpack (expected 4, got 3)
# error: pedimos el valor de 4 argumentos (a, b, c, d)
# pero SÓLO hay 3 valores -> 1, 2 y (5, 6)

# DESEMPAQUETADO PROFUNDO
a, b, (c, d) = lst
print(a, b, c, d) # 1 2 5 6

t = 1, 2, 3, (4, (5, 6)) # tupla dentro de una tupla, dentro de una tupla
a, b, c,(d, (e, f)) = t
print(a, b, c, d, e, f) # 1 2 3 4 5 6