"""
Class editor tiene dos objetos: rectángulo y círculo
Crear métodos para inicializar esos objetos
Cambiar método, añadir un factor a los datos
  p.ej. si Rectangulo=(3,5)
  factor 2 -> (3+2, 5+2)
Imprimir solo el método imprimir
Ver captura de pantalla
"""


# Class editor tiene dos objetos: rectángulo y círculo
class Rectangulo:  # Class: plantilla con la que crear objetos
    def __init__(self, ancho, alto):  # Constructor, asigna valores a los parámetros
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


class Editor:  # Objeto
    def __init__(self):  # Constructor
        self.rectang = None  # Crea método para inicializar rectángulo SIN CREARLO
        #                      (mas abajo se comprueba este atributo para saber si existe o no el objeto)
        self.circulo = None  # Crea método para inicializar rectángulo SIN CREARLO
        #                      (mas abajo se comprueba este atributo para saber si existe o no el objeto)

    def crear_rectangulo(self, ancho, alto):  # Método
        self.rectang = Rectangulo(ancho, alto)  # Atributo

    def crea_circulo(self, radio):  # Método
        self.circulo = Circulo(radio)

    # Cambiar rectángulo, añadir un factor a los datos
    def cambiar_rectangulo(self, factor):  # Método
        if self.rectang == None:  # Comprueba si rectángulo existe, se debería usar IS None (pronto)
            return
        ancho, alto = self.rectang.ancho + factor, self.rectang.alto + factor
        self.crear_rectangulo(ancho, alto)  # Crea un rectángulo + factor

    # Cambiar circulo , añadir un factor a los datos
    def cambiar_circulo(self, factor):  # Método
        if self.circulo == None:  # Comprueba si círculo existe, se debería usar IS None (pronto)
            return
        self.crea_circulo(self.circulo.radio + factor)  # Crea un circulo + factor

    # Cambiar métodos,
    def cambiar(self, factor):
        self.cambiar_rectangulo(factor)
        self.cambiar_circulo(factor)

    def print(self):  # Método

        if self.rectang != None:  # Comprueba que el rectángulo existe
            print(f'Área del rectángulo: {self.rectang.area_rectangulo()}')  # imprime, en caso positivo

        if \
                self.circulo != None:  # Comprueba que el círculo existe
            print(f'Área del círculo: {self.circulo.area_circulo()}')  # imprime, en caso positivo


editor = Editor() # Instancia de Editor
editor.crear_rectangulo(3, 5)  # Método para crear rectángulo
editor.print()  # "Área del rectángulo: 15"

editor.crea_circulo(5) # Método para crear círculo
editor.cambiar_circulo(2) # Método para añadir factor a
editor.print()  # Área del círculo: 153.86

#   p.ej. si Rectangulo=(3,5)
#   factor 2 -> (3+2, 5+2)
# Imprimir solo el método imprimir
# Ver captura de pantalla
