# Se crea una clase llamada Calculadora como base para el programa
class Calculadora:
    # Creacion de una lista de numeros
    lista_numero = [] 
    # Se crea un constructor que reciba la lista para inicializar los valores
    def __init__(self, lista_numero):
        # lista protegida para guardar los valores del parametro
        self._lista_numero = lista_numero
        # Lista para almacenar el historial de operaciones
        self._historial = []
    # Propiedad que permite consultar la lista de numeros sin modificarlos
    @property
    def lista_numero(self):
        return self._lista_numero
    # Propiedad que permite asignar un nuevo valores a la lista de numeros
    @lista_numero.setter
    def lista_numero(self, nueva_lista):
        # Validacion para asegurar entrada de numeros enteros o decimales en toda la lista
        if not all(isinstance(n, (int, float)) for n in nueva_lista):
            raise ValueError("Todos los elementos de la lista deben ser números.")
        
        self._lista_numero = nueva_lista
    # Metodo que realiza la operacion de suma entre lista de numeros, guardando en resultados    
    def sumar(self):
        resultado = sum(self._lista_numero)
        # Se utiliza el metodo _registrar_operacion pasando como argumento el simbolo y resultado 
        self._registrar_operacion("+", resultado)
        return resultado
    # Metodo que realiza la operacion de resta entre lista de numeros, guardando en resultados 
    def restar(self):
        resultado = self.lista_numero[0]
        for n in self.lista_numero[1:]:
            resultado -= n
        # Se utiliza el metodo _registrar_operacion pasando como argumento el simbolo y resultado 
        self._registrar_operacion("-", resultado)
        return resultado
    # Metodo que realiza la operacion de multiplicacion entre lista de numeros, guardando en resultados 
    def multiplicar(self):
        resultado = self.lista_numero[0]
        for n in self.lista_numero[1:]:
            resultado *= n
        # Se utiliza el metodo _registrar_operacion pasando como argumento el simbolo y resultado 
        self._registrar_operacion("*", resultado)
        return resultado
    # Metodo que realiza la operacion de division entre lista de numeros, guardando en resultados 
    def dividir(self):
        # Se hace uso de try y except para solucionar el error de indeterminacion
        try:
            resultado = self._lista_numero[0]
            for n in self._lista_numero[1:]:
                resultado /= n
            # Se utiliza el metodo _registrar_operacion pasando como argumento el simbolo y resultado 
            self._registrar_operacion("/", resultado)
            return resultado
        except ZeroDivisionError:
             print("No se puede dividir por cero.")
    # Metodo que realiza la operacion de potencias entre lista de nuemros, guardando en resultados 
    def potencia(self):
        resultado = self.lista_numero[0]
        for n in self.lista_numero[1:]:
            resultado **= n
        # Se utiliza el metodo _registrar_operacion pasando como argumento el simbolo y resultado 
        self._registrar_operacion("^", resultado)
        return resultado
    # Metodo privado para registro en historial
    def _registrar_operacion(self, operador, resultado):
        # Se convierte los daros de la lista en tipo string  para uso del metodo join
        lista_str = [str(n) for n in self._lista_numero]
        # Se agrega un diccionario a la lista _historial 
        self._historial.append({
            "operacion": f" {operador} ".join(lista_str),
            "resultado": resultado
        })
    # Metodo para visualizar historial
    def ver_historial(self):
        # Validacion para asegurar que la lista no esta vacia
        if not self._historial:
            print("No hay operaciones en el historial")
            return
        # Si no está vacia se imprime el historial
        else:
            print("\n--- Historial de Operaciones ---")
            contador = 1
            for operacion in self._historial:
                print(f"{contador}. {operacion['operacion']} = {operacion['resultado']}")
                contador += 1
