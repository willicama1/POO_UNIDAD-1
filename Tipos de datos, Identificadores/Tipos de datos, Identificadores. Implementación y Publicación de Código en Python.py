def calcular_pendiente_superficie(funcion, punto):
    """
    Calcula las pendientes en las direcciones X e Y de una superficie definida por una función
    en un punto específico.

    Parámetros:
        funcion (function): Función que define la superficie f(x, y).
        punto (tuple): Tupla que representa el punto (x, y) en la superficie.

    Retorna:
        tuple: Tupla que contiene las pendientes en las direcciones X e Y.
    """

    x, y = punto

    # Derivadas parciales con respecto a x e y
    df_dx = partial(funcion, dx=1, dy=0)
    df_dy = partial(funcion, dx=0, dy=1)

    # Evaluación de las derivadas parciales en el punto
    pendiente_x = df_dx(x, y)
    pendiente_y = df_dy(x, y)

    return pendiente_x, pendiente_y


def main():
    """
    Programa principal que calcula las pendientes en las direcciones X e Y de una superficie
    parabólica en un punto específico.
    """

    # Función que define la superficie parabólica f(x, y)
    def funcion_superficie(x, y):
        return 4 - x**2 - y**2

    # Punto en la superficie
    punto = (1, 1)  # P(1, 1, 2)

    # Cálculo de las pendientes
    pendiente_x, pendiente_y = calcular_pendiente_superficie(funcion_superficie, punto)

    # Impresión de los resultados
    print(f"Pendiente en dirección X: {pendiente_x}")
    print(f"Pendiente en dirección Y: {pendiente_y}")


if __name__ == "__main__":
    main()
