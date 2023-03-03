"""
Leer un linea de N enteros 
Imprimir el resultado más pequeño posible de A[i] + A[j] + j - i
    ·donde 0 <= i < j <= N-1
Input    --> Output
20 1 9 4  ->  7
"""

def par_mas_pequeño(lst):
    respuesta = None

    for pos1, item1 in enumerate(lst):
        for pos2 in range(pos1+1, len(lst)): # loop par comprobar que i < j 
            item2 = lst[pos2]
        
        actual = item1 + item2 + pos2 - pos1

        if respuesta is None or respuesta > actual:
            respuesta = actual
    
    return respuesta



if __name__ == '__main__':
    lst = list(map(int,input().split()))

    respuesta = par_mas_pequeño(lst)
    print(respuesta)



