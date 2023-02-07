# Leer un número X, depués leer 6 enteros s1, e1, s2, e2, s3, e3
#   Esos 6 números son para 3 intervalos
#   Cada intervalo es un "range[start, end]"
#   num X in a range if start <= X <=end
#   ejemplo -> 7 está en "range[5, 12]" pero no en "range[10,20]"
# Imprimir en cuantos intervalos es parte X
# Inputs
#   7 1,10 5,6 4,40 -> 2 .-Numero 7 existe en 2 intervalos [1, 10] y [4, 40]
#   10 5,15 6,100 3,30 -> 3 .-10 existe en 3 intervalos [5, 15], [6,100], [3, 30]
#   10 100,200 100,101 120, 170 -> [No existe en ningún]

# Leer un número X, depués leer 6 enteros s1, e1, s2, e2, s3, e3
X = int(input("Ingresa un número: "))
s1, e1, s2, e2, s3, e3 = map(int, input("Ingresa seis números: ").split())

#   Esos 6 números son para 3 intervalos
#   Cada intervalo es un "range[start, end]"
#   num X in a range if start <= X <=end
contador = 0
contador += s1 <= X <= e1
contador += s2 <= X <= e2
contador += s3 <= X <= e3

# Imprimir en cuantos intervalos es parte X
print(f"El número aparece {contador} veces")
# Inputs
#   7 1,10 5,6 4,40 -> 2 .-Numero 7 existe en 2 intervalos [1, 10] y [4, 40]
#   10 5,15 6,100 3,30 -> 3 .-10 existe en 3 intervalos [5, 15], [6,100], [3, 30]
#   10 100,200 100,101 120, 170 -> [No existe en ningún]