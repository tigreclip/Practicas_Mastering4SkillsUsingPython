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
    resultado = ''
    for index, caracter in enumerate(string): # enumerate da un index a cada elemento 0:a, 1:b...
        resultado += caracter * (index + 1)
    return resultado


print(special_multiplicacion('abcxf'))

