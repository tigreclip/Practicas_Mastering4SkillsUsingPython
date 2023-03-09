################### MÉTODO SPLIT ###################

# POR DEFECTO SPLIT USA LOS ESPACIOS, pero no tiene en cuenta TABULADOR \t NI RETURN \n
print('\n\n\tOye miguel'.split()) 
# ['Oye', 'miguel']

print(' Soy una patata,tubérculo,papa'.split()) # por defecto, separa por espacios NO LOS ITENE EN CUENTA
#['Soy', 'una', 'patata,tubérculo,papa']

print(' Soy una patata,tubérculo,papa'.split(',')) # usando 'coma' para separar
#[' Soy una patata', 'tubérculo', 'papa']

print(' Soy una patata,tubérculo,papa'.split('a')) # usando 'a' para separar
# [' Soy un', ' p', 't', 't', ',tubérculo,p', 'p', '']

print('\n\n\tOye miguel'.split(' ')) # usado espacio, PARTIRÁ EL STRING USANDO TODOS LOS ESPACIOS
# ['\n\n\tOye', 'miguel']

print('1,,,2'.split(',')) # cuando hay más de 1 coma, la primera se usa como separador y el resto como str
# ['1', '', '', '2']

# USO MÁS COMÚN DE SPLIT
item = input().split()
print(item)

# input: alhambra de Granada  
# output:['alhambra', 'de', 'Granada']


