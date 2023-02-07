# Leer 3 numero e imprimir el menor de ellos

#METODO 1
# Crea 3 variables usando .split()
"""
num1, num2, num3 = input("ingresa tres números, en la misma lína, separados por un espacio:").split()

num1, num2, num3 = float(num1), float(num2), float(num3)

if num1<num2 and num1<num3:
    print(num1)
elif num2 < num1 and num2< num3:
    print(num2)
else:
    print(num3)
"""

# Entradas:
# 10.5-20-30 -> 10.5
# 7-5-15 -> 5

#METODO 2

num1, num2, num3 = map(float, input("ingresa tres números, en la misma lína, separados por un espacio:").split())

if num1 < num2:
    if num1 < num3:
        print(num1)
    else:
        print(num3)
else: 
    if num2 < num3:
        if num2 < num1:
            print(num2)
    else:
        print(num3)
