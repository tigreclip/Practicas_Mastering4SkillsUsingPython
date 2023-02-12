"""
Contar cuántos enteros (a, b, c, d) tiene las propiedades:
    1 <= a, b, c, d <= 200
    a+b = c+d
output: 5333400

"""
cnt = 0  # crea contador para saber cuántos enteros son
for a in range(1, 201):  # todos los números "a" entre 1 y 200
    for b in range(1, 201):  # todos los números "b" entre 1 y 200
        for c in range(1, 201):  # todos los números "c" entre 1 y 200
            d = a + b - c  # despejamos d desde(a+b=c+d)
            if 1 <= d <= 200:
                cnt += 1  # suma todos los a+b = c+d

print(cnt)  # muestra los números que cumplen la condición
