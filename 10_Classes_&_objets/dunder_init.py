class Empleado:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


emp1 = Empleado('Bartolomé', 33)
# Si intentamos imprimir un objeto, el resultado es una impresión inesperada(p.ej. memoria)
print(emp1)  # dirección en memoria <__main__.Empleado object at 0x000001804A08FE10>
s = str(emp1)

# __init__ es un método especial (EN ->Dunder= "Double Under (Underscores)".)
# Se llama de manera implícita para crear un nuevo objeto

# Si intentamos imprimir un objeto, el resultado es una impresión inesperada(p.ej. memoria)

# Python busca la función __str__: SI ESTÁ, será usada para representar al objeto
# Si NO ESTÁ, buscará __repr__ y la usará
# SI NO ESTÁ, usará alguna manera por defecto(p. ej. dirección de memoria

# print(objeto) o str(objeto) intentará seguir IMPLÍCITAMENTE el proceso de arriba
# en ese caso, la función usada DEBE retornar string (cadena de texto)

# Podemos retornar cualquier cosa, pero esto será inútil para uso práctico apropiado
