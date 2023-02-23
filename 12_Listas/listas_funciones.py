

# .split() retorna una LISTA DE STRINGS,
mi_lista = input('Ingresa contenido: ').split()

for item in mi_lista:
    print(item, end=' ')
print(mi_lista)

# LISTA DE ENTEROS
mi_lista = list(map(int, input('ingresa contenido:').split()))

print(type(mi_lista), type(mi_lista[0]))  # ist, int

for item in mi_lista:
    print(item, end=' ')
print()

# muy útil para leer números variables de elementos en la misma línea



