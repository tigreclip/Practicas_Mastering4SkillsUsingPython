"""
Leer 3 enteros N, M, SUM.
Encontrar todos los pares que cumplan:
    A+B==SUM donde:
        1 <= A <= N
        1 <= B <= M

"""
N, M, SUM = map(int, input().split())  # crear las tres variables
cnt = 0

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if i + j == SUM:
            cnt += 1
print(cnt)

# input  output
# 200 300 70 = 69
