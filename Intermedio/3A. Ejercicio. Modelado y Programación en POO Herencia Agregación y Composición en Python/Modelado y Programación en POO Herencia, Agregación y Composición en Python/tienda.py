# Se importan las clases necesarias
from venta import Venta
# Clase Tienda
class Tienda:
    # Inicializador
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.ventas: list[Venta] = []
    # Método para registrar una venta
    def registrar_venta(self, venta: Venta) -> None:
        self.ventas.append(venta)