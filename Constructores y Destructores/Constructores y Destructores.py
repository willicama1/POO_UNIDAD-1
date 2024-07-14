class Archivo:
    def __init__(self, nombre):
        """
        Constructor de la clase Archivo.

        Args:
        nombre (str): El nombre del archivo que se va a manejar.
        """
        self.nombre = nombre
        print(f'Se ha creado el archivo {self.nombre}.')

    def escribir(self, contenido):
        """
        Simula la escritura de contenido en el archivo.

        Args:
        contenido (str): El contenido que se va a escribir en el archivo.
        """
        print(f'Escribiendo en el archivo {self.nombre}: {contenido}')

    def __del__(self):
        """
        Destructor de la clase Archivo.

        Se ejecuta automáticamente cuando el objeto es destruido.
        Aquí se simularía el cierre del archivo o la liberación de recursos.
        """
        print(f'Se está cerrando el archivo {self.nombre}.')
        # Aquí se cerraría el archivo en un caso real


# Ejemplo de uso de la clase Archivo
if __name__ == "__main__":
    # Creamos un objeto de la clase Archivo
    archivo = Archivo('mi_archivo.txt')

    # Simulamos escribir en el archivo
    archivo.escribir('Hola, este es el contenido del archivo.')

    # Al finalizar el bloque, el objeto archivo será destruido automáticamente
