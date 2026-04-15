# ============================================================
# Sistema de Gestión de Notas de Estudiantes
# Asignatura: Programación 2 - ECC-1A
# Descripción:
#   Aplicación para registrar estudiantes, asignar notas,
#   calcular promedios y mostrar resultados.
#   Implementa estructuras lógicas, repetitivas y funciones
#   documentadas con comentarios explicativos.
# ============================================================

# Lista global que almacena todos los estudiantes registrados
# Se inicializa con datos de ejemplo para demostrar el funcionamiento
estudiantes = [
    {"nombre": "Ana García",    "notas": [8.5, 9.0, 7.5, 9.5]},
    {"nombre": "Luis Pérez",    "notas": [6.0, 5.5, 7.0, 6.5]},
    {"nombre": "María Torres",  "notas": [4.0, 3.5, 5.0, 4.5]},
    {"nombre": "Carlos Ruiz",   "notas": [10.0, 9.5, 10.0, 9.0]},
    {"nombre": "Sofía León",    "notas": []},
]


def mostrar_menu():
    """Muestra el menú principal del sistema."""
    print("\n╔══════════════════════════════════════╗")
    print("║   SISTEMA DE GESTIÓN DE NOTAS        ║")
    print("╠══════════════════════════════════════╣")
    print("║  1. Registrar estudiante             ║")
    print("║  2. Agregar nota a estudiante        ║")
    print("║  3. Ver notas de un estudiante       ║")
    print("║  4. Ver todos los estudiantes        ║")
    print("║  5. Estudiante con mejor promedio    ║")
    print("║  6. Salir                            ║")
    print("╚══════════════════════════════════════╝")


def leer_opcion():
    """
    Solicita y valida la opción ingresada por el usuario.
    Repite la solicitud hasta recibir un número válido.
    """
    while True:
        opcion = input("\nSeleccione una opción: ").strip()
        # Verifica que la opción sea un número entero
        if opcion.isdigit():
            return int(opcion)
        else:
            print("⚠  Error: ingrese un número válido.")


def registrar_estudiante():
    """
    Registra un nuevo estudiante en el sistema.
    Valida que el nombre no esté vacío y que no exista duplicado.
    """
    print("\n--- Registrar Estudiante ---")

    while True:
        nombre = input("Nombre del estudiante: ").strip()

        # Validación: el nombre no puede estar vacío
        if nombre == "":
            print("⚠  Error: el nombre no puede estar vacío.")
            continue

        # Validación: verificar si el estudiante ya existe
        existe = False
        for est in estudiantes:
            if est["nombre"].lower() == nombre.lower():
                existe = True
                break

        if existe:
            print(f"⚠  El estudiante '{nombre}' ya está registrado.")
        else:
            break

    # Se crea el estudiante como un diccionario con nombre y lista de notas vacía
    nuevo_estudiante = {
        "nombre": nombre,
        "notas": []
    }

    estudiantes.append(nuevo_estudiante)
    print(f"✔  Estudiante '{nombre}' registrado correctamente.")


def buscar_estudiante(nombre):
    """
    Busca un estudiante por nombre en la lista global.
    Retorna el diccionario del estudiante si existe, o None si no se encuentra.
    """
    for est in estudiantes:
        if est["nombre"].lower() == nombre.lower():
            return est
    return None


def agregar_nota():
    """
    Permite agregar una nota a un estudiante existente.
    Valida que la nota esté en el rango permitido de 0 a 10.
    """
    print("\n--- Agregar Nota ---")

    # Verificar si hay estudiantes registrados antes de continuar
    if len(estudiantes) == 0:
        print("⚠  No hay estudiantes registrados aún.")
        return

    nombre = input("Nombre del estudiante: ").strip()
    estudiante = buscar_estudiante(nombre)

    # Verificar que el estudiante exista en el sistema
    if estudiante is None:
        print(f"⚠  No se encontró al estudiante '{nombre}'.")
        return

    while True:
        nota_str = input("Ingrese la nota (0 - 10): ").strip()

        try:
            nota = float(nota_str)
            # Validación: la nota debe estar dentro del rango permitido
            if 0 <= nota <= 10:
                estudiante["notas"].append(nota)
                print(f"✔  Nota {nota} agregada correctamente a '{nombre}'.")
                break
            else:
                print("⚠  Error: la nota debe estar entre 0 y 10.")
        except ValueError:
            print("⚠  Error: ingrese un valor numérico válido.")


def calcular_promedio(notas):
    """
    Calcula el promedio de una lista de notas.
    Retorna 0 si la lista está vacía para evitar errores de división por cero.
    """
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)


def determinar_estado(promedio, tiene_notas):
    """
    Determina el estado académico del estudiante según su promedio.
    Usa estructuras lógicas para clasificar en tres categorías.
    """
    if not tiene_notas:
        return "Sin notas registradas"
    elif promedio >= 7:
        return "✔  APROBADO"
    elif promedio >= 5:
        return "⚠  EN RECUPERACIÓN"
    else:
        return "✘  REPROBADO"


def ver_notas_estudiante():
    """
    Muestra las notas y el promedio de un estudiante específico.
    Indica además si aprobó, está en recuperación o reprobó.
    """
    print("\n--- Ver Notas de Estudiante ---")

    if len(estudiantes) == 0:
        print("⚠  No hay estudiantes registrados aún.")
        return

    nombre = input("Nombre del estudiante: ").strip()
    estudiante = buscar_estudiante(nombre)

    if estudiante is None:
        print(f"⚠  No se encontró al estudiante '{nombre}'.")
        return

    notas = estudiante["notas"]
    print(f"\n  Estudiante: {estudiante['nombre']}")
    print("  " + "-" * 30)

    # Verificar si el estudiante tiene notas antes de mostrarlas
    if len(notas) == 0:
        print("  Sin notas registradas aún.")
    else:
        print("  Notas registradas:")

        # Recorrer e imprimir cada nota con su número de orden
        for i in range(len(notas)):
            print(f"    Nota {i + 1}: {notas[i]:.1f}")

        promedio = calcular_promedio(notas)
        estado   = determinar_estado(promedio, True)
        print(f"\n  Promedio: {promedio:.2f}")
        print(f"  Estado:   {estado}")


def ver_todos_estudiantes():
    """
    Muestra la lista completa de estudiantes con su promedio y estado académico.
    Recorre toda la lista usando un ciclo for.
    """
    print("\n╔══════════════════════════════════════════════════════════╗")
    print("║              LISTA DE TODOS LOS ESTUDIANTES             ║")
    print("╚══════════════════════════════════════════════════════════╝")

    if len(estudiantes) == 0:
        print("  ⚠  No hay estudiantes registrados aún.")
        return

    # Recorrer todos los estudiantes con un ciclo for
    for i in range(len(estudiantes)):
        est      = estudiantes[i]
        notas    = est["notas"]
        promedio = calcular_promedio(notas)
        estado   = determinar_estado(promedio, len(notas) > 0)

        print(f"\n  {i + 1}. {est['nombre']}")
        print(f"     Notas registradas : {len(notas)}")
        print(f"     Promedio          : {promedio:.2f}")
        print(f"     Estado            : {estado}")

    print("\n" + "─" * 60)


def mejor_estudiante():
    """
    Encuentra y muestra el estudiante con el mayor promedio.
    Solo considera estudiantes que tienen al menos una nota registrada.
    """
    print("\n--- Mejor Estudiante ---")

    if len(estudiantes) == 0:
        print("⚠  No hay estudiantes registrados aún.")
        return

    mejor          = None
    mayor_promedio = -1

    # Recorrer todos los estudiantes para comparar sus promedios
    for est in estudiantes:
        if len(est["notas"]) > 0:
            promedio = calcular_promedio(est["notas"])
            # Actualizar el mejor si este promedio supera al mayor encontrado
            if promedio > mayor_promedio:
                mayor_promedio = promedio
                mejor          = est

    # Verificar si algún estudiante tenía notas registradas
    if mejor is None:
        print("⚠  Ningún estudiante tiene notas registradas aún.")
    else:
        print(f"\n  🏆  Mejor estudiante : {mejor['nombre']}")
        print(f"      Promedio         : {mayor_promedio:.2f}")
        print(f"      Notas            : {mejor['notas']}")


def mostrar_bienvenida():
    """
    Muestra un mensaje de bienvenida con los estudiantes precargados al inicio.
    Sirve para demostrar que el sistema ya tiene datos funcionales desde el arranque.
    """
    print("\n╔══════════════════════════════════════════════════════════╗")
    print("║       SISTEMA DE GESTIÓN DE NOTAS - Programación 2      ║")
    print("╠══════════════════════════════════════════════════════════╣")
    print("║  Sistema iniciado con datos de ejemplo precargados.     ║")
    print(f"║  Estudiantes disponibles: {len(estudiantes)}                           ║")
    print("╚══════════════════════════════════════════════════════════╝")

    print("\n  Estudiantes precargados:")

    # Mostrar la lista inicial de estudiantes con su estado
    for est in estudiantes:
        promedio = calcular_promedio(est["notas"])
        tiene    = len(est["notas"]) > 0
        estado   = determinar_estado(promedio, tiene)
        print(f"   • {est['nombre']:20s} | Promedio: {promedio:.2f} | {estado}")


def main():
    """
    Función principal del sistema.
    Controla el flujo general del programa mediante un menú repetitivo.
    Carga datos de ejemplo al inicio para demostrar el funcionamiento.
    """
    mostrar_bienvenida()

    # Ciclo principal: el programa corre hasta que el usuario elija salir
    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            registrar_estudiante()
        elif opcion == 2:
            agregar_nota()
        elif opcion == 3:
            ver_notas_estudiante()
        elif opcion == 4:
            ver_todos_estudiantes()
        elif opcion == 5:
            mejor_estudiante()
        elif opcion == 6:
            print("\n  Cerrando el sistema. ¡Hasta luego!\n")
            break
        else:
            # Mensaje de error si la opción no corresponde al menú
            print("⚠  Opción no válida. Intente nuevamente.")


# Punto de entrada principal del programa
if __name__ == "__main__":
    main()
