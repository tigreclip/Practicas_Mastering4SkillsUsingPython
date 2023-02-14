"""
Contar cuántos números x e Y que:
    x en rango(50-300)
    Y en rango(70-400)
    X<Y
    (X+Y) divisible entre 7

output: 8040

nota: después de resolver, pensar en optimizar el código

cnt = 0
for x in range(50, 301): # por cada X en un rango entre 50 y 300
    for y in range(70-401): #por cada Y en un rango entre 70 y 400
        if x < y and (x + y) % 7 == 0: # si x manor que Y y (x+Y) múltiplo de 7
            cnt += 1 # añadir 1 a contador
print(cnt) # imprimir contador
"""
# Código mejorado:

cnt = 0

for x in range(50, 301):  # por cada X en un rango entre 50 y 300
    start = max(70, x+1)  # el máximo entre 70 y x+1
    for y in range(start, 401):  # por cada Y en un rango entre start y 401
        if (x + y) % 7 == 0:  # si x + y es múltiplo de 7
            cnt += 1
print(cnt)
