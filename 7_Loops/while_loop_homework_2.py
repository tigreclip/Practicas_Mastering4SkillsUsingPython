###### CALCULADORA ESPECIAL #######

"""
Diseñar un pequeña app que continue preguntado 3 opciones:
    -Ingrese 1 para sumar enteres desde 1 hasta N
    -Ingrese 2 para evaluar 2 expresions numéricas(p.e. 2+3)
    -Ingrese 3 para finalizar la app

-El usuario debe ingresar valores desde 1 hasta 3_
    .si no, informar que es invalida la entrada e intentar de nuevo
-Tomar la entrada adecuada del usuario y devolver respuesta
"""

sumar, evaluar, finalizar = 1, 2, 3
print("-->Ingrese 1 para sumar enteros desde 1 hasta N\n-->Ingrese 2 para evaluar 2 expresiones numéricas\n-->Ingrese 3 para finalizar")
opcion = int(input("Elija una opcion e ingrese el numero correspondiente: "))


while opcion >= 1 and opcion <=3:
    if sumar == opcion:
        print(f'Has elegido {sumar} ')
    
    elif evaluar == opcion:
        print(f'Has elegido el nº{evaluar} ')

        num1,num2 = map(int,input("ingresa un número: ").split())
        suma, resta, multiplicacion, division = '+', '-', '*','/'
        print("Elige el tipo operacion a realizar con los números: \nSUMA + \nRESTA - \nMULTIPLICACIÓN * \nDIVISION /")
        operacion = input("Qué operacion deseas realizar?")
        if operacion == suma:
            print(num1 + num2)
        elif operacion == resta:
            print(num1 - num2)
        elif operacion == multiplicacion:
            print( num1 * num2)
        else:
            print(num1 / num2)
    elif finalizar == opcion:
        print(f'Has elegido el nº{finalizar} ')
        break
    else:
        print("Opción no disponible")