"""
Leer un número entero N y testear N veces
.-Leer N números ( uno por línea!)
.-Para cada numero N:
    Imprimir la suma desde 1 hasta N
Recuerda, podemos reemplazar la suma con la fórmula N*(N+1)/2


N = int(input())

# iterar N veces en N casos
while N > 0:
    num = int(input())
    
    suma = 0
    start = 1

    #Loop anidado: suma desde 1 hasta num
    while start <= num:
        suma += start
        start += 1
    N -= 1
    print(f"suma desde 1 hasta {num} = {suma}")

"""

######## IMPRIMIR TRIÁNGULO INCLINADO A LA IZQUIERDA #####
"""
Dado un número N, imprimir un triángulo inclinado a la izquierda con N filas
- ver la imagen por IO(cmd)
"""
num = int(input()) #ingresar un número
fila = 1 # fila mínima es 1

#(este bucle comprueba que filas y número sean iguales)
while fila <= num: # mientras que fila sea menor o igual a num
    contador = 1   # el contador empieza en 1
                            #(este bucle se repite la impresion)
    while contador <= fila: # Mientras que contador sea menor o igual a fila:
        print('*', end='')  #   -Imprimir '*' con final en blanco y nueva fila
        contador += 1       #   -Incrementar contador  1 unidad
        fila += 1           #   -Incremar fila 1 unidad

