# Librería para trabajar con fechas
from datetime import date

# Clase base "Empleado"
class Empleado:
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, sueldo_base):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._fecha_nacimiento = fecha_nacimiento
        self._sueldo_base = sueldo_base

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def get_apellido(self):
        return self._apellido

    def set_apellido(self, nuevo_apellido):
        self._apellido = nuevo_apellido

    def get_dni(self):
        return self._dni

    def get_fecha_nacimiento(self):
        return self._fecha_nacimiento.strftime("%d/%m/%Y")

    def get_sueldo_base(self):
        return self._sueldo_base

    def calcular_bono(self):
        # Implementación base para el cálculo de bono (puede ser más compleja)
        bono = self._sueldo_base * 0.1
        return bono

    def __str__(self):
        return f"Empleado: {self._nombre} {self._apellido} - DNI: {self._dni} - Fecha Nac: {self._fecha_nacimiento.strftime('%d/%m/%Y')} - Sueldo Base: ${self._sueldo_base:.2f}"


# Clase derivada "Gerente"
class Gerente(Empleado):
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, sueldo_base, zona_gerencia):
        super().__init__(nombre, apellido, dni, fecha_nacimiento, sueldo_base)
        self._zona_gerencia = zona_gerencia

    def get_zona_gerencia(self):
        return self._zona_gerencia

    def set_zona_gerencia(self, nueva_zona_gerencia):
        self._zona_gerencia = nueva_zona_gerencia

    # Sobrescritura del método para calcular el bono de gerente
    def calcular_bono(self):
        bono_base = super().calcular_bono()
        bono_adicional = self._sueldo_base * 0.05
        bono_total = bono_base + bono_adicional
        return bono_total

    def __str__(self):
        # Se incluye la información de la zona de gerencia
        return f"{super().__str__()} - Zona Gerencia: {self._zona_gerencia}"


# Creación de instancias y uso de métodos
empleado1 = Empleado("Juan", "Pérez", 12345678, date(1980, 1, 1), 1500)
gerente1 = Gerente("Ana", "López", 87654321, date(1975, 7, 10), 2000, "Zona
