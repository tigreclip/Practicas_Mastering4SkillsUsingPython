# Optener 3 enteros,
num1, num2, num3 = map(int,(input("Ingresa tres números enteros separados por un espacio: ").split()))
# Ordenarlos en ascendentemente
if num2 < num1: # Intercambio de valores  si num2 menor que num1
    num1, num2 = num2, num1
if num3 < num2: # Intercambio de valores  si num3 menor que num2
    num2 , num3 = num3, num2
if num2 < num1: # el valor de num2 PUEDE HABER CAMBIADO, asi que SE INTERCAMBIA OTRA VEZ con num1
    num1, num2 = num2, num1


# Imprimirlos
print(num1, num2, num3)

# inputs --> output
# 1 2 3 = 1 2 3
# 1 3 2 = 1 2 3
# 2 1 3 = 1 2 3
# 2 3 1 = 1 2 3
# 3 1 2 = 1 2 3
# 3 2 1 = 1 2 3