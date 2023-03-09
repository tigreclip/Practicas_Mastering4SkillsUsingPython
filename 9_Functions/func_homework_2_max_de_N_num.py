# Máximo de 6 números: Desarrolla las cuatro funciones para ayudar a calcular el máximo de 6 números
# Cada función debería ser SOLO UNA LINEA DE CÓDIGO
def my_max2(a, b):
    if a > b:
        return a
    return b


def my_max3(a, b, c):
    return my_max2(a, my_max2(b, c))  # se usa  "my_max2" dos veces, para calcular el max de esos pares


def my_max4(a, b, c, d):
    return  my_max2(a,my_max3(b, c, d))  # se usa"my_max3" y "my_max2 para calcular el max de dos


def my_max5(a, b, c, d, e):  # se usa "my_max4" para calcular el max de 4 y "my_max2" para calcular el max de dos
    return my_max2(a, my_max4(b, c, d, e))


def my_max6(a, b, c, d, e, f):
    return my_max2(a,my_max5(b, c, d, e, f))  # se usa "my_max5" para calcular el max de 5 y "my_max2" para calcular el max de dos



