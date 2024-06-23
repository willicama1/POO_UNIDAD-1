class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        pass  # Este método será sobrescrito en las clases derivadas

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

# Clase derivada
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Llama al constructor de la clase base
        self.raza = raza

    def hacer_sonido(self):
        print("Guau!")

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Raza: {self.raza}")

# Clase derivada
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)  # Llama al constructor de la clase base
        self.color = color

    def hacer_sonido(self):
        print("Miau!")

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Color: {self.color}")

# Uso de las clases
perro = Perro("Max", 5, "Labrador")
gato = Gato("Luna", 3, "Negro")

perro.mostrar_informacion()
perro.hacer_sonido()

gato.mostrar_informacion()
gato.hacer_sonido()