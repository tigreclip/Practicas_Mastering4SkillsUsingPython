#Dados 3 enteros
a, b, c = map(int,input('Ingresa tres números separados por un espacio: ').split())
# Encotrar el numero mayor de los que son < 100:

######## PRIMER BLOQUE ########
#comprobar que todos los valores son igual o mayores de 100:
if a >=100 and b >=100 and c >=100:
    res = -1 #   imprimir -1 si no existe
else:
    # Encontrar y validar el valor 
    if a < 100:
        res = a
    elif b < 100:
        res = b
    else:
        res = c
######## SEGUNDO BLOQUE ########
# Asegurarse de que el resultado de cada elemento es mejor de lo que hemos asignado previamente
    if res < a < 100:
        res = a
    if res < b < 100:
        res = b
    if res  < c < 100:
        res =  c

print(res)


#inputs --> outputs
#22 90 115 --> 90  #[22 90] son los únicos <100. El mayor (22,90)=90
#200 300 400 --> -1 # todos son >100, sin respuesta
# 50 100 150 --> 50 # solo 50 es < 100
#10 30 20 --> 30 # los tres numeros son <100, asi que el mayor es 30