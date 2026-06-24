import sys
sys.path.append(".")

from Servicios.restaurante import Restaurante
from Modelos.productos import Producto
from Modelos.cliente import Cliente

def main():
    mi_restaurante = Restaurante("Sabor Casero")

    plato1 = Producto("Bandeja Paisa", "Plato fuerte", 12.50, True)
    plato2 = Producto("Ceviche de Camarón", "Entrada", 9.75, True)
    bebida1 = Producto("Jugo de Maracuyá", "Bebida", 2.80, False)

    mi_restaurante.agregar_producto(plato1)
    mi_restaurante.agregar_producto(plato2)
    mi_restaurante.agregar_producto(bebida1)

    cliente1 = Cliente("María López", "maria@correo.com", "0987654321", True)
    cliente2 = Cliente("Juan Pérez", "juan@correo.com", "0912345678", False)

    mi_restaurante.agregar_cliente(cliente1)
    mi_restaurante.agregar_cliente(cliente2)

    mi_restaurante.mostrar_productos()
    mi_restaurante.mostrar_clientes()

if __name__ == "__main__":
    main()