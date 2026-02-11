# Clase Producto
class Producto:
    # Atributo de clase para contar productos
    contador_productos = 0
    # Inicializador
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio
        # Incrementar el contador de productos al crear una nueva instancia
        Producto.contador_productos += 1
    # Método estático para validar el precio
    @staticmethod
    def es_precio_valido(precio: float) -> bool:
        return precio > 0
    
    @classmethod
    def total_productos(cls) -> int:
        return cls.contador_productos