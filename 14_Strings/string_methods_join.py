
################ JOIN ################
lst = ['a', 'bb', 'ccc']
print(''.join(lst)) # abbccc

print(','.join(lst)) # a,bb,ccc # EL CASO MÁS COMÚN 

print('#$#'.join(lst)) # a#$#bb#$#ccc

# JOIN toma un iterable: list, string, tuple, dict, set
# UNE TODOS LOS ELEMENTOS de la cadena usada

s1 = 'abc'
s2 = '12345'
print(s1.join(s2)) # 1abc2abc3abc4abc5

print(s2.join(s1)) # a12345b12345c


