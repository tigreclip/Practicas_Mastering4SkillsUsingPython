# Leer un entero
num = int(input("Ingresa un número: "))

# si num < 10000, imprimir "Es un número pequeño"
if num < 10000:
    print("Es un número pequeño.")

# de lo contrario sumar los tres últimos dígitos:
else:
    digito1 = num % 10 # optención del último dígito
    num = num // 10 # ELIMINA EL ÚLTIMO DIGITO
    digito2 = num % 10
    num = num // 10
    digito3 = num % 10

    #suma de los tres últimos difitos 
    suma =  digito1 + digito2 + digito3

    #si la suma es impar, imprimir "Este es un gran número"
    if suma % 2 != 0:
        print('Este es un gran número.')
    # Si cualquier dígito de los tres últimos es impar, imprimir "Este es un gran número"
    # de lo contrario, imprimir "Este es un mal número"
    else:
        digito1_impar = digito1 % 2 != 0
        digito2_impar = digito2 % 2 != 0
        digito3_impar = digito3 % 2 != 0

        if digito1_impar or digito2_impar or digito3_impar:
            print('Este es un gran número.')
        else:
            print('Este es un mal número.')

#testeado con :  
# 100
# 10111
# 10330
# 10303
# 10033
# 10000
