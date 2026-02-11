# Se importan las clases necesarias
from usuario import Usuario
# Clase Administrador
class Administrador(Usuario):
    # Inicializador
    def __init__(self, nombre: str, correo: str, permisos: list[str]):
        super().__init__(nombre, correo)
        self.permisos = permisos
    # Método para mostrar información del administrador
    def mostrar_info(self) -> str:
        return f"Administrador: {self.nombre}, Correo: {self.correo}, Permisos: {', '.join(self.permisos)}"