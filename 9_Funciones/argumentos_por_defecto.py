# a, b: argumentos NO por defecto
# c, d: argumentos por defecto
# La función acepta desde 2 hasta 4 argumentos
def my_suma(a, b, c=1, d=2):
    return a + b + c + d


print(my_suma(1, 2, 3, 4))  # 10
print(my_suma(3, 7))  # 13

#  TypeError: my_suma() takes from 2 to 4 positional arguments but 5 were given
# my_suma(1, 2, 3, 4, 5) # se usa mas elementos(5) de los que se necesitan (4)


#  SyntaxError: non-default argument follows default argument
# def my_suma(a = 1, b, c = 1, d = 2): # no puede haber argumento NON-DEFAULT antes de un argumento DEFAULT
#     return a + b + c +d

