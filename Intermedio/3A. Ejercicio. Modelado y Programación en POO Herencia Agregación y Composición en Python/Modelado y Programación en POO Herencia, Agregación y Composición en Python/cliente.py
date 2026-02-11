# Se importan las clases necesarias
from usuario import Usuario
# Clase Cliente
class Cliente(Usuario):
    # Inicializador
    def __init__(self, nombre: str, correo: str, saldo: float):
        super().__init__(nombre, correo)
        self.saldo = saldo
    # Método para mostrar información del cliente
    def mostrar_info(self) -> str:
        return f"Cliente: {self.nombre}, Correo: {self.correo}, Saldo: ${self.saldo:.2f}"