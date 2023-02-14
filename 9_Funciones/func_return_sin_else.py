def minimo(primero, segundo):
    if primero < segundo:
        return primero
    else:
        return segundo  # Cuando la función encuentra RETURN, TERMINA LA FUNCIÓN.


def maximo(primero, segundo):
    if primero > segundo:
        return primero  # RETURN TERMINA LA FUNCIÓN
    return segundo  # Se ejecuta este RETURN SIN NECESIDAD DE "else:"


a, b = 5, 20
print(minimo(a, b))  # 5
print(maximo(a, b))  # 20
