###### CALCULADORA ESPECIAL #######

"""
Diseñar un pequeña app que continue preguntado 3 opciones:
    -Ingrese 1 para sumar enteros desde 1 hasta N
    -Ingrese 2 para evaluar 2 expresiones numéricas(p.e. 2+3)
    -Ingrese 3 para finalizar la app

-El usuario debe ingresar valores desde 1 hasta 3_
    .si no, informar que es invalida la entrada e intentar de nuevo
-Tomar la entrada adecuada del usuario y devolver respuesta
"""
# Diseñar un pequeña app que continue preguntado 3 opciones:
while True:
    print('\n\nMenu:')
    print('Elige 1 para sumar numeros desde 1 hasta N.')
    print('Elige 2 para evaluar un expresión simple con dos números(p.e. 2 + 3).')
    print('Elige 3 para finalizar el programa.')

#     -Ingrese 1 para sumar enteres desde 1 hasta N
#     -Ingrese 2 para evaluar 2 expresions numéricas(p.e. 2+3)
#     -Ingrese 3 para finalizar la app
    user_inp = input('\nIngresa la elección desde 1 hasta 3:')

# -El usuario debe ingresar valores desde 1 hasta 3_
#     .si no, informar que es invalida la entrada e intentar de nuevo
    if user_inp != '1' and user_inp != '2' and user_inp != '3':
        print("*********************************************************")
        print('Selección incorrecta...Inténtalo otra vez.')
# -Tomar la entrada adecuada del usuario y devolver respuesta
    if user_inp == '1':
        print("*********************************************************")
        n = int(input("Ingrese el número final de la suma: "))
        suma = n * (n + 1) // 2 # suma los números consecutivamente
        print("*********************************************************")
        print(f"El resultado de sumar desde 1 hasta {n} es {suma}")

    elif user_inp == '2':
        print("*********************************************************")
        num1, operacion, num2 = input('Ingresa una operación matemática simple,\nNOTA:dejar espacio entre elementos (p.e. 5 + 2) ').split()
        num1,num2 = float(num1), float(num2)

        resultado = None # None es un valor que significa "nada asignado"

        if operacion == '+':
            resultado = num1 + num2
        elif operacion == '-':
            resultado = num1 - num2
        elif operacion == '*':
            resultado = num1 * num2
        elif operacion == '**':
            resultado = num1 ** num2
        else:
            if num2 == 0:
                print("*********************************************************")
                print("No es posible dividir entre 0")
                print("*********************************************************")
            elif operacion == '/':
                resultado = num1 / num2
            else:
                resultado = num1 // num2
        
        if resultado != None:
            print("*********************************************************")
            print(f"El resultado de {num1} {operacion} {num2} es {resultado}")
            print("*********************************************************")
    else:
        break