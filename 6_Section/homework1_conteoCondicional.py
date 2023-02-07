# EScribe un programa que lea el numero X, depués otros 5 números. 
x, n1, n2, n3, n4, n5 = map(int, input('Ingresa seis números separados por un espacion: ').split())
contador = 0
# Cuantos numeros son <= x
contador += n1 <= x #booleano, si (n1 <= x) entonces sumar/añadir a contador n1
contador += n2 <= x #booleano, si (n2 <= x) entonces sumar/añadir a contador n2
contador += n3 <= x #booleano, si (n3 <= x) entonces sumar/añadir a contador n3
contador += n4 <= x #booleano, si (n4 <= x) entonces sumar/añadir a contador n4
contador += n5 <= x #booleano, si (n5 <= x) entonces sumar/añadir a contador n5

# Cuantos numeros son > x
print(contador, 5 - contador)# print(contador) indica los numeros < x, print(5 - contador) indica los numeros > x

# ¿Alguna relación entre esas dos respuestas? 
# R: se complementan

# Inputs:
# 10 --> (300, 1, 5, 100, 200)
# OUTPUT --> 2, 3
# Explicación
# Dos numeros (1, 5) son <=10
# Tres números (100, 200, 300) son >10