# Este programa calcula el área de un círculo.
# El usuario proporciona el radio como entrada.

import math

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    :param radio: Radio del círculo (float)
    :return: Área del círculo (float)
    """
    area = math.pi * radio ** 2
    return area

def main():
    try:
        radio = float(input("Ingresa el radio del círculo: "))
        area_circulo = calcular_area_circulo(radio)
        print(f"El área del círculo con radio {radio} es {area_circulo:.2f}")
    except ValueError:
        print("Error: Ingresa un valor numérico válido para el radio.")

if __name__ == "__main__":
    main()
