"""
-Leer un entero y contar el nùmero de dígitos.
-Ver la salida en la captura de pantalla.
Nota: una forma es convertir el INT a STRING(no usar -string-)
"""

num = int(input())
num2 = num # bug_1: imprime num como 0 , solucion: crear una copia de num e imprimirla

if num == 0: # bug_2: falla cuando  num =0 , solucion: crear una condición if num == 0:
    digits = 1
else:
    digits = 0

    if num < 0 : # bug_3: falla cuando num es negativo,solucion: crear una condicion If y multiplicar num * -num
        num = -num

    while num > 0:
        digits += 1
        num //= 10 

print(f'El # de dígitos de {num2} es {digits}')


# Hay 3 BUGS en este código
# Encuentra un testeo para cada error
# bug_1: imprime num como 0 , solucion: crear una copia de num e imprimirla
# bug_2: falla cuando  num =0 
# bug_3: falla cuando num es negativo

# inputs / outputs
# -