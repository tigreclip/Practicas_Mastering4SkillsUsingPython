
# Sumar 1 + 2 + 3 + 4 + 5
x = 1
sum = 0

while x <= 5:
    sum += x # suma 1+2+3+4+5 = 15
    x = x + 1 # suma ((((1+1)+1 )+1) +1) = 5

print(sum) # 15

# Sumar 5 + 4 + 3 + 2 + 1

x = 5
sum = 0

while x >= 0:
    sum += x # suma 5, 4, 3, 2, 1
    x -= 1 # resta 5-1, 4-1, 3-1, 2-1, 1-1

print(sum) #15

###### USANDO BREAK ######
"""
# Escribir un programa que SIGA leyendo 2 números e imprima su division en flotante
# Si el 2º número es cero:
#   -imprimir "Bye".
#   -finalizar el programa.
# Podemos usar la palabra BREAK para finalizar el bucle WHILE y continuar depués del bucle.
"""

# Escribir un programa que SIGA leyendo 2 números e imprima su division en flotante
while True:
    x, y = map(float,input("ingresa dos numeros: ").split())
    if y == 0:  #Si el 2º número es cero: ->finalizar el programa.
        print("Y es cero!")
        break # DETIENe el loop. Salta a la linea 39

    print(x / y)
print("Bye") # ->imprime "Bye" 

# input / output
# 5 6 -> 0.8333333333333334
# 6 2 -> 3.0
# 10 2 -> 5.0
# 5 0 -> "Y es cero!" -> "Bye"
#
