##################### ZIP función #####################

# Cuando tienes múltiples secuencias y quieres iterar
# para obtener un simple elemento de cada secuencia: necesitamos ZIP

numeros = [1, 2, 3]
letras = ['a', 'b', 'c']

# CONTRUCTRO de la clase zip: def __init__(self, *iterables)
# toma a un grupo de iterables
# y ellos retornan un iterador que podemos usar para iterar

zipped = zip(numeros, letras)
print(list(zipped))
# [(1, 'a'), (2, 'b'), (3, 'c')]

palabras = ['miguel', 'sandra','iván']

print(zip(numeros, letras, palabras)) 
# imprime la direccion en memoria <zip object at 0x0000024989500200>

# ZIP ---> LIST --> 
print(list(zip(numeros, letras, palabras))) # lista de 3 tuplas
# [(1, 'a', 'miguel'), (2, 'b', 'sandra'), (3, 'c', 'iván')]

##################### ZIP  #####################

numeros = [1, 2, 3]
letras = ['a', 'b', 'c']
palabras = ['miguel', 'sandra','iván']

# genera una TUPLA CON LOS ELEMENTOS EN ZIP
for tupla_elemento in zip(numeros, letras, palabras):
    print(tupla_elemento)

""" 
(1, 'a', 'miguel')
(2, 'b', 'sandra')
(3, 'c', 'iván')
"""

# DESEMPAQUETA LA TUPLA ZIP DIRECTAMENTE
for numero, letra, palabra in zip(numeros, letras, palabras):
    print(numero, letra, palabra)

""" 
1 a miguel
2 b sandra
3 c iván

 """

 ##################### ZIP Y DESEMPAQUETADO PROFUNDO #####################

numeros = [1, 2, 3]
letras = ['a', 'b', 'c']
palabras = ['miguel', 'sandra','iván']

# INDICE(ZIP(TUPLAS))
for idx, tupla_elemento in enumerate(zip(numeros, letras, palabras)):
    print(idx, tupla_elemento)

"""

0 (1, 'a', 'miguel')
1 (2, 'b', 'sandra')
2 (3, 'c', 'iván')
"""

for idx, (numero, letra, palabra) in enumerate((zip(numeros, letras, palabras))):
    print(idx, numero, letra, palabra)

"""

0 1 a miguel
1 2 b sandra
2 3 c iván
"""

 ##################### DIFERENTES LONGITUDES #####################

 # y si las secuencias tienen diferentes longitudes?
 # SE PARA EN LA LONGITUD MAS CORTA

items = list(zip(range(10, 15), range(100)))
print(items)
# (10, 0), (11, 1), (12, 2), (13, 3), (14, 4)]
# OJO:  se para despues de sólo 5 elementos porque ->range(10, 15)

# UNZIP
secuen_1, secuen_2 = zip(*items)
print(secuen_1) # (10, 11, 12, 13, 14) -> viene de la longitud de range(10, 15)
print(secuen_2) # (0, 1, 2, 3, 4) --> muestra solo 5 valores, aunque el rango es 100 -->range(100)

