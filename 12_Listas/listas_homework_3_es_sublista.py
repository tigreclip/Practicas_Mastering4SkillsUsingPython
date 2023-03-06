################## ES SUBLISTA ##################

"""
 Leer un línea de N enteros. La llamaremos lista_1
- Después leer una línea de M enteros. Le llamaremos lista_2
- Imprimir YES si lista_2 es una sublista de lista_1, 
  de lo contrario, imprimir NO
  
     input              --> output
·[1 2 3 4] [1 4]        --> False
·[1 2 3 4] [2 3]        --> True
·[10 -10 20 25 2 7 2 3]  [20 25 25] --> True
·[10 -10 20 25 2 7 2 3]  [20 25 7]  --> False
·
"""

def es_sublista(lista_1, lista_check):
    # comprobar si la lista está vacia o no:
    if len(lista_check) == 0:
        return True
    
    # comprobar que lista_check no es mayor que lista_1
    if len(lista_check) > lista_1:
        return False
    
    # para cada index, generar una sublista y comprobar
    for idx in range(len(lista_1 - len(lista_check) + 1)):
        if lista_check == lista_1[idx: idx - len(lista_check)]:
            return True


if __name__ == '__main__':
    lista_1 = list(map(int,input().split()))
    lista_2 = list(map(int,input().split()))


