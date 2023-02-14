def f():
    return 1, 2, 3


# si tenemos diferentes elementos, podemos asignarlos a diferentes variables
a, b, c, = f()
print(a, b, c)  # 1 2 3

juntos = f()
print(type(juntos))  # <class 'tuple'>

x, y, z = juntos  # unpack_desempaqueta
print(x, y, z)  # 1 2 3

# ValueError: Too many values to unpack (expected 2)
# x, y = juntos

# ValueError: Need more values to unpack (expected 5, got 3)
# x, y, z, w1, w2 = juntos

mi_tupla = (5, 6, 7)  # Crea una tupla
x, y, z = juntos
