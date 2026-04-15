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
estudiantes = []


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
            print("⚠ Error: ingrese un número válido.")


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
            print("⚠ Error: el nombre no puede estar vacío.")
            continue

        # Validación: verificar si el estudiante ya existe
        existe = False
        for est in estudiantes:
            if est["nombre"].lower() == nombre.lower():
                existe = True
                break

        if existe:
            print(f"⚠ El estudiante '{nombre}' ya está registrado.")
        else:
            break

    # Se crea el estudiante como un diccionario con nombre y lista de notas
    nuevo_estudiante = {
        "nombre": nombre,
        "notas": []
    }

    estudiantes.append(nuevo_estudiante)
    print(f"✔ Estudiante '{nombre}' registrado correctamente.")


def buscar_estudiante(nombre):
    """
    Busca un estudiante por nombre en la lista global.
    Retorna el diccionario del estudiante si lo encuentra, o None si no existe.
    """
    for est in estudiantes:
        if est["nombre"].lower() == nombre.lower():
            return est
    return None


def agregar_nota():
    """
    Permite agregar una nota a un estudiante existente.
    Valida que la nota esté entre 0 y 10.
    """
    print("\n--- Agregar Nota ---")

    # Verificar si hay estudiantes registrados antes de continuar
    if len(estudiantes) == 0:
        print("⚠ No hay estudiantes registrados aún.")
        return

    nombre = input("Nombre del estudiante: ").strip()
    estudiante = buscar_estudiante(nombre)

    # Verificar que el estudiante exista
    if estudiante is None:
        print(f"⚠ No se encontró al estudiante '{nombre}'.")
        return

    while True:
        nota_str = input("Ingrese la nota (0 - 10): ").strip()

        try:
            nota = float(nota_str)
            # Validación: la nota debe estar en el rango permitido
            if 0 <= nota <= 10:
                estudiante["notas"].append(nota)
                print(f"✔ Nota {nota} agregada correctamente a '{nombre}'.")
                break
            else:
                print("⚠ Error: la nota debe estar entre 0 y 10.")
        except ValueError:
            print("⚠ Error: ingrese un valor numérico válido.")


def calcular_promedio(notas):
    """
    Calcula el promedio de una lista de notas.
    Retorna 0 si la lista está vacía para evitar errores de división.
    """
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)


def ver_notas_estudiante():
    """
    Muestra las notas y el promedio de un estudiante específico.
    También indica si aprobó o reprobó según su promedio.
    """
    print("\n--- Ver Notas de Estudiante ---")

    if len(estudiantes) == 0:
        print("⚠ No hay estudiantes registrados aún.")
        return

    nombre = input("Nombre del estudiante: ").strip()
    estudiante = buscar_estudiante(nombre)

    if estudiante is None:
        print(f"⚠ No se encontró al estudiante '{nombre}'.")
        return

    notas = estudiante["notas"]

    print(f"\nEstudiante: {estudiante['nombre']}")

    # Verificar si el estudiante tiene notas registradas
    if len(notas) == 0:
        print("Sin notas registradas aún.")
    else:
        print("Notas registradas:")

        # Recorrer e imprimir cada nota con su número
        for i in range(len(notas)):
            print(f"  Nota {i + 1}: {notas[i]}")

        promedio = calcular_promedio(notas)
        print(f"Promedio: {promedio:.2f}")

        # Estructura lógica para determinar estado del estudiante
        if promedio >= 7:
            print("Estado: ✔ APROBADO")
        elif promedio >= 5:
            print("Estado: ⚠ EN RECUPERACIÓN")
        else:
            print("Estado: ✘ REPROBADO")


def ver_todos_estudiantes():
    """
    Muestra la lista completa de estudiantes registrados
    junto con su promedio y estado académico.
    """
    print("\n--- Lista de Estudiantes ---")

    if len(estudiantes) == 0:
        print("⚠ No hay estudiantes registrados aún.")
        return

    # Recorrer todos los estudiantes con un ciclo for
    for i in range(len(estudiantes)):
        est = estudiantes[i]
        promedio = calcular_promedio(est["notas"])
        cantidad = len(est["notas"])

        print(f"\n{i + 1}. {est['nombre']}")
        print(f"   Notas registradas: {cantidad}")
        print(f"   Promedio: {promedio:.2f}")

        # Determinar estado según el promedio calculado
        if cantidad == 0:
            print("   Estado: Sin notas")
        elif promedio >= 7:
            print("   Estado: ✔ Aprobado")
        elif promedio >= 5:
            print("   Estado: ⚠ En recuperación")
        else:
            print("   Estado: ✘ Reprobado")


def mejor_estudiante():
    """
    Encuentra y muestra el estudiante con el mayor promedio.
    Solo considera estudiantes que tienen al menos una nota registrada.
    """
    print("\n--- Mejor Estudiante ---")

    if len(estudiantes) == 0:
        print("⚠ No hay estudiantes registrados aún.")
        return

    mejor = None
    mayor_promedio = -1

    # Recorrer todos los estudiantes para comparar promedios
    for est in estudiantes:
        if len(est["notas"]) > 0:
            promedio = calcular_promedio(est["notas"])
            if promedio > mayor_promedio:
                mayor_promedio = promedio
                mejor = est

    # Verificar si algún estudiante tenía notas
    if mejor is None:
        print("⚠ Ningún estudiante tiene notas registradas aún.")
    else:
        print(f"🏆 Mejor estudiante: {mejor['nombre']}")
        print(f"   Promedio: {mayor_promedio:.2f}")


def main():
    """
    Función principal del sistema.
    Controla el flujo general del programa mediante un menú repetitivo.
    """
    print("\nBienvenido al Sistema de Gestión de Notas")

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
            print("\nCerrando el sistema. ¡Hasta luego!")
            break
        else:
            # Mensaje de error si la opción no está en el menú
            print("⚠ Opción no válida. Intente nuevamente.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
