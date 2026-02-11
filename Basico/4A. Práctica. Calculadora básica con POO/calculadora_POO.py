# Se crea una clase llamada Calculadora como base para el programa
class Calculadora:
    numero1 = 0
    numero2 = 0 
    # Se crea un constructor que reciba los dos parametros para inicializar los valores
    def __init__(self, numero1, numero2):
        # Atributos protegidos para guardar los valores del parametro
        self._numero1 = numero1
        self._numero2 = numero2
        # Lista para almacenar el historial de operaciones
        self._historial = []
    # Propiedad que permite consultar el primer numero sin modificarlo
    @property
    def numero1(self):
        return self._numero1
    # Propiedad que permite asignar un nuevo valor al atributo del primer numero
    @numero1.setter
    def numero1(self, nuevo_numero1):
        # Validacion para asegurar entrada de numeros enteros o decimales
        if type(nuevo_numero1) in (int, float):
            self._numero1 = nuevo_numero1
        # Si no es un numero muestra un error
        else:
            raise ValueError("Debe ser un numero")
    # Propiedad que permite consultar el segundo numero sin modificarlo
    @property
    def numero2(self):
        return self._numero2
    # Propiedad que permite asignar un nuevo valor al atributo del segundo numero
    @numero2.setter
    def numero2(self, nuevo_numero2):
        # Validacion para asegurar entrada de numeros enteros o decimales
        if type(nuevo_numero2) in (int, float):
            self._numero2 = nuevo_numero2
        # Si no es un numero muestra un error
        else:
            raise ValueError("Debe ser un numero")
    # Metodo que realiza la operacion de suma entre atributos, guardando en resultados    
    def sumar(self):
        resultado = self._numero1 + self._numero2
        self._registrar_operacion("+", resultado)
        return resultado
    # Metodo que realiza la operacion de resta entre atributos, guardando en resultados 
    def restar(self):
        resultado = self._numero1 - self._numero2
        self._registrar_operacion("-", resultado)
        return resultado
    # Metodo que realiza la operacion de multiplicacion entre atributos, guardando en resultados 
    def multiplicar(self):
        resultado = self._numero1 * self._numero2
        self._registrar_operacion("*", resultado)
        return resultado
    # Metodo que realiza la operacion de division entre atributos, guardando en resultados 
    def dividir(self):
        resultado = self._numero1 / self._numero2
        # Se utiliza el metodo _registrar_operacion pasando como argumento el simbolo y resultado 
        self._registrar_operacion("/", resultado)
        return resultado
    # Metodo privado para registro en historial
    def _registrar_operacion(self, operador, resultado):
        # Se agrega un diccionario a la lista _historial
        self._historial.append({
            "operacion": f"{self._numero1} {operador} {self._numero2}",
            "resultado": resultado
        })
    # Metodo para visualizar historial
    def ver_historial(self):
        # Validacion para asegurar que la lista no esta vacia
        if not self._historial:
            print("No hay operaciones en el historial")
            return
        # Cuando no esta vacia se devuelve el historial 
        else:
            print("\n--- Historial de Operaciones ---")
            contador = 1
            for operacion in self._historial:
                print(f"{contador}. {operacion['operacion']} = {operacion['resultado']}")
                contador += 1
#Funcion que recibe como parametros una cadena de expresion e indentifica los operadores
def interpretar_expresion(expresion):
    for operador in ["+", "-", "*", "/"]:
        # Verifica si el operador actual se encuentra en la expresion y la divide en partes
        if operador in expresion:
            partes = expresion.split(operador)   
            # Si son dos partes, convierte los elementos a numeros float y elimina espacios 
            if len(partes) == 2:
                # El codigo original se rompe en caso de ingresar caracteres por ello se agrega un try/excep 
                # Que retorna un valor de None para una respuesta
                try:
                    num1 = float(partes[0].strip())
                    num2 = float(partes[1].strip())
                except ValueError:
                    return None
                return num1, num2, operador
# Funcion principal que inicializa un objeto de la clase "Calculadora"
def main():
    calc = Calculadora(0,0)
    # Instrucciones iniciales para el usuario
    print("Calculadora Básica. Escribe 'salir' para terminar o  'historial' para ver operaciones.\n")
    # Bucle que permite ingresar al usuario operaciones continuamente
    while True:
        entrada = input("Ingresa la operacion (ejemplo 5 + 5): ")
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
            print("Expresion no valida. Usa el formato: numero operador numero (ej. 5 + 5)\n")
            continue
        # Asignacion de los valores devueltos por interpretar_expresion
        num1, num2, operador = resultado
        calc.numero1 = num1
        calc.numero2 = num2
        # Validada el tipo de operacion a realizar segun la expresion del usuario
        if operador == "+":
            print("Resultado:", calc.sumar())
        elif operador == "-":
            print("Resultado:", calc.restar())
        elif operador == "*":
            print("Resultado:", calc.multiplicar())
        elif operador == "/":
            print("Resultado:", calc.dividir())
# Se llama a la funcion main  para iniciar la calculadora
main()
