##### NÚMERO DIVISIBLE ENTRE 3 #####
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

##### fUNCIÓN POTENCIA #####
"""
Lee 2 enteros X e Y y calcula X*y(potencia)
    X * X * X... Y veces
    ejemplo: 2 potencia 5 = 2*2*2*2*2
    NOTA: NO USAR X**y
"""
num, potencia = map(int,input().split())
python_resultado = num ** potencia
mi_resultado = 1
while potencia >= 1:
    mi_resultado *= num
    potencia -= 1
print(mi_resultado)

assert python_resultado == mi_resultado, "Comprobar otra vez.." # comprueba que es correcto, en caso contrario lanza un mesaje
