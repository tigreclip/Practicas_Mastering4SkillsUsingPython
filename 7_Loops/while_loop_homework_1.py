
##### HOMEWORK 1  PRINT RANGE #####
""" 
Dado un número inicial  X y un número final Y, imprime todos los
números entre X e Y (inclusive) 


start, end = map(int, input().split())

while start <= end:
    print(start, end=', ')
    start += 1

"""

##### HOMEWORK 2 REPETIR #####
"""
-Leer entero N y string S
-Imprimir S repitiendo N veces
-input: 5 Hi
-output: HiHiHiHiHi
NOTA:  podemos usar string*5:
        -por favor, usar bucle while 

n, s = input().split()
n = int(n)

while n: # mientras sea positivo, el valor de while es True
    print(s, end='')
    n -= 1 # resta 1 a N hasta que llega a 0,  0 == False y el bucle no se ejecuta

###### test ######    
#Input          output
# 5 "Hi"   -->  "HiHiHiHiHi"   
"""


##### HOMEWORK 3 IMPRIMIR TRIÁNGULO INCLINADO, INVERTIDO#####
"""
Leer entero N.
Imprimir un triángulo inclinado invertido que tengas N filas o rows


N = int(input("Introduce un número: "))
filas = N

while filas > 0:
    contador_asterisco = 1
    
    while contador_asterisco <= filas:
        print('*', end='')
        contador_asterisco += 1
    
    print()
    filas -= 1

#input   -   output
# 5           *****
#             ****
#             ***
#             **
#             *

"""


##### HOMEWORK 4 PROMEDIO ESPECIAL #####

"""

-Leer entero N, depués leer N números:
    .cada uno en lineas separadas
-Imprimir 2 valores:
    .el promedio de numeros en posiciones impares(1º, 3º, 5º..)
    .El promedio de numero en posiciones PARES (2º, 4º, 6º)

ejemplos promedio:
    (10+20+30)/3 = 20
    (100+200+600)/3 = 300
"""
pares_suma, impares_suma, pares_contador, impares_contador = 0, 0, 0, 0

n = int(input('Ingresa un numero:'))

cnt = 1
while cnt <= n:
    value = float(input("ingresa otro número: "))

    if cnt % 2 == 0: # posion PAR
        pares_suma += value
        pares_contador += 1
    else:
        impares_suma += value
        impares_contador += 1
    
    cnt += 1

print(impares_suma/impares_contador, pares_suma/pares_contador)



