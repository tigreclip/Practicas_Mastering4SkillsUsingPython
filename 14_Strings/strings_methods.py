
################## MÉTODOS DE STRING ##################

print('abcDEF'.lower()) # abcdef: LOWER convierte a minúsculas
print('abcDEF'.upper()) # ABCDEF: UPPER convierte a mayúsculas

print('abc'.islower()) # True, son minúsculas TODOS lo cararteres?
print('ABC'.isupper()) # True, son mayúsculas TODOS lo cararteres?
print('123'.isdecimal()) # True, TODOS LOS CARACTERS SON NÚMEROS entre 0 y 9

print('abcdef'.startswith('abc')) # True
print('abcdef'.startswith('abcD')) # False
print('abcdef'.endswith('def')) # True

print('abcdbcd'.find('bc')) # 1 -> ENCUENTRA EL ÍNDICE MAS BAJO, QUE COINCIDA CON LA BÚSQUEDA
print('abcdbcd'.find('xx')) # -1 -> SI NO EXISTE, DEVUELVE -1 
print('abcdbcd'.rfind('bc')) # 4 -> ENCUENTRA EL ÍNDICE MAS ALTO, QUE COINCIDA CON LA BÚSQUEDA
# print('abcdbcd'.index('xx')) # igual que FIND pero ValueError si no encuentra lo que busca
# ValueError: substring not found

print('HoHoHo'.count('Ho')) # 3 coincidencias para Ho
print('AAAA'.count('AA')) # 2 coincidencias

print(' '.isspace()) # True, hay un espacio
print('\n'.isspace()) # True, Retorno es espacio
print('\t'.isspace()) # True, Tabulador es espacio
print(''.isspace()) # False, No hay espacio, sólo las comilllas

print('\n\tHola    \t'.strip()) # Hola, STRIP ELIMINA TODOS LOS ESPACIOS

print('Hola Jorge? Hola'.replace('Hola', 'Más')) # Más Jorge? Más

print('\nYo tengo   33'.split()) # ['Yo', 'tengo', '33'] SPLIT devuelve cada caracter separado por espacios
print('Oye\n¿Cómo\nEstás ?'.splitlines()) #['Oye', '¿Cómo', 'Estás ?'] SPLITLINES  devuelve lineas enteras

