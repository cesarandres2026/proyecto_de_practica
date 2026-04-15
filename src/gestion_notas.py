"""
Sistema de Gestión de Notas de Estudiantes
Desarrollado para Aprendizaje Autónomo 2
Autor: [Tu Nombre]
Fecha: 12 de abril de 2026
"""

# Lista global para almacenar todos los estudiantes
estudiantes = []

def mostrar_menu():
    """
    Muestra el menú principal del sistema
    """
    print("\n" + "="*50)
    print("         SISTEMA DE GESTIÓN DE NOTAS")
    print("="*50)
    print("1. Registrar estudiante")
    print("2. Agregar nota a estudiante")
    print("3. Ver notas de un estudiante")
    print("4. Ver todos los estudiantes")
    print("5. Mostrar mejor estudiante")
    print("6. Salir")
    print("="*50)

def registrar_estudiante():
    """
    Registra un nuevo estudiante en el sistema
    Valida que el nombre no esté vacío y no exista previamente
    """
    print("\n--- REGISTRO DE ESTUDIANTE ---")
    
    # Validación estructura lógica: nombre no vacío
    while True:
        nombre = input("Ingrese el nombre del estudiante: ").strip().title()
        if nombre == "":
            print("❌ Error: El nombre no puede estar vacío.")
            continue
        break
    
    # Validación estructura lógica: estudiante no existe
    for estudiante in estudiantes:
        if estudiante["nombre"] == nombre:
            print(f"❌ Error: Ya existe un estudiante llamado '{nombre}'")
            return
    
    # Crear nuevo estudiante con lista vacía de notas
    nuevo_estudiante = {
        "nombre": nombre,
        "notas": []
    }
    estudiantes.append(nuevo_estudiante)
    print(f"✅ Estudiante '{nombre}' registrado exitosamente!")

def agregar_nota():
    """
    Agrega una nota a un estudiante existente
    Valida existencia del estudiante y rango de nota (0-10)
    """
    print("\n--- AGREGAR NOTA ---")
    
    if not estudiantes:
        print("❌ No hay estudiantes registrados.")
        return
    
    # Mostrar estudiantes disponibles
    print("\nEstudiantes disponibles:")
    for i, est in enumerate(estudiantes, 1):
        promedio = calcular_promedio(est["notas"])
        estado = obtener_estado_academico(promedio)
        print(f"{i}. {est['nombre']} - Promedio: {promedio:.2f} ({estado})")
    
    # Validación estructura lógica: selección válida
    while True:
        try:
            opcion = int(input("\nSeleccione el estudiante (número): "))
            if 1 <= opcion <= len(estudiantes):
                estudiante_seleccionado = estudiantes[opcion - 1]
                break
            else:
                print("❌ Opción inválida. Intente nuevamente.")
        except ValueError:
            print("❌ Debe ingresar un número válido.")
    
    # Validación estructura repetitiva: nota en rango 0-10
    while True:
        try:
            nota = float(input(f"Ingrese la nota para {estudiante_seleccionado['nombre']} (0-10): "))
            if 0 <= nota <= 10:
                estudiante_seleccionado["notas"].append(nota)
                print(f"✅ Nota {nota} agregada correctamente!")
                break
            else:
                print("❌ La nota debe estar entre 0 y 10.")
        except ValueError:
            print("❌ Debe ingresar un número válido.")

def ver_notas_estudiante():
    """
    Muestra todas las notas y promedio de un estudiante específico
    Usa estructura repetitiva for para recorrer notas
    """
    print("\n--- VER NOTAS DE ESTUDIANTE ---")
    
    if not estudiantes:
        print("❌ No hay estudiantes registrados.")
        return
    
    # Mostrar estudiantes
    print("\nEstudiantes disponibles:")
    for i, est in enumerate(estudiantes, 1):
        print(f"{i}. {est['nombre']}")
    
    # Validación de selección
    while True:
        try:
            opcion = int(input("\nSeleccione el estudiante (número): "))
            if 1 <= opcion <= len(estudiantes):
                estudiante = estudiantes[opcion - 1]
                break
            else:
                print("❌ Opción inválida.")
        except ValueError:
            print("❌ Debe ingresar un número válido.")
    
    print(f"\n📋 Notas de {estudiante['nombre']}:")
    if not estudiante["notas"]:
        print("No hay notas registradas.")
    else:
        # Estructura repetitiva for para mostrar notas
        for i, nota in enumerate(estudiante["notas"], 1):
            print(f"  Nota {i}: {nota}")
        
        promedio = calcular_promedio(estudiante["notas"])
        estado = obtener_estado_academico(promedio)
        print(f"\n📊 Promedio: {promedio:.2f}")
        print(f"Estado: {estado}")

def ver_todos_estudiantes():
    """
    Muestra todos los estudiantes con sus promedios
    Usa estructura repetitiva for para recorrer lista completa
    """
    print("\n--- LISTA DE TODOS LOS ESTUDIANTES ---")
    
    if not estudiantes:
        print("❌ No hay estudiantes registrados.")
        return
    
    print("\n" + "-"*60)
    print(f"{'N°':<3} {'NOMBRE':<20} {'NOTAS':<15} {'PROMEDIO':<10} {'ESTADO'}")
    print("-"*60)
    
    # Estructura repetitiva for para mostrar todos los estudiantes
    for i, estudiante in enumerate(estudiantes, 1):
        num_notas = len(estudiante["notas"])
        promedio = calcular_promedio(estudiante["notas"])
        estado = obtener_estado_academico(promedio)
        print(f"{i:<3} {estudiante['nombre']:<20} {num_notas:<15} {promedio:<10.2f} {estado}")

def mejor_estudiante():
    """
    Determina el estudiante con mejor promedio
    Usa estructura repetitiva for y condicionales para comparación
    """
    print("\n--- MEJOR ESTUDIANTE ---")
    
    if not estudiantes:
        print("❌ No hay estudiantes registrados.")
        return
    
    mejor_promedio = -1
    mejor_estudiante_nombre = ""
    
    # Estructura repetitiva for con condicional para encontrar máximo
    for estudiante in estudiantes:
        promedio = calcular_promedio(estudiante["notas"])
        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_estudiante_nombre = estudiante["nombre"]
    
    print(f"\n🏆 ¡Felicidades {mejor_estudiante_nombre}!")
    print(f"   Mejor promedio: {mejor_promedio:.2f}")
    print(f"   Estado: {obtener_estado_academico(mejor_promedio)}")

def calcular_promedio(notas):
    """
    Calcula el promedio de una lista de notas
    """
    if not notas:
        return 0.0
    return sum(notas) / len(notas)

def obtener_estado_academico(promedio):
    """
    Determina el estado académico según el promedio
    Implementa estructuras lógicas if-elif-else
    """
    if promedio >= 9.0:
        return "EXCELENTE"
    elif promedio >= 7.0:
        return "APROBADO"
    elif promedio >= 6.0:
        return "RECUPERACIÓN"
    else:
        return "REPROBADO"

def main():
    """
    Función principal que ejecuta el ciclo while del menú
    Estructura repetitiva while para mantener programa activo
    """
    print("¡Bienvenido al Sistema de Gestión de Notas!")
    
    # Estructura repetitiva while para menú principal
    while True:
        mostrar_menu()
        
        # Validación estructura lógica para opción del menú
        while True:
            try:
                opcion = int(input("Seleccione una opción (1-6): "))
                if 1 <= opcion <= 6:
                    break
                else:
                    print("❌ Opción inválida. Debe ser 1-6.")
            except ValueError:
                print("❌ Debe ingresar un número válido.")
        
        # Estructura lógica if-elif para ejecutar funciones
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
            print("\n👋 ¡Gracias por usar el Sistema de Gestión de Notas!")
            print("Desarrollado para Aprendizaje Autónomo 2")
            break
        
        input("\nPresione Enter para continuar...")

# Iniciar el programa
if __name__ == "__main__":
    main()