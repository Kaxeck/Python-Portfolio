# Variable para contar billetes
billetes_1000 = 10
billetes_500 = 10
billetes_200 = 10
billetes_100 = 10
billetes_50 = 10

try:
    #  Iniciamos el sistema
    print("\n--- Dispensadora de Billetes")
    # Solicitar monto
    entrada = input("Ingresa la cantidad de billetes\n")
    # Transformamos el valor dato a un tipo de dato entero 
    monto = int(entrada)
    #Condiciones segun la entrada de la cantidad de billetes a retirar
    if monto <= 0:
        # Si el numero es negativo
        print("Error: Ingrese un monto positivo.")
    elif monto % 50 != 0:
        # Si el numero no es multiplo de 50.
        print("Error: El monto debe ser un múltiplo de $50.")
    else:
        # Variable para billetes a entregar
        entregar_1000 = 0
        entregar_500 = 0
        entregar_200 = 0
        entregar_100 = 0
        entregar_50 = 0
        monto_restante = monto
        # Calculo de billetes a entregar por denominacion y restando de mayor a menor
        entregar_1000 = min(monto_restante // 1000, billetes_1000)
        monto_restante -= entregar_1000 * 1000
        entregar_500 = min(monto_restante // 500, billetes_500)
        monto_restante -= entregar_500 * 500
        entregar_200 = min(monto_restante // 200, billetes_200)
        monto_restante-= entregar_200 * 200
        entregar_100 = min(monto_restante // 100, billetes_100)
        monto_restante -= entregar_100 * 100
        entregar_50 = min(monto_restante // 50, billetes_50)
        monto_restante -= entregar_50 * 50
        # Condicion de entrega de billtes y actualizacion de inventario
        if monto_restante == 0:
            print(f"\nTransacción exitosa por ${monto}")
            if entregar_1000 > 0: print(f"\nse entregaron {entregar_1000} billete(s) de $1000")
            if entregar_500 > 0: print(f"\nse entregaron {entregar_500} billete(s) de $500")
            if entregar_200 > 0: print(f"\nse entregaron {entregar_200} billete(s) de $200")
            if entregar_100 > 0: print(f"\nse entregaron {entregar_100} billete(s) de $100")
            if entregar_50 > 0: print(f"\nse entregaron {entregar_50} billete(s) de $50")
            # Actualizar el inventario
            billetes_1000 -= entregar_1000
            billetes_500 -= entregar_500
            billetes_200 -= entregar_200
            billetes_100 -= entregar_100
            billetes_50 -= entregar_50
        # Condicion cuando no hay suficientes billetes
        else:
            print("\nError: No hay suficientes billetes para completar la transacción.")
# Condicion cuando la entrada es difrente a las esperadas
except ValueError:
    print("Error: Por favor, ingrese un número válido.")