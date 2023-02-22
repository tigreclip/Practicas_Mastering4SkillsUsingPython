# COMPARACIÓN
# Mismas reglas que comparar cadenas de texto(strings)
# Compara elemento por elemento
# Si un elemento es pequeño, su lista es pequeña

lst1 = [1, 5, 8]
lst2 = [1, 5, 8]
lst3 = [1, 5]
lst4 = [7, 5]

# PARA COMPARAR VALORES ES MEJOR USAR '=='
# PARA COMPARAR OBJETOS ES MEJOR USAR 'is'
print(lst1 is lst2)  # False, compara objetos y son diferentes elementos en memoria
print(lst1 == lst2)  # True, ya que compara los valores y son los mismos

print(lst1 < lst2)  # False, son iguales
print(lst1 <= lst2)  # True
print(lst1 <= lst3)  # False, lst3 es menor
print(lst1 <= lst4)  # True

# ERROR: NO SE PUEDE COMPARARint(números) y str(letras) , PERAS < MANZANAS = ERROR
print([1, 2] < ['Miguel'])
# TypeError: '<' not supported between instances of 'int' and 'str


