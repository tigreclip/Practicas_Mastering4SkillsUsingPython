# Leer diez números
# Encontrar el número de mayor valor
# Imprir resultado
# RESTRICION: en todo el código SOLO debe haber 2 VARIABLES definidas

#ASI ES COMO LO HE ECHO (más abajo está el ejercio como en el tutorial)
resultado = float(input("Ingrese el primer número: ")) #lectura del primer resultado

#lectura de los otros nueve números:
contador = 0
while contador < 9:
    contador += 1
    num = float(input("Ingrese el siguiente número: "))
    if resultado < num:
        resultado = num
# Imprimir el número de mayor valor
print(resultado)

# Inputs ( cada entero en una linea separada)
# 1
# 67
# -6
# 88
# -45
# 129
# 90
# 65
# 77
# 34

# Output ---> 129

"""
#ASI ES COMO LO HACEN EN EL TUTORIAL 
resultado = float(input())#leer el primer número

num = float(input("Ingrese el siguiente número: ")) # leer el siguiente número
if resultado < num:
    resultado = num
    
num = float(input("Ingrese el siguiente número: ")) # leer el siguiente número
if resultado < num:
    resultado = num
    
num = float(input("Ingrese el siguiente número: ")) # leer el siguiente número
if resultado < num:
    resultado = num

num = float(input("Ingrese el siguiente número: ")) # leer el siguiente número
if resultado < num:
    resultado = num

num = float(input("Ingrese el siguiente número: ")) # leer el siguiente número
if resultado < num:
    resultado = num
    
num = float(input("Ingrese el siguiente número: ")) # leer el siguiente número
if resultado < num:
    resultado = num

num = float(input("Ingrese el siguiente número: ")) # leer el siguiente número
if resultado < num:
    resultado = num

num = float(input("Ingrese el siguiente número: ")) # leer el siguiente número
if resultado < num:
    resultado = num

num = float(input("Ingrese el siguiente número: ")) # leer el siguiente número
if resultado < num:
    resultado = num

print(resultado)
"""


