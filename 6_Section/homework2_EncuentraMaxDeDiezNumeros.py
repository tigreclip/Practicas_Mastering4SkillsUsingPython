

contador = int(input("Ingrese el primer número: "))#leer el primer número

# Leer un primer número
resultado = float(input("Ingrese el siguiente número: "))
contador = 10

# Leer HASTA 9 veces mas
###### CÓDIGO OPTIMIZADO ######
while contador > 1:
    if contador > 0:
        num = float(input("Ingrese el siguiente número: "))
        contador -= 1
        if num > resultado:
            resultado = num

print(resultado)

###### CÓDIGO EJERCICIO ######            
"""       
if contador > 0:
    num = float(input("Ingrese el siguiente número: "))
    contador -= 1
    if num > resultado:
        resultado = num
        
if contador > 0:
    num = float(input("Ingrese el siguiente número: "))
    contador -= 1
    if num > resultado:
        resultado = num

if contador > 0:
    num = float(input("Ingrese el siguiente número: "))
    contador -= 1
    if num > resultado :
        resultado = num

if contador > 0:
    num = float(input("Ingrese el siguiente número: "))
    contador -= 1
    if num > resultado:
        resultado = num
        
if contador > 0:
    num = float(input("Ingrese el siguiente número: "))
    contador -= 1
    if num > resultado:
        resultado = num

if contador > 0:
    num = float(input("Ingrese el siguiente número: "))
    contador -= 1
    if num > resultado:
        resultado = num

if contador > 0:
    num = float(input("Ingrese el siguiente número: "))
    contador -= 1
    if num > resultado:
        resultado = num

if contador > 0:
    num = float(input("Ingrese el siguiente número: "))
    contador -= 1
    if num > resultado:
        resultado = num

print(resultado)
"""
    




# Inputs(deben estar en lineas separadas)

# 5 ( 1, 3, 2, 4.5, 2) --> 4.5
#   5 indica leer 5 enteros
#   Despues los leemos (1, 3, 2, 4.5, 2).Su máximo es 4.5

# 10 (1, 67, -9, 88, -45, 129, 90, 65, 77, 34) --> 129
#ES IGUAL AL EJERCICIO ANTERIOR, ESTA VEZ LE INDICAMOS PRIMERO N(10)
