

class Rectangulo:  # Class: plantilla con la que crear objetos
    # Constructor
    def __init__(self, ancho, alto):  # Parámetros
        self.ancho = ancho  # ATRIBUTO
        self.alto = alto  # ATRIBUTO

    def area_rectangulo(self):  # MÉTODO: Función definida dentro de una clase
        return self.ancho * self.alto  # Área rectángulo = base * altura


class Circulo:
    # Constructor
    def __init__(self, radio):  # Parámetros
        self.radio = radio  # ATRIBUTO

    def area_circulo(self):  # MÉTODO: Función definida dentro de una clase
        return 3.14 * self.radio * self.radio  # Área círculo = π * r² (pi = 3.14)


r = Rectangulo(2, 5)  # OBJETO
print(r.area_rectangulo())  # 5 Método accesible usando el punto(.)

c = Circulo(5)  # OBJETO, INSTANCIA DE CLASE
print(c.area_circulo())  # 78.5 Método accesible usando el punto(.)


