# REVERSE IN PLACE
# Leer una línea con N enteros
# recuerda: list.reverse()
#   realiza "In situ" la inversion de valores
# Implementaremos nuestra propia función 'reverse' en un estilo iterativo
# def mi_reverse(list)
#   no tiene un retorno

# __name__ es un s
print(__name__)  # __main__  indica que este es máximo nivel para ejecutar código,

# Implementaremos nuestra propia función 'reverse' en un estilo iterativo
def mi_reverse(lst):
    for pos1 in range(len(lst) // 2):  # pos1 es la PRIMERA POSICIÓN 1
        pos2 = len(lst) - pos1 - 1  # pos2 es la ÚLTIMA POSICIÓN
        lst[pos1], lst[pos2] = lst[pos2], lst[pos1]  # intercambio de valores


if __name__ == '__main__':
    lst = list(map(int, input().split())) # Leer una línea con N enteros
    mi_reverse(lst)
    print(lst)
