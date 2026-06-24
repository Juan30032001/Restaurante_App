from Modelos.productos import Producto
from Modelos.cliente import Cliente

class Restaurante:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def mostrar_productos(self):
        print(f"\n=== MENÚ: {self.nombre.upper()} ===")
        if not self.productos:
            print("No hay productos registrados.")
            return
        for p in self.productos:
            print(p)

    def mostrar_clientes(self):
        print(f"\n=== CLIENTES REGISTRADOS ===")
        if not self.clientes:
            print("No hay clientes registrados.")
            return
        for c in self.clientes:
            print(c)