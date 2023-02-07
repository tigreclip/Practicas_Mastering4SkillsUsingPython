"""
Lee un entero X
Imprimir todos los números divisibles entre 3 desde 1 a X 
    - 3, 6, 9, 12, 15, 18,...(múltiplos de 3)
Ver ejemplo para entrada 12
"""

# Lee un entero X
end = int(input("Ingresa un número: "))
# Imprimir todos los números divisibles entre 3 desde 1 a X 
start = 1
while start <= end:
    if start % 3 == 0:
        print(start)
    start += 1
#     - 3, 6, 9, 12, 15, 18,...(múltiplos de 3)

#input / output
#  12 -> 3, 6, 9, 12