class Empleado:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):  # PREVISTO PARA CLIENTES / objetivo: legible
        return f'El empleado {self.nombre} tiene {str(self.edad)}'

    def __repr__(self):  # PREVISTO PARA DESARROLLADORES (p. ej. depuración/inicio sesión/objetivos)
        return f"Empleado(nombre='{self.nombre}', edad='{str(self.edad)}')"  # ATENCIÓN, edad-> convertir INT --> STR
        # TOMA NOTA: Es bonito usar los outputs como un objeto de clase en la depuración (debugging) : INCONFUNDIBLE


emp1 = Empleado('Bartolomé', 33)
# Si __str__ está disponible, será usado (
print(str(emp1))  # El empleado Bartolomé tiene 33

print(repr(emp1))  # Empleado(nombre='Bartolomé', edad='33')


######### Por qué usar AMBOS str y repr? #########

# __str__ PREVISTO PARA CLIENTES / objetivo: legible

# __repr__  PREVISTO PARA DESARROLLADORES (p. ej. depuración/inicio sesión/objetivos)
# Si trabajamos en CONSOLA PYTHON esta usará __REPR__, ya que entiende que estamos depurando el código
