class MiRango:
    def __init__(self, start, end, step):  # constructor con parámetros
        self.start = start  # parámetro
        self.end = end  # parámetro
        self.step = step  # parámetro

    def siguiente(self):
        return self.start < self.end

    def usar_siguiente(self):
        retorno = self.start
        self.start += self.step
        return retorno


rng = MiRango(5, 10, 1) # rango de 5-10 con paso de 1

while rng.siguiente():  # mientras siguiente True(hay un siguiente número)
    print(rng.usar_siguiente(), end=' ')  # imprimir usar_siguiente con espacio al final

print()  # imprimir espacio, mejor legibilidad del código

rng = MiRango(5, 10, 2)  # rango de 5-10 con paso de 2
while rng.usar_siguiente():
    print(rng.usar_siguiente(), end=' ')



