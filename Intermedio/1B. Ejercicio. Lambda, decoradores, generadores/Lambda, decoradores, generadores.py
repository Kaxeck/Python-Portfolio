# Importar time
import time
# Importar reduce desde functools
from functools import reduce
# Lista interna de tuplas con estado y temperatura
lista = [
    ("Guanajuato", 38),
    ("Jalisco", 35),
    ("Michoacan", 25),
    ("Puebla", 20),
    ("Queretaro", 15),
    ("Quintana Roo", 42),
    ("San Luis Potosi", 32),
    ("Sinaloa", 36),
    ]
# Decorador para auditar funciones
def auditoria_funcion(funcion):
    def funcion_tiempo(*args, **kwargs):
        # Incrementar el contador de llamadas
        funcion_tiempo.conteo += 1
        # Imprimir información de auditoría
        print(f"\nEjecucion de la función: {funcion.__name__}")
        print(f"Número de llamadas: {funcion_tiempo.conteo}")
        # Medir el tiempo de ejecución
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        tiempo = fin - inicio
        # Imprimir información de tiempo de ejecución
        print(f"Tiempo de ejecución de {funcion.__name__}: {tiempo:.6f} segundos")
        return resultado
    # Inicializar el contador de llamadas
    funcion_tiempo.conteo = 0
    return funcion_tiempo

# Generador de temperaturas de diferentes estados
@auditoria_funcion
def leer_temperaturas(datos):
    # Iterar sobre los datos y yield cada temperatura
    for temperatura in datos:
        yield temperatura
    print("Lectura de temperaturas finalizada.")

# Función principal para monitorear temperaturas
@auditoria_funcion
def monitoreo():
    # Filtrar estados con temperaturas mayores a 30 grados Celsius usando filter y lambda
    calor = list(filter(lambda x: x[1] > 30, leer_temperaturas(lista)))
    # Ordenar la lista resultante de mayor a menor temperatura usando sorted y lambda
    orden = sorted(calor, key=lambda x: x[1], reverse=True)
    # Transformar la lista en mensajes de alerta usando map y lambda
    transformacion = list(map(lambda x: f"Alerta de calor en {x[0]}: {x[1]}°C", orden))
    # Calcular el promedio de las temperaturas usando reduce y lambda
    suma = reduce(lambda x, y: x + y[1], orden, 0)
    # Calcular el promedio dividiendo la suma entre el número de elementos
    promedio = suma / len(orden)
    print("\nMonitoreo finalizado.")
    return promedio, transformacion

# Función main para ejecutar el monitoreo y mostrar resultados
@auditoria_funcion
def main(promedio, transformacion):
    for alerta in transformacion:
        print(alerta)
    print(f"\nEl promedio de la temperatura es: {promedio}")
    print("Fin del programa.")

main(*monitoreo())
