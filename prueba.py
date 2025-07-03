
tareas_archivo = "tareas.txt"
tareas = []

def cargar_tareas():
    """Carga las tareas de el arcivo al inicio del programa."""
    try:
        whith open(tareas_archivo, 'r') as f:
        for linea in f:
            tarea_info = linea.strip().split(',')
            if len(tarea_info)==2:
            descripcion,estado = tarea_info
            tareas.append({'descripccion':descripcion, 'completada': estado == 'True'})
        else:
            tareas.append({'descripcion': tarea_info[0], 'completada': False})
        except FileNotFoundError:
print("No se encontro el archivo de tareas. iniciando con una lista vacia")
pass # El archivo no existe aun, no hay problema

def guardar_tareas():
    """Guarda las tareas en el archivo."""
    with open(tareas_archivo, 'w') as f:
        for tarea in tareas:
            f.write(f"{tarea['descripcion']},{tarea['completada']}\n")
                        
def mostrar_menu():
    """muestra las opciones disponibles del usuario"""
    print("\n--- Gestor de tareas ---")
    print("1. Anadir tarea")
    print("2. ver tareas")
    print("3. marcar tarea completada")
    print("4. Eliminar tarea")
    print("5. Salir")
    print("-----------------------------------------------")
def anadir_tarea():
    """permite al usuario anadir una nueva tarea."""
    descripcion = input("introduce la descripcion de la tarea: ")
    tareas.append({'descripcion': descripcion, 'completada': False})
    print(f"Tarea '{descripcion}' anadida.")

def ver_tareas():
    """Muestra todas la tareas, indicando su estado"""
    if not tareas:
        print("No hay tareas pendientes.")
        return
    print("\n--- Tus Tareas ---")
    for i, tarea in enumerate(tareas):
        estado = "hecha" if tarea['completada'] else "pendiente" print(f"{i + 1}. {estado} {tarea['descripcion']}")
        print("---------------------------------------------")

def marcar_completada():
    """Marcar una tarea existente como completada."""
    ver_tareas()
    if not tareas:
        return
try:
    num_tarea = int(input("introduce el numero de la tarea a marcar como completada: "))-1
    if 0 <= num_tarea < len(tareas):
        tareas[num_tarea]['completada'] = True
        print(f"tarea '{tareas[num_tarea]['descripcion']}' marcada como completada.")
    else:
        print("Numero de tarea no valido")
except ValueError:
        print("Entrada invalida. Por favor introduce un numero")

def eliminar_tarea():
    """Elimina una tarea de la lista"""
    ver_tareas()
    if not tareas:
        return
try:
    num_tarea = int (input("Introduce el numerode la tarea a eliminar: "))-1
    if 0 <= num_tarea < len(tareas):
        tarea_eliminada = tareas.pop(num_tarea)
        print(f"Tarea '{tarea_eliminada['descripcion']}' eliminada.")
    else:
        print("Numero de tarea no valido")
except ValueError:
print("Entrada invalida, por favor introduce un numero")

def main():
    """Funcion principal del progrma"""
    cargar_tareas()
    while true:
        mostrar_menu()
        opcion = input("Elige una opcion: ")
        if opcion == '1':
            anadir_tarea()
        elif opcion == '2':
            ver_tareas()
        elif opcion == '3':
            marcar_completada()
        elif opcion == '4':
            eliminar_tarea()
        elif opcion == '5':
            guardar_tareas()
            print('saliendo del gestor de tareas, hasta luego!')
            break
        else:
            print("opcion no valida, por favor elije una opcion del 1 al 5")
if __name__ == "__main__":
    main()