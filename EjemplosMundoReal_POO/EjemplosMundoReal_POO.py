#un ejemplo sencillo en Python que modela un sistema de reservas para una aerolínea:
class Vuelo:
    def __init__(self, numero_vuelo, origen, destino, capacidad):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.capacidad = capacidad
        self.reservas = []

    def reservar_asiento(self, pasajero):
        if len(self.reservas) < self.capacidad:
            self.reservas.append(pasajero)
            print(f"¡Asiento reservado para {pasajero} en el vuelo {self.numero_vuelo}!")
        else:
            print(f"Lo siento, el vuelo {self.numero_vuelo} está lleno.")

    def mostrar_reservas(self):
        print(f"Reservas para el vuelo {self.numero_vuelo}:")
        for pasajero in self.reservas:
            print(f"- {pasajero}")

# Ejemplo de uso
vuelo1 = Vuelo(numero_vuelo="AC123", origen="Seattle", destino="Nueva York", capacidad=100)
vuelo1.reservar_asiento("Alice")
vuelo1.reservar_asiento("Bob")
vuelo1.mostrar_reservas()
