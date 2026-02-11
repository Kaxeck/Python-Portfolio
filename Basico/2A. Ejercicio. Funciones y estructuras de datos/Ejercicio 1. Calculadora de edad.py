# Esta libreria permite el uso de fechas
import datetime
# Se crea un diccionario para almacenar toda la informacion del cliente
perfil = {"nombre": "", "nacimiento": "", "edad": None, "estado_cumpleanos": ""}

# Se inicia el sistema
print("Formulario de Seguro")
print("\nCompleta los siguientes datos:")
# Bucle para evitar los campos vacios en la introduccion del nombre
while True:
    # Se solicita el nombre
    perfil["nombre"] = input("Nombre: ")
    # Condicion que permite romper el bucle cuando se cumple
    if perfil["nombre"].strip():
        break
    # Condicion cuando el espacio se queda vacio  
    else:
        print("El campo no puede estar vacio")
# Se crea un función llamada calculo_edad que permite el calculo de la edad
# segun la fecha de nacimiento y valida la fecha
def calculo_edad():
    try:
        # Se llama a la variable global
        global fecha_nacimiento
        # Se convierte del tipo string a tipo date la fecha
        fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, "%d-%m-%Y").date()
        # Condicion que comprueba que el año de nacimiento debe ser mayor de 1900. 
        if fecha_nacimiento.year < 1900:
            #Se retorna inavlido como condicion para el while de fecha de nacimiento 
            return "invalido"
        # Se obtiene la fecha actual
        hoy = datetime.date.today()
        # Se crean tupla para facilitar la comparacion de las fechas
        nacimiento_tupla = (fecha_nacimiento.month, fecha_nacimiento.day)
        hoy_tupla = (hoy.month, hoy.day)
        # Operacion para calcular las fechas con ayuda de las tuplas
        edad = hoy.year - fecha_nacimiento.year - ((hoy_tupla) < (nacimiento_tupla))
        # Se usan varias condiciones comparando las tupla para verficar el estado 
        if hoy_tupla == nacimiento_tupla:
            estado = "Hoy es el cumpleaños del cliente"
        elif hoy_tupla > nacimiento_tupla:
            estado = "El cliente ya cumplio años"
        else: 
            estado= "El cliente aun no ha cumplido años"
        # Se actualiza el diccionario con los datos calculados
        perfil["edad"] = edad
        perfil["estado_cumpleanos"] = estado
        perfil["nacimiento"] = fecha_nacimiento
        #Se retorna true como condicion para el while de fecha de nacimiento        
        return True
    
    except ValueError:
        print("Formato de fecha inválido o no existe")
        #Se retorna none como condicion para el while de fecha de nacimiento 
        return None
# Bucle para solicitar y validar fecha
while True:
    # Se solicita la fecha de nacimiento al usuario
    fecha_nacimiento = input("Fecha de nacimiento (formato DD-MM-AAAA):")
    # Se llama a la funcion calculo_edad
    validacion = calculo_edad()
    # Condiciones que evaluan el resultado de la funcion
    if validacion == "invalido":
        print("El año de nacimiento debe ser mayor de 1900")
        break
    elif validacion is not None:
        print("Fecha de nacimiento:")
        print(perfil["nacimiento"])
        print("edad:")
        print(perfil["edad"])
        print("Estado del cumpleaños:")
        print(perfil["estado_cumpleanos"])
        break
    else:
        # Si la funcion devolvio None el bucle continuara, pidiendo la fecha de nuevo.
        print("Por favor, intentalo de nuevo")