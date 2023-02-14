# Funciones sin retorno

def mi_print(primero, segundo):
    print('Suma = ', primero + segundo)
    print('Multiplicación = ', primero * segundo)


res = mi_print(1, 3)  # no da error, pero devuelve "None"
print(res)  # None
