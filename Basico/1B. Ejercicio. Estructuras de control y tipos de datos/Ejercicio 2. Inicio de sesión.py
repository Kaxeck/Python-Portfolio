# Credenciales validas (como variables individuales)
usuario_correcto= "admin"
clave_correcta= "1234"
# Variable de cantidad maxima de intentos
intentos = 3
# Bucle de inicio de sesion con un maximo de intentos hasta llegar a 0
while intentos > 0:
    # Incio del sistema
    print("\n--- Sistema de Inicio de Sesion ---")
    print(f"Intentos restantes: {intentos}")
    # Solicitar credenciales
    print("Usuario: ")
    usuario = input()
    print("Contraseña: ")
    clave = input()
    # Condiciones de inicio de sesion correcto
    if usuario == usuario_correcto and clave == clave_correcta:
        print("Inicio de sesion correcto")
        # Rompe el bucle12
        break
    # Condicion cuando los campos estan vacios
    elif not usuario or not clave:
        print("Error de autenticacion")
        continue
    # Condicion cuando las credenciales son incorrectas
    else:
        print("Credenciales invalidas")
        # Operacion que descuenta los intentos
        intentos -= 1
# Cuando en contador llega a 0 se cierra el bucle
else: 
    print("Te has quedado sin intentos")
    