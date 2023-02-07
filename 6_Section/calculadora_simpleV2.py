# dos numeros y un signo entre ellos indica suma,resta, divide con coma o multiplica. Hallar el valor de la respuesta
# simbolos + - * /
# zeroDivisionError: imprimir NA -->No Answer

num1, operation, num2 = input().split() # crea las tres variables de una vez
num1,num2 = float(num1), float(num2)

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
else:
    if num2 > 0:
        print(num1 / num2)
    else:
        print("NA_No Answer")

