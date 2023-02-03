# Leer 2 enteros A,B e imprimir según casos:
A, B = map(int,input("ingresa dos numeros separados por un espacio: ").split()) # se crean dos variables de enteros usando MAP para convertir en enteros los INPUTS

# BOOLEAN para saber si es IMPAR
imparA = A % 2 != 0 
imparB = B % 2 != 0

# Si AMBOS son IMPARES, imprimir el PRODUCTO A*B
if imparA and imparB:
    print (A * B)

# Si AMBOS son PARES, imprimir la DIVISION A/B (division decimal / asumimos B!=0)
elif not imparA and not imparB:
    print(A//B)

# Si el PRIMERO es IMPAR y SEGUNDO PAR, hallar la SUMA A+B
elif imparA and not imparB:
    print(A+B)

# Si el PRIMERO es PAR y el SEGUNDO IMPAR, hallar la RESTA A-B
else:
    print(A-B)

# inputs --> output
# 5,7 -> 35
# 12, 2 -> 6
# 5, 6 -> 11
# 12, 3 -> 9
