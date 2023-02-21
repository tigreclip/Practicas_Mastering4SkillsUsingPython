lst = [7, 8, 9, 'holi']

# INVERTIR ORDEN: estilo C++/Java
for pos in range(len(lst)):
    print(lst[len(lst) - pos - 1], end=' ')  # holi 9 8 7
print()

# INVERTIR ORDEN: estilo Python: range(start,end, step)
for idx in range(len(lst) - 1, -1, -1):
    print(lst[idx], end=' ')  # holi 9 8 7
print()

# MEJOR FORMA DE INVERTIR ORDEN:  con REVERSED y ENUMERATE
for item in reversed(lst):  # NO SE CREA COPIA
    print(item, end=' ')
print()

for pos, item in reversed(list(enumerate(lst))):
    print(pos, item, end=' ')
    # 3 holi 2 9 1 8 0 7
    # cuidado:
    # list(iterable) --> crea una copia: más memoria/lentitud

