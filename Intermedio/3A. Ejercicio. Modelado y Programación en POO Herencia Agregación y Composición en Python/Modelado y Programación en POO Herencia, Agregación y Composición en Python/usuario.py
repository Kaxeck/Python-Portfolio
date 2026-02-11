# Se importan las clases necesarias
from abc import ABC, abstractmethod 
# Clase Usuario
class Usuario(ABC):
    # Inicializador
    def __init__(self, nombre: str, correo: str):
        self.nombre = nombre
        self.correo = correo
    # Método abstracto para mostrar información del usuario
    @abstractmethod
    def mostrar_info(self) -> str:
        pass