

# The default type of parameter in python is positional or keyword
# El tipO de parámetro por defecto en python es POSICIONAL o KEYWORD (palabra clave)
def f(a, b, c, d, e = 10):
    print(a, b, c, d, e)

# argumentos posicionales
f(1, 2, 3, 4, 5)                # 1 2 3 4 5

# argumentos keywork, en orden
f(a=1, b=2, c=3, d=4, e=5)      # 1 2 3 4 5

# argumentos keywork, desordenados
f(e=5, b=2, c=3, d=4, a=1)      # 1 2 3 4 5

# 2 argumentos posicionales, 3 arg
# 
# 2 argumentos posicionales, 3 argumentos keyword 
f(1, 2, c=3, d=4, e=5)      # 1 2 3 4 5

# 2 posicionales, 2 argumentos keyword , 1 por defecto (ver la primera funcion, arriba)
f(1, 2, d=4, c=3)           # 1 2 3 4 10

#TypeError: f() got an unexpected keyword argument 'k' (NO EXISTE ´k´ y da error)
#f(1, 2, d=4, k=3)

# TODO los argumentos posicionales vienen DEPUÉs de cualquier argumento keyword
# SyntaxError: positional argument follows keyword argument
#f(d=4, c=3, 1, 2)

