"""
Sistema de Gestión de Notas de Estudiantes
Desarrollado para Aprendizaje Autónomo 2
Autor: CESAR ANDRÉS CHARI GUAMAN
Fecha: 12 de abril de 2026

Descripción general:
Aplicación de consola para gestionar estudiantes y sus calificaciones.
Permite registrar estudiantes, agregar notas, consultar promedios,
mostrar reportes, editar información, eliminar registros y guardar
los datos en un archivo JSON.

Este sistema fue diseñado para evidenciar:
- estructuras lógicas
- estructuras repetitivas
- modularización del código
- validación de datos
- comentarios y documentación de funciones
"""

import json
import os

ARCHIVO_DATOS = "estudiantes.json"
estudiantes = []


def limpiar_pantalla():
    """
    Limpia la consola según el sistema operativo.
    No es indispensable para el funcionamiento, pero mejora la presentación.
    """
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    """
    Detiene momentáneamente el programa hasta que el usuario presione Enter.
    """
    input("\nPresione Enter para continuar...")


def cargar_datos():
    """
    Carga los datos desde un archivo JSON si existe.
    Si el archivo no existe o está dañado, inicia con una lista vacía.
    """
    global estudiantes

    if not os.path.exists(ARCHIVO_DATOS):
        estudiantes = []
        return

    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

            # Validación básica del contenido cargado
            if isinstance(datos, list):
                estudiantes = datos
            else:
                estudiantes = []
    except (json.JSONDecodeError, OSError):
        print("⚠ Advertencia: no se pudo cargar el archivo de datos.")
        estudiantes = []


def guardar_datos():
    """
    Guarda la información actual de estudiantes en un archivo JSON.
    Esto permite que los datos permanezcan disponibles aunque el programa se cierre.
    """
    try:
        with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
            json.dump(estudiantes, archivo, indent=4, ensure_ascii=False)
    except OSError:
        print("⚠ Error: no se pudieron guardar los datos.")


def mostrar_encabezado():
    """
    Muestra el título principal del sistema.
    """
    print("=" * 70)
    print("               SISTEMA DE GESTIÓN DE NOTAS")
    print("=" * 70)


def mostrar_menu():
    """
    Presenta el menú principal con todas las opciones del sistema.
    """
    limpiar_pantalla()
    mostrar_encabezado()
    print("1. Registrar estudiante")
    print("2. Agregar nota a estudiante")
    print("3. Ver notas de un estudiante")
    print("4. Ver todos los estudiantes")
    print("5. Mostrar mejor estudiante")
    print("6. Editar nombre de estudiante")
    print("7. Eliminar estudiante")
    print("8. Guardar datos")
    print("9. Salir")
    print("=" * 70)


def leer_entero(mensaje, minimo=None, maximo=None):
    """
    Solicita al usuario un número entero y lo valida.
    Puede restringirse con un valor mínimo y máximo.
    """
    while True:
        entrada = input(mensaje).strip()

        try:
            valor = int(entrada)

            if minimo is not None and valor < minimo:
                print(f"❌ Error: el valor debe ser mayor o igual a {minimo}.")
                continue

            if maximo is not None and valor > maximo:
                print(f"❌ Error: el valor debe ser menor o igual a {maximo}.")
                continue

            return valor
        except ValueError:
            print("❌ Error: debe ingresar un número entero válido.")


def leer_decimal(mensaje, minimo=None, maximo=None):
    """
    Solicita al usuario un número decimal y lo valida.
    Puede restringirse con un valor mínimo y máximo.
    """
    while True:
        entrada = input(mensaje).strip()

        try:
            valor = float(entrada)

            if minimo is not None and valor < minimo:
                print(f"❌ Error: el valor debe ser mayor o igual a {minimo}.")
                continue

            if maximo is not None and valor > maximo:
                print(f"❌ Error: el valor debe ser menor o igual a {maximo}.")
                continue

            return valor
        except ValueError:
            print("❌ Error: debe ingresar un valor numérico válido.")


def leer_texto_no_vacio(mensaje):
    """
    Solicita un texto y valida que no esté vacío.
    """
    while True:
        texto = input(mensaje).strip()

        if texto == "":
            print("❌ Error: este campo no puede estar vacío.")
        else:
            return texto.title()


def buscar_estudiante_por_nombre(nombre):
    """
    Busca un estudiante por nombre.
    Retorna el diccionario del estudiante si lo encuentra; de lo contrario, None.
    """
    for estudiante in estudiantes:
        if estudiante["nombre"].lower() == nombre.lower():
            return estudiante
    return None


def listar_estudiantes_basico():
    """
    Muestra un listado simple de estudiantes para que el usuario pueda seleccionar uno.
    """
    if not estudiantes:
        print("❌ No hay estudiantes registrados.")
        return False

    print("\nEstudiantes registrados:")
    for i, estudiante in enumerate(estudiantes, start=1):
        print(f"{i}. {estudiante['nombre']}")
    return True


def seleccionar_estudiante():
    """
    Permite seleccionar un estudiante por número dentro del listado.
    Retorna el estudiante seleccionado o None si no hay estudiantes.
    """
    if not listar_estudiantes_basico():
        return None

    opcion = leer_entero("\nSeleccione un estudiante por número: ", 1, len(estudiantes))
    return estudiantes[opcion - 1]


def calcular_promedio(notas):
    """
    Calcula el promedio de una lista de notas.
    Si no existen notas, retorna 0.0 para evitar división por cero.
    """
    if len(notas) == 0:
        return 0.0
    return sum(notas) / len(notas)


def obtener_estado_academico(promedio, cantidad_notas):
    """
    Determina el estado académico del estudiante en función de su promedio.
    Usa estructuras lógicas para clasificar el rendimiento.
    """
    if cantidad_notas == 0:
        return "SIN NOTAS"
    elif promedio >= 9:
        return "EXCELENTE"
    elif promedio >= 7:
        return "APROBADO"
    elif promedio >= 6:
        return "RECUPERACIÓN"
    else:
        return "REPROBADO"


def registrar_estudiante():
    """
    Registra un nuevo estudiante validando que no exista otro con el mismo nombre.
    """
    limpiar_pantalla()
    mostrar_encabezado()
    print("--- REGISTRAR ESTUDIANTE ---\n")

    nombre = leer_texto_no_vacio("Ingrese el nombre del estudiante: ")

    if buscar_estudiante_por_nombre(nombre) is not None:
        print(f"❌ Error: ya existe un estudiante llamado '{nombre}'.")
        pausar()
        return

    nuevo_estudiante = {
        "nombre": nombre,
        "notas": []
    }

    estudiantes.append(nuevo_estudiante)
    guardar_datos()

    print(f"✅ Estudiante '{nombre}' registrado correctamente.")
    pausar()


def agregar_nota():
    """
    Permite agregar una nota a un estudiante existente.
    La nota debe estar entre 0 y 10.
    """
    limpiar_pantalla()
    mostrar_encabezado()
    print("--- AGREGAR NOTA A ESTUDIANTE ---\n")

    estudiante = seleccionar_estudiante()
    if estudiante is None:
        pausar()
        return

    nota = leer_decimal(
        f"Ingrese la nota para {estudiante['nombre']} (0 a 10): ",
        0,
        10
    )

    estudiante["notas"].append(round(nota, 2))
    guardar_datos()

    print(f"✅ Nota agregada correctamente a '{estudiante['nombre']}'.")
    pausar()


def ver_notas_estudiante():
    """
    Muestra todas las notas de un estudiante, su promedio y su estado académico.
    """
    limpiar_pantalla()
    mostrar_encabezado()
    print("--- VER NOTAS DE UN ESTUDIANTE ---\n")

    estudiante = seleccionar_estudiante()
    if estudiante is None:
        pausar()
        return

    notas = estudiante["notas"]
    promedio = calcular_promedio(notas)
    estado = obtener_estado_academico(promedio, len(notas))

    print(f"\nNombre: {estudiante['nombre']}")
    print("-" * 50)

    if len(notas) == 0:
        print("Este estudiante aún no tiene notas registradas.")
    else:
        print("Notas registradas:")
        for i, nota in enumerate(notas, start=1):
            print(f"  Nota {i}: {nota:.2f}")

    print(f"\nPromedio: {promedio:.2f}")
    print(f"Estado académico: {estado}")
    pausar()


def ver_todos_estudiantes():
    """
    Muestra una tabla general con todos los estudiantes, cantidad de notas,
    promedio y estado académico.
    """
    limpiar_pantalla()
    mostrar_encabezado()
    print("--- LISTADO GENERAL DE ESTUDIANTES ---\n")

    if len(estudiantes) == 0:
        print("❌ No hay estudiantes registrados.")
        pausar()
        return

    print(f"{'N°':<4}{'NOMBRE':<25}{'NOTAS':<10}{'PROMEDIO':<12}{'ESTADO'}")
    print("-" * 70)

    for i, estudiante in enumerate(estudiantes, start=1):
        cantidad_notas = len(estudiante["notas"])
        promedio = calcular_promedio(estudiante["notas"])
        estado = obtener_estado_academico(promedio, cantidad_notas)

        print(
            f"{i:<4}"
            f"{estudiante['nombre']:<25}"
            f"{cantidad_notas:<10}"
            f"{promedio:<12.2f}"
            f"{estado}"
        )

    pausar()


def mostrar_mejor_estudiante():
    """
    Determina cuál es el estudiante con mejor promedio.
    Solo considera estudiantes que tengan al menos una nota registrada.
    """
    limpiar_pantalla()
    mostrar_encabezado()
    print("--- MEJOR ESTUDIANTE ---\n")

    if len(estudiantes) == 0:
        print("❌ No hay estudiantes registrados.")
        pausar()
        return

    mejor = None
    mejor_promedio = -1

    # Se recorre toda la lista para comparar promedios y hallar el valor máximo.
    for estudiante in estudiantes:
        if len(estudiante["notas"]) > 0:
            promedio = calcular_promedio(estudiante["notas"])
            if promedio > mejor_promedio:
                mejor_promedio = promedio
                mejor = estudiante

    if mejor is None:
        print("❌ Ningún estudiante tiene notas registradas todavía.")
    else:
        estado = obtener_estado_academico(mejor_promedio, len(mejor["notas"]))
        print(f"Nombre: {mejor['nombre']}")
        print(f"Promedio: {mejor_promedio:.2f}")
        print(f"Estado académico: {estado}")

    pausar()


def editar_nombre_estudiante():
    """
    Permite cambiar el nombre de un estudiante ya registrado.
    Se valida que el nuevo nombre no exista previamente.
    """
    limpiar_pantalla()
    mostrar_encabezado()
    print("--- EDITAR NOMBRE DE ESTUDIANTE ---\n")

    estudiante = seleccionar_estudiante()
    if estudiante is None:
        pausar()
        return

    nuevo_nombre = leer_texto_no_vacio("Ingrese el nuevo nombre: ")

    estudiante_existente = buscar_estudiante_por_nombre(nuevo_nombre)
    if estudiante_existente is not None and estudiante_existente != estudiante:
        print(f"❌ Error: ya existe otro estudiante llamado '{nuevo_nombre}'.")
        pausar()
        return

    nombre_anterior = estudiante["nombre"]
    estudiante["nombre"] = nuevo_nombre
    guardar_datos()

    print(f"✅ Nombre actualizado de '{nombre_anterior}' a '{nuevo_nombre}'.")
    pausar()


def eliminar_estudiante():
    """
    Elimina un estudiante del sistema después de confirmar la operación.
    """
    limpiar_pantalla()
    mostrar_encabezado()
    print("--- ELIMINAR ESTUDIANTE ---\n")

    estudiante = seleccionar_estudiante()
    if estudiante is None:
        pausar()
        return

    confirmacion = input(
        f"¿Está seguro de eliminar a '{estudiante['nombre']}'? (s/n): "
    ).strip().lower()

    if confirmacion == "s":
        estudiantes.remove(estudiante)
        guardar_datos()
        print("✅ Estudiante eliminado correctamente.")
    else:
        print("ℹ Operación cancelada.")

    pausar()


def guardar_manualmente():
    """
    Guarda la información de forma manual cuando el usuario lo solicite desde el menú.
    """
    limpiar_pantalla()
    mostrar_encabezado()
    print("--- GUARDAR DATOS ---\n")

    guardar_datos()
    print("✅ Datos guardados correctamente en el archivo JSON.")
    pausar()


def main():
    """
    Función principal del sistema.

    Controla el flujo general del programa mediante un ciclo repetitivo.
    Cada opción del menú dirige a una funcionalidad específica.
    """
    cargar_datos()

    while True:
        mostrar_menu()
        opcion = leer_entero("Seleccione una opción (1-9): ", 1, 9)

        if opcion == 1:
            registrar_estudiante()
        elif opcion == 2:
            agregar_nota()
        elif opcion == 3:
            ver_notas_estudiante()
        elif opcion == 4:
            ver_todos_estudiantes()
        elif opcion == 5:
            mostrar_mejor_estudiante()
        elif opcion == 6:
            editar_nombre_estudiante()
        elif opcion == 7:
            eliminar_estudiante()
        elif opcion == 8:
            guardar_manualmente()
        elif opcion == 9:
            guardar_datos()
            limpiar_pantalla()
            print("✅ Datos guardados.")
            print("👋 Gracias por usar el Sistema de Gestión de Notas.")
            print("Autor: CESAR ANDRÉS CHARI GUAMAN")
            break


if __name__ == "__main__":
    main()
