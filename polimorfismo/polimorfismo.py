class Forma:
    def area(self):
        pass  # Método que será implementado en las clases derivadas

# Clase derivada
class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14159 * (self.radio ** 2)

# Clase derivada
class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

# Función que usa polimorfismo
def imprimir_area(forma):
    print(f"El área de la forma es: {forma.area()}")

# Uso de las clases y polimorfismo
formas = [Circulo(5), Rectangulo(3, 4), Circulo(2)]

for forma in formas:
    imprimir_area(forma)