# Secuencia de Fibonacci
# Cada número es la suma de los dos anteriores
# p.e. 13 = 5 + 8
# ESCRIBIR FUNCIÓN: n_fib(num)
#   - Retorna el término n
#   *simple loop
def n_fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    a, b = 0, 1
    n -= 2
    while n > 0:
        c = a + b
        a = b
        b = c
        n -= 1
    return c


for i in range(1, 10):
    print((i, n_fib(i)))
