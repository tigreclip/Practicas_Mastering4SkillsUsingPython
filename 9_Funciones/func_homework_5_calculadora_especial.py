# TODO generar Docstring para cada función

"""
Calculadora Especial con la que es posible:
    ·Sumar enteros desde 1 hasta N
    ·Realizar operaciones matemáticas
"""


def menu():
    """
    Muestra en pantalla las opciones que ofrece la calculadora especial
    :return: opciones: 1) Sumar, 2) Calcular, 3) Finalizar programa
    """
    while True:
        print('\n\nMenu:')
        print('Elige 1 para sumar números desde 1 hasta N.')
        print('Elige 2 para evaluar un expresión simple con dos números(p.e. 2 + 3).')
        print('Elige 3 para finalizar el programa.')

        # -El usuario debe ingresar valores desde 1 hasta 3
        user_inp = input('\nElige una opción de 1 a 3: ')

        #  si no, informar que es inválida la entrada e intentar de nuevo
        if user_inp != '1' and user_inp != '2' and user_inp != '3':
            print('Ingreso inválido... Inténtalo de nuevo: ')
            continue
        else:
            return user_inp


def sum_1_to_n():
    print("*********************************************")
    n = int(input("Ingrese el número final de la suma: "))
    suma = n * (n + 1) // 2  # suma los números consecutivamente
    print("*********************************************")
    print(f"El resultado de sumar desde 1 hasta {n} es {suma}")


def divide(num1, num2, operacion):
    """
    Comprueba que no se usa 0 en la división y el tipo de division(con o sin decimal)
    :param num1: ingresar por teclado el primer número entero, DIVIDENDO
    :param num2: ingresar por teclado el segundo número entero, DIVISOR
    :param operacion: ingresar por teclado el tipo de operación.
    :return:
    """
    if num2 == 0:
        resultado = None  # None es un valor que significa "nada asignado"
    elif operacion == '/':
        resultado = num1 / num2
    else:
        resultado = num1 // num2

    return resultado


def calcular():
    """
    Realiza la operación matemática seleccionada en menu()
    :return: Tipo de operacion a realizar( +, -, *, **, /, //)
    """
    num1, operacion, num2 = input('ingresa el primer número, después el simbolo de la operacion y el segundo número:  (p.ej. "5 + 6" ').split()
    num1, num2 = float(num1), float(num2)

    if operacion == '+':
        resultado = num1 + num2
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '**':
        resultado = num1 ** num2
    else:
        resultado = divide(num1, num2, operacion)

    if resultado != None:
        print(f'El valor de la operacion es {resultado}')
    else:
        print('Disculpa, no es posible realizar el cálculo')


def calculadora_interface():
    while True:
        user_inp = menu()

        if user_inp == '1':
            sum_1_to_n()
        elif user_inp == '2':
            calcular()
        else:
            break


calculadora_interface()
