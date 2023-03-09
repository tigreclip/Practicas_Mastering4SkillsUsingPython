
# ALL(iterable): RETORNA True SI TODOS los elementos son True
###################################################
lst = [10, 10, -12, 'Miguel']

print(all(lst)) # True
print(all([]))  # True

# Elementos causantes de False:
print(all([False]))  # False, False siempre da False
print(all(['']))  # False, lista vacía
print(all([0]))  # False, 0 es Falso y 1 es True

print(all([10, 0, 2]))  # False, hay un 0
"""
equivalente a:
def all(iterable):
    for element in iterable:
        if not element:
            return False
        return True
"""

# ANY(iterable): RETORNA True SI 1 ELEMENTO es true
###################################################
# ¿Cómo retornar True si cualquier elemento del iterable es True?
lst = [10, 20, 0, 'Miguel']

print(all(lst))  # False, ALL EXIGE QUE TODOS los elementos sean True
print(any(lst))  # True, ANY SOLO NECESITA UN ELEMENTO True para retornar True
"""
equivalente a:
def any(iterable):
    for element in iterable:
        if element:
            return True
        return False
"""