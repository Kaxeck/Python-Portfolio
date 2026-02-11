# importar las colecciones necesarias
from collections import Counter, OrderedDict
# Lista de nombres de personas que realizaron compras
compras = ["Luis", "Ana", "Luis", "Carlos", "Marta", "Ana", "Sofia",
           "Elena", "Luis", "Carlos"]
# Lista para almacenar nombres de personas registradas
registrados = ["Ana", "Carlos", "Marta", "Elena"]
# Función para identificar clientes no registrados
def clientes_nuevos(compras, registrados):
    # Se usa diferencia de conjuntos para encontrar clientes no registrados
    return set(compras).difference(registrados)
# Función para obtener lista de compradores sin duplicados y en orden
def compradores(compras):
    # Se utiliza OrderedDict para mantener el orden ya que que set no pemite esto
    # y eliminar duplicados manteniendo el orden original
    lista_compras = list(OrderedDict.fromkeys(compras))
    return lista_compras
# Función para contar las compras por persona
def contador(compras):
    # Se utiliza Counter para contar las veces que cada persona realizó una compra
    conteo = Counter(compras)
    return conteo
# Función para generar un resumen de clientes con más de una compra usando dict comprehension
def resumen_clientes(contador):
    # Se crea un diccionario con clientes que tienen más de una compra
    resumen = {persona: f"Ha comprado {cantidad} veces" for persona, cantidad in contador.items() if cantidad > 1}
    return resumen
# Función main para ejecutar las operaciones y mostrar resultados
def main(): 
# Mostrar resultados de las funciones definidas
# Imprimir la lista de clientes no registrados
    print(f"\nClientes No Registrados: {clientes_nuevos(compras, registrados)}")
    # Imprimir la lista de compradores únicos
    print(f"\nLista de clientes únicos: {compradores(compras)}")
    # Imprimir el resumen de clientes frecuentes
    print("\nResumen por cliente frecuente:")
    for nombre, cantidad in resumen_clientes(contador(compras)).items():
        print(f'"{nombre}": "{cantidad}"')
# Ejecutar la función principal main 
main()