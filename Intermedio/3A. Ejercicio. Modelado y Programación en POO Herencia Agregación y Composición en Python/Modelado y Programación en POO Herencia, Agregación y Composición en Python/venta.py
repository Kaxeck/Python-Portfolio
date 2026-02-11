# Se importan las clases necesarias
from producto import Producto
from cliente import Cliente
# Clase Venta
class Venta:
    # Inicializador
    def __init__(self, cliente: Cliente):
        self.cliente = cliente
        self.productos: list[Producto] = []
    # Método para agregar productos a la venta
    def agregar_producto(self, producto: Producto) -> None:
        self.productos.append(producto)
    # Método para calcular el total de la venta
    def total(self) -> float:
        return sum(p.precio for p in self.productos)