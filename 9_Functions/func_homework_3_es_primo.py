# Implementar 2 funciones:
#    - is_prime():
#        Retornar True si número es primo (divisible por si mismo y por 1)
#    - n_prime(n):
#        Retornar n numeros primo(usar funcion is_prime
#        p.e. n_prime(6) --> 13
#        números primos son: 2, 3, 5, 7, 11, 13, 17, 19

def is_prime(n):
    if n <= 1:  # si no es 1, no es primo
        return False
    for i in range(2, n):
        if n % i == 0:  # 0 indica que NO es primo
            return False
        return True  # equivale a "else: return True" sin necesidad de indicarlo


# print(is_prime(3))


def n_prime(n):  # test -> n=5
    start = 2  # 1ºvuelta: contador empieza desde 2 / 2ºvuelta: start=3/ 3ºvuelta: start=4 / 4ºvuelta: start= 5.....
    while n > 0:  # 1ºvuelta: 5>0 / 2ºvuelta: 5>0 / 3ºvuelta: 4>0
        if is_prime(start):  # 1ºvuelta: 2 NO es primo: asi que no se cumple / 2ºvuelta: 3 SI es primo / 3ºvuelta: 4 NO es primo
            n -= 1  # 1ºvuelta: NO SE CUMPLE / 2ºvuelta: n-1 / 3ºvuelta: NO SE CUMPLE
            if n == 0:  # 1ºvuelta: 4 != 0 / 2ºvuelta n= 4 !== 0
                return start  # 1ºvuelta: retorna 2
        start += 1  # 1ºvuelta: suma 1 a start / 2ºvuelta suma 1 a start
    return -1


# print(n_prime(20))

for i in range(1, 10):
    print(i, n_prime(i))
