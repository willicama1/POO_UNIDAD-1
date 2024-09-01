class Producto:
    def __init__(self, producto_id, nombre, cantidad, precio):
        self.producto_id = producto_id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.producto_id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def get_id(self):
        return self.producto_id

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_cantidad(self):
        return self.cantidad

    def set_precio(self, precio):
        self.precio = precio

    def get_precio(self):
        return self.precio
import json

class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        self.productos[producto.get_id()] = producto

    def eliminar_producto(self, producto_id):
        if producto_id in self.productos:
            del self.productos[producto_id]
        else:
            print(f"Producto con ID {producto_id} no encontrado.")

    def actualizar_producto(self, producto_id, nombre=None, cantidad=None, precio=None):
        if producto_id in self.productos:
            producto = self.productos[producto_id]
            if nombre is not None:
                producto.set_nombre(nombre)
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
        else:
            print(f"Producto con ID {producto_id} no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [producto for producto in self.productos.values() if producto.get_nombre() == nombre]
        return resultados

    def mostrar_productos(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_inventario(self, archivo):
        with open(archivo, 'w') as f:
            inventario_dict = {pid: vars(p) for pid, p in self.productos.items()}
            json.dump(inventario_dict, f, indent=4)

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'r') as f:
                inventario_dict = json.load(f)
                self.productos = {}
                for pid, datos in inventario_dict.items():
                    producto = Producto(datos['producto_id'], datos['nombre'], datos['cantidad'], datos['precio'])
                    self.productos[pid] = producto
        except FileNotFoundError:
            print("Archivo no encontrado.")

import json

class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        self.productos[producto.get_id()] = producto

    def eliminar_producto(self, producto_id):
        if producto_id in self.productos:
            del self.productos[producto_id]
        else:
            print(f"Producto con ID {producto_id} no encontrado.")

    def actualizar_producto(self, producto_id, nombre=None, cantidad=None, precio=None):
        if producto_id in self.productos:
            producto = self.productos[producto_id]
            if nombre is not None:
                producto.set_nombre(nombre)
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
        else:
            print(f"Producto con ID {producto_id} no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [producto for producto in self.productos.values() if producto.get_nombre() == nombre]
        return resultados

    def mostrar_productos(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_inventario(self, archivo):
        with open(archivo, 'w') as f:
            inventario_dict = {pid: vars(p) for pid, p in self.productos.items()}
            json.dump(inventario_dict, f, indent=4)

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'r') as f:
                inventario_dict = json.load(f)
                self.productos = {}
                for pid, datos in inventario_dict.items():
                    producto = Producto(datos['producto_id'], datos['nombre'], datos['cantidad'], datos['precio'])
                    self.productos[pid] = producto
        except FileNotFoundError:
            print("Archivo no encontrado.")
