
print("Programa de clasificación de número pares e impares")
# Leer un enter
num1 = int(input("Ingrese un número: "))
# Si es par: imprimir el último dígito
es_par = num1 % 2 == 0

#   Si es impar:
if es_par:
    print(num1 % 10) # modulo de num1 divido entre 10, devuelve el útimo digito (sin convertir a string ni despues usar index)

# Si número > 1000, imprimir 2 últimos dígitos
# Si número > 1000 y número < 1000000, imprimir 4 últimos dígitos
# De lo contrario, imprimir su valor negativo
else:
    if num1 > 1000:
        print(num1 % 100)
    elif num1 > 1000000:
        print(num1 % 10000)
    else:
        print(-num1)
