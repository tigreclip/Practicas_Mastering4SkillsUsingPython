s1 = 'miguel' # string
s2 = 'perez'  # string
s3 = s1 + s2 * 2 # miguelperezperez

lst = list(s1) # ['m', 'i', 'g', 'u', 'e', 'l']

# iterar, string o cadena de caracteres
for idx, char in enumerate(s1):
    print(idx, char)
""" 
0 m
1 i
2 g
3 u
4 e
5 l
 """

 # boolean
print('most'<'Most') # False : MAYÚSCULAS SON DE MENOR VALOR QUE MINÚSCULAS

a, b, c, d = 'Most'
print(c) # s

# Desempaquedato de listas
a, b = [3, 4]

############################# CON FUNCIONES #############################

s1 = 'moST'

print(len(s1), min(s1), max(s1)) # 4 S o

print((sorted(s1))) # ['S', 'T', 'm', 'o'] ordenados de menor a mayor

print(tuple(reversed(s1))) # ('T', 'S', 'o', 'm') elementos en orden inverso

############################# INDEXAR Y SLICING #############################

# Lo mismo que las tuplas. STRING ES INMUTABLE

s1 = 'moST'
print(s1[0],s1[-1]) # m T -> INDEXAR

print(s1[2:]) # ST  -> SLICING
print(s1[::]) #moST -> SLICING
print(s1[:: -1]) # TSom  -> SLICING
print(s1[:]) #moST -> SLICING
print(s1[: -1]) # moS  -> SLICING

# STRING ES INMUTABLE
# s1[0] = 'c' 
# TypeError: 'str' object does not support item assignment

# del s1[0]
# TypeError: 'str' object doesn't support item deletion

############################# LIST COMPREHENSION, para usar en bucles FOR #############################

lst = ['Hola', 'Mundo', 'Python', 'es', 'guay']
primeras_letras = [palabra[0] for palabra in lst] # list comprehension, para bucle 'for'
print(primeras_letras) # ['H', 'M', 'P', 'e', 'g'] # DEVUEVE LAS PRIMERAS LETRAS de cada palabra

primeras_letras = [palabra[0].lower() for palabra in lst]
print(primeras_letras) # ['h', 'm', 'p', 'e', 'g'] # CONVIERTE A MAYÚSCULAS las primeras letras de cada palabra

mi_str = "Por favor 10 encuentra 123todos los digit0s"
digitos = [int(char) for char in mi_str if char.isdigit()]
print(digitos) # [1, 0, 1, 2, 3, 0]
 
############################# INMUTABILIDAD #############################

mi_str = 'miguel'

# mi_str[3] = 'G' # inmutable, da error. 
# TypeError: 'str' object does not support item assignment

# EL ÚNICO MODO DE CAMBIAR UN STRING ES CONSTRUIR OTRO STRING
mi_str = mi_str[:2] + mi_str[2].upper() + mi_str[3:]
print(mi_str) # miGuel

mi_str2 = mi_str
print(mi_str is mi_str2) # True
print(id(mi_str)) # 3086128402608
mi_str += 'sandra' # se crea nueva dirección de memoria, es otro objeto
print(id(mi_str)) # 3086128402672
print(id(mi_str2)) # 3086128402608
print(mi_str is mi_str2) # False
