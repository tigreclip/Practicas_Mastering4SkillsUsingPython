""" 
Escribe una funcion que tome una lista y un tipo
    ·retorna el valor minimo entre estos tipos de datos o None si no está presente
    ·P. ej. en la lista [10, 30, 5] son del tipo INT. El mínimo es 5 
"""

def find_smallest(lst, target_type):
    new_lst = [item for item in lst if type(item) is target_type ] # comprehension list

    if len(new_lst) == 0:
        return None
    return min(new_lst)

if __name__ == '__main__':
    lst = [10, -2.5, 20, 5, 'Miguel', 5.2, 'Ruiz']
     
    print(find_smallest(lst, type(0))) # 5
    print(find_smallest(lst, type(0.9))) # -2.5
    print(find_smallest(lst, type(''))) # Miguel