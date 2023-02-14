# Desarrolla una función: def multiplicación_especial(string):
# Devuelve un string donde cada carácter es repetido acorde a su posición

#  Input: abcxf
#  Output: abbcccxxxxfffff
#  Observaciones:
#       -a se repite una vez
#       -b se repite dos veces
#       -c se repite tres veces
#       -x se repite cuatro veces
#       ... y así con el resto


def special_multiplicacion(string):
    resultado = ''  # se guarda los strings generados
    # bucle for en dos elementos a la vez
    for index, caracter in enumerate(string): # se crean dos variables y se les asignan los valores provenientes de ENUMERATE(index = índice, caracter= item)
        resultado += caracter * (index + 1)  # se añade a RESULTADO -->(caracter * (index + 1)el índice empieza en 0
    return resultado


print(special_multiplicacion('abcxf'))  # output:abbcccxxxxfffff

