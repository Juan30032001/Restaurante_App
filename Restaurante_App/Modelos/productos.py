class Producto:
    def __init__(self, nombre: str, categoria: str, precio: float, disponible: bool):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    def __str__(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"{self.nombre} | Categoría: {self.categoria} | Precio: ${self.precio:.2f} | {estado}"