
# ENUMERATE, asigna un índice a cada elemento
mi_lista = [1, 'Miguel', 4]
for idx, item in enumerate(mi_lista):
    print(idx, item)
    idx = -100  # sin efecto actual
"""
INDICE  ELEMENTO
    0       1
    1       Miguel
    2        4
"""