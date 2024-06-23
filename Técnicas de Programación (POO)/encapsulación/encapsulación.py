class CuentaBancaria:
    def __init__(self, titular, balance_inicial):
        self.titular = titular
        self.__balance = balance_inicial  # Atributo privado

    # Método público para depositar dinero
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__balance += cantidad
            print(f"Depositados {cantidad}$. Nuevo balance: {self.__balance}$.")
        else:
            print("La cantidad a depositar debe ser positiva.")

    # Método público para retirar dinero
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__balance:
            self.__balance -= cantidad
            print(f"Retirados {cantidad}$. Nuevo balance: {self.__balance}$.")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    # Método público para consultar el balance
    def obtener_balance(self):
        print(f"El balance actual es: {self.__balance}$.")
        return self.__balance

# Uso de la clase CuentaBancaria
cuenta = CuentaBancaria("Juan Pérez", 1000)
cuenta.depositar(500)
cuenta.retirar(200)
cuenta.obtener_balance()

# Intentar acceder al atributo privado fuera de la clase (causará un error)
# print(cuenta.__balance)






