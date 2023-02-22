# REVERSE IN PLACE
# Leer una línea con N enteros
# recuerda: list.reverse()
#   realiza "In situ" la inversion de valores
# Implementaremos nuestra propia función 'reverse' en un estilo iterativo
# def mi_reverse(list)
#   no tiene un retorno


def mi_reverse(lst):
    for pos1 in range(len(lst) // 2):  # pos1 es la PRIMERA POSICIÓN 1
        pos2 = len(lst) - pos1 - 1  # pos2 es la ÚLTIMA POSICIÓN
        lst[pos1], lst[pos2] = lst[pos2], lst[pos1]  # intercambio de valores


def main():
    """
    input(): ingresa los num,
    split(): separa cada elemento,
    int():convierte cada objeto en entero,
    map(): aplica int() a cada objeto de input().split(),
    list(): crea una lista con todos los objetos de input().split(
    :return: lst invertida
    """
    lst = list(map(int, input().split()))
    mi_reverse(lst)
    print(lst)


main()





