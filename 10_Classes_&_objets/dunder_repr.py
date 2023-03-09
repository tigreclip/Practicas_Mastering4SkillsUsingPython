class Empleado:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return f'El empleado {self.nombre} tiene {str(self.edad)} años **'  # ATENCIÓN, edad-> convertir INT --> STR


emp1 = Empleado('Bartolomé', 33)

print(emp1)  # El empleado Bartolomé tiene 33 años **

# Si  __str__ no está disponible, __repr__
# entonces se usa __repr__
print(str(emp1))
print(repr(emp1))