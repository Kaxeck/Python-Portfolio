from calculadora import Calculadora
#Funcion que recibe como lista una cadena de expresion e indentifica los operadores
def interpretar_expresion(expresion):
    for operador in ["+", "-", "*", "/", "^"]:
        # Verifica si el operador se encuentra en la expresion
        if operador in expresion:
            # Funcion que elimina los operadores de la cadena de expresion
            partes = expresion.split(operador)   
            # Se agrega un try/excep que retorna un valor de None para una respuesta
            try:
                # Se convierte la expresion en una lista, eliminando los espacios vacios y retorno la lista y operador
                lista = [float(p.strip()) for p in partes]
                return lista, operador
            except ValueError:
                return None
# Funcion principal que inicializa un objeto de la clase "Calculadora"
def main():
    calc = Calculadora([])
    # Instrucciones iniciales para el usuario
    print("Calculadora Básica. Escribe 'salir' para terminar o  'historial' para ver operaciones.\n")
    # Bucle que permite ingresar al usuario operaciones continuamente
    while True:
        entrada = input("Ingresa la operacion (ejemplo 5 + 5 + 5): ")
        # Condicion para salir de la calculadora
        if entrada.strip().lower() == "salir":
            print("¡Hasta pronto!")
            break
        # Condicion para ver el historial de la calculadora
        if entrada.strip().lower() == "historial":
            calc.ver_historial()
            continue
        # Validacion de la expresion en caso de la existencia de un error
        resultado = interpretar_expresion(entrada)
        if not resultado:
            print("Expresion no valida. Usa el formato: numero operador numero (ej. 5 + 5 + 5)\n")
            continue
        # Asignacion de los valores devueltos por interpretar_expresion
        lista, operador = resultado
        calc.lista_numero = lista
        # Validada el tipo de operacion a realizar segun la expresion del usuario
        resultado1 = None
        if operador == "+":
            resultado1 = calc.sumar()
        elif operador == "-":
            resultado1 = calc.restar()
        elif operador == "*":
            resultado1 = calc.multiplicar()
        elif operador == "/":
            resultado1 = calc.dividir()
        elif operador == "^":
            resultado1 = calc.potencia()
        # Valida que la operacion se realizo correctamente y no mando ningun error
        if resultado1 is not None:
            print("Resultado:", resultado1)
# Se llama a la funcion main  para iniciar la calculadora
main()
