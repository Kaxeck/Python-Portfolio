# Funcion para validar datos de entrada
def validar_datos(nombre, edad, correo):
    # Imprimir los datos recibidos
    print(f"\nValidando datos para: {nombre}, {edad}, {correo}")
    # Bloque try-except para manejar excepciones
    try:
        # Validación de tipos de datos
        if not isinstance(nombre, str) or not isinstance(edad, int):
            raise TypeError("Tipo de dato incorrecto.")
        # Validación de edad
        if edad < 0:
            raise ValueError("La edad debe ser mayor a cero.")
        # Validación de nombre vacío
        if len(nombre.strip()) == 0:
            raise ValueError("El nombre no puede estar vacío.")
        # Validación simple del correo electrónico
        if "@" not in correo:
            raise ValueError("El correo electrónico no es válido.")
        # Muestra de error zero division
        división = 100 / edad
        # Mensaje de éxito
        print("Datos válidos")
    # Captura de excepciones de TypeError
    except TypeError as e:
        print(f"Error de tipo: {e}")
    # Captura de excepciones de ValueError
    except ValueError as e:
        print(f"Error de validación: {e}")
    # Captura de excepciones de ZeroDivisionError
    except ZeroDivisionError as e:
        print("Error de división por cero")
    # Captura de cualquier otra excepción
    except Exception as e:
        print(f"Error inesperado: {e}")
    # Mensaje final
    finally:
        print("Validación de datos finalizada.")
# Función de datos de prueba
def probar_validaciones():
    # Error de tipo de dato en edad
    validar_datos("Juan Pérez", "a", "juan@xample.com")
    # Error de tipo de dato en nombre
    validar_datos(46478, 30, "46478@example.com")
    # Edad menor a cero
    validar_datos("María Gómez", -5, "maria@example.com")
    # Nombre vacío
    validar_datos("", 22, "nombrevacio@example.com")
    # Correo electrónico inválido
    validar_datos("Luis Martínez", 28, "luismartinezgmail.com")
    # Error de división por cero
    validar_datos("Carlos Sánchez", 0, "carlos@example.com")
    # Caso válido
    validar_datos("Ana López", 25, "ana@example.com")
# Ejecutar las pruebas
probar_validaciones()