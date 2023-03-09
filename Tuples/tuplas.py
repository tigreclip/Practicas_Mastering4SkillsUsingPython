""" 
TUPLES: coleccion ORDENADA e INMUTABLE de objetos
-Varias SIMILITUDES CON LIST:
    ·iteración
    ·indexación
    ·slicing(rebanar)
    ·comparación
    ·elementos múltiples: min(), max(), sorted()
Más:
-Tipo de datos INMUTABLES: no se pueden cambiar ni borrar
    ·Muchos métodos no existen: append, insert, remove
    ·Podemos cambiar el contenido de un elemento, si ese elemento es mutable
-ITERACIÓN MAS EFICIENTE QUE EN UNA LISTA
-Key con Diccionario. LIST no puede
-Retorno múltiple de una función o asignamiento múltiple.

 """
# la coma (,) es la que genera la tupla, no los paréntesis
def f():
    return 1, 2, 3 # retorna una tupla (1, 2, 3)

a, b, c = f() # desempaquetado de una tupla

a, _, _ = f() # (_) se usa para desempaquetar una tupla sin importar los parámetros

juntos = f()
print(type(juntos)) # <class 'tuple'>

x, y, z = juntos # desempaquetado

######### MAL DESEMPAQUETADO #########

# MENOS PARÁMETROS QUE VALORES EXISTENTES EN LA TUPLA
# X, Y = juntos # ValueError: too many values to unpack (expected 2)

# MAS PARÁMTROS QUE VALORES EXISTENTES EN LA TUPLA
# x, y , z, w1, w2 = juntos #ValueError: not enough values to unpack (expected 5, got 3)

# mi_tupla = ( 5, 6, 7) # CREAR TUPLA: es la coma ',' la que crea la tupla y no los paréntesis

# x, y, z = juntos # UNPACK: desempaquetado

# x, y = y, x # SWAP:intercambio de valores de los parámetros

#################### CREACIÓN DE TUPLA ##########################################

t = ('miguel', 12, 2.5, 12)  # 4 items
t = ('miguel', 12, 2.5, 12, )  # 4 items también! después de una coma, si no hay valor no hay item

# tuplas de 1 item
t = (10) # MAL, NO ES TUPLA
print(type(t)) # <class 'int'>

t = (10,) # BIEN, la coma ',' crea la tupla!
print(type(t)) # <class 'tuple'>

# LEN, sirve igual ya que TUPLE ES ITERABLE
print(len((True, 'miguel'))) #  longitud de 2 elementos

# TODOS SON TUPLAS
X, Y = 1, 2
X, Y = (1, 2)
(X, Y) = (1, 2)

# TUPLE: constructor de tuplas
# MAL: necesita 1 argumento y le pasamos 3
# t = tuple(1, 2, 3) # TypeError: tuple expected at most 1 argument, got 3

# BIEN
t = tuple([1, 2, 3]) # 1 argumento: una lista
t = tuple((1, 2, 3)) # 1 argumento: otra tupla
t = tuple('maximo') # 1 argumento STR genera una tupla con los CARACTERES SEPARADOS
                    # ('m', 'a', 'x', 'i', 'm', 'o')
print(t)

#################### INDEXING Y SLICING ####################

# IGUAL QUE en las LISTAS

numeros = (10, 2, 7, 5, 3)

print(numeros[0], numeros[-1]) # 10 3
print(numeros[::]) # (10, 2, 7, 5, 3)
print(numeros[::-1]) # (3, 5, 7, 2, 10)

for item in numeros:
    print(item, end=' ') # 10 2 7 5 3

# 
# ERROR: no se puede cambiar el valor de un elementos de la tupla
# numeros[0] = 4 # TypeError: 'tuple' object does not support item assignment


#################### MÉTODOS Y FUNCIONES ####################

numeros = (10, 2, 7, 2, 2, -5)

# FUNCIONES QUE NO ALTERAN EL VALOR: INDEX Y COUNT
print(numeros.count(2))  # 3
print(numeros.index(2))  # 1

# FUNCIONES QUE ALTERAN EL VALOR DAN ERROR!
# numeros.remove[0] # AttributeError: 'tuple' object has no attribute 'remove'
# del numeros[0]    # TypeError: 'tuple' object doesn't support item deletion

print(min(numeros),max(numeros)) # -5 10

lst = sorted(numeros) # SORTED DEVUELVE UNA LISTA de menor a mayor valor
print(lst) # [-5, 2, 2, 2, 7, 10]
print(tuple((sorted(numeros)))) # TUPLE: CONVIERTE LISTA en TUPLE

lst = reversed(numeros) # REVESED DEVULVE UNA LISTA con los elementos con el orden alrevés
print(tuple(reversed(numeros))) #

#################### CAMBIO O NO?! ####################

class Empleado:
    def __init__(self):
        self.id = 0
lst = [1, 2, 3, 4]
emp = Empleado()

tupla = (lst, emp)
print(tupla[0]) # [1, 2, 3, 4] 

# NO PODEMOS CAMBIAR LOS ELEMENTOS de un tupla, es INMUTABLE
# tupla[0] = [6, 7] #TypeError: 'tuple' object does not support item assignment

# PERO SI PODEMOS CAMBIAR EL CONTENIDO DE ESOS ELEMENTOS
lst[0] = 100
emp.id = 20
 
print(tupla[0]) # [100, 2, 3, 4]


#################### OPERADORES + Y * ####################
t1 = (1, 2, 3)
t2 = ('miguel', True)

t = t1 + 2 * t2 # SUMA DE TUPLAS
print(t) # (1, 2, 3, 'miguel', True, 'miguel', True)

# sólo se pueden encadenar TUPPLAS CON TUPLAS, NO CON LISTAS
# t = t1 + [2, 3, 4] #TypeError: can only concatenate tuple (not "list") to tuple

print(('hola') *4) # OJO, no es tupla, le falta ',' 
# holaholaholahola

print(('hola',)*4) # OJO, es tupla por la coma
# ('hola', 'hola', 'hola', 'hola')