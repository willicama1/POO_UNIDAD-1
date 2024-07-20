import os


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'POO_UNIDAD-1/Clases, objetos, herencia, encapsulamiento y polimorfismo./Clases, objetos, herencia, encapsulamiento y polimorfismo.py',
        '2': 'POO_UNIDAD-1/Constructores y Destructores/Constructores y Destructores.py',
        '3': 'POO_UNIDAD-1/EjemplosMundoReal_POO/EjemplosMundoReal_POO.py',
        '4': 'POO_UNIDAD-1/Tipos de datos, Identificadores/Tipos de datos, Identificadores. Implementación y Publicación de Código en Python.py',
        '5': 'POO_UNIDAD-1/Técnicas de Programación (POO)/abstracción/abstracción.py',
        '6': 'POO_UNIDAD-1/Técnicas de Programación (POO)/encapsulación/encapsulación.py',
        '7': 'POO_UNIDAD-1/Técnicas de Programación (POO)/herencia/herencia.py',
        '8': 'POO_UNIDAD-1/Técnicas de Programación (POO)/polimorfismo/polimorfismo.py',

        # Agrega aquí el resto
        # de las rutas de los scripts
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()