# Se crea una lista para almacenar todos los estudiantes
lista_estudiantes = []
# Se crea un diccionario para almacenar materias y calificaciones
materias = {}
# Se crea un función llamada promedio que permite calcular el promedio y darle un estado
def promedio(estudiante):
    # Se obtiene las calificaciones
    calificaciones = estudiante["calificaciones"].values()
    # Calculo de promedio
    promedio_final = sum(calificaciones) / len(calificaciones)
    # Condion de aprovado o reprobado
    if promedio_final >= 6:
        estado = "Aprobado"
    else:
        estado = "Reprobado"
    return promedio_final, estado

# Se inicia el sistema
print("Sistema de evaluacion")
print("\nRegistro de Materias:")
# Bucle para registro de materias
while True:
    # Se solicita el nombre de la materia
    print("Para dejar de cargar materias introduce exit")
    materia= input("Nombre de la materia: ")
    # Condicion para salir del bucle
    if materia.lower() == 'exit':
        if not materias:
            print("Debe registrar al menos una materia antes de salir.")
            continue
        else:
            break
    # Condicion cuando el espacio se queda vacio 
    if not materia.strip():
        print("No puede estar vacion el campo")
        continue
    # Se agrega la materia al diccionario
    materias[materia] =  None
    print("Se registro correctamente")
# Registro de alumnos
print("\nRegistro de alumnos")
# Cantidad de alumnos a registrar
no_alumnos = int(input("Numero de alumnos: "))
# Bucle para registro de alumnos segun la condicion anterior
for i in range(no_alumnos):
    print(f"\nRegistro del alumno {i+1} de {no_alumnos}")
    # Se solicita el nombre y se verifica que no este vacia
    while True:
        nombre= input("Nombre del alumno: ")
        if nombre.strip():
            break
        print("No puede estar vacion el campo")
    # Se solicita la matricula y se verifica que no este vacia
    while True:
        matricula= input("Matricula del alumno: ")
        if matricula.strip():
            break
        print("No puede estar vacion el campo")
    # Se crea un diccionario para los datos del estudiante 
    estudiante = {
        "nombre": nombre,
        "matricula": matricula,
        "calificaciones": materias.copy()
    }
    # Calificaciones
    print(f"Introduce las calificaciones para {nombre}")
    # Bucle para insertar las calificaciones de cada materia
    for materia in estudiante["calificaciones"]:
        while True:
            calificacion = input(f"Calificacion para {materia}: ")
            # Condicion cuando el espacio no se queda vacio 
            if calificacion.strip():
                # Convierte el tipo de dato de string a int
                calificacion = int(calificacion)
                # Guarda la calificacion en el diccionario del alumno
                estudiante["calificaciones"][materia] = calificacion
                break
            # Condicion cuando el espacio se queda vacio 
            else:
                print("No puede estar vacion el campo")
    # Se agrega el estudiante a la lista general
    lista_estudiantes.append(estudiante)
    print("Se registro correctamente")
# Resultados 
print("\nREGISTRO FINAL DEL SISTEMA")
# condicion que verifica si se registró al menos un estudiante
if not lista_estudiantes:
    print("No se registró ningún alumno.")
else:
    # Muestra la indormacion de cada estudiante
    for estudiante in lista_estudiantes:
        print(f"\nAlumno: {estudiante['nombre']} | Matrícula: {estudiante['matricula']}")
        print("Materias y Calificaciones:")
        for materia, calificacion in estudiante['calificaciones'].items():
            print(f" {materia}: {calificacion}")
        # Calcula el promedio y da el estado
        promedio_final, estado = promedio(estudiante)
        print(f"Promedio: {promedio_final:.2f} | Estado: {estado}")
