class Libro:
    def __init__(self, titulo, autor, ISBN):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        else:
            return False

    def devolver(self):
        self.disponible = True

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.ISBN}")
        print(f"Disponibilidad: {'Disponible' si self.disponible else 'No disponible'}")

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        for libro in self.libros:
            libro.mostrar_informacion()
            print("---")

    def prestar_libro(self, ISBN):
        for libro in self.libros:
            if libro.ISBN == ISBN:
                if libro.prestar():
                    print(f"El libro {libro.titulo} ha sido prestado.")
                else:
                    print(f"El libro {libro.titulo} no está disponible.")
                return
        print("El libro no se encontró en la biblioteca.")

    def devolver_libro(self, ISBN):
        for libro in self.libros:
            if libro.ISBN == ISBN:
                libro.devolver()
                print(f"El libro {libro.titulo} ha sido devuelto.")
                return
        print("El libro no se encontró en la biblioteca.")

# Uso del sistema de gestión de biblioteca
biblioteca = Biblioteca()

libro1 = Libro("El Quijote", "Miguel de Cervantes", "1234567890")
libro2 = Libro("1984", "George Orwell", "0987654321")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

biblioteca.mostrar_libros()

biblioteca.prestar_libro("1234567890")
biblioteca.mostrar_libros()

biblioteca.devolver_libro("1234567890")
biblioteca.mostrar_libros()