#Ejercicio 8/Nayla Cala/2211870

class Proyecto:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def mostrar_tareas(self):
        print(f"Tareas del proyecto '{self.nombre}':")
        for tarea in self.tareas:
            print(f"- {tarea.descripcion} ({tarea.estado})")

    def generar_informe(self):
        print(f"Informe de progreso del proyecto '{self.nombre}':")
        total_tareas = len(self.tareas)
        tareas_completadas = sum(1 for tarea in self.tareas if tarea.estado == "Completada")
        progreso = tareas_completadas / total_tareas * 100
        print(f"Progreso: {progreso:.2f}%")
        print(f"Tareas completadas: {tareas_completadas}/{total_tareas}")

    def asignar_tarea(self, tarea, miembro):
        for t in self.tareas:
            if t.descripcion == tarea and t.asignado_a == "":
                t.asignado_a = miembro
                return True
        return False


class Tarea:
    def __init__(self, descripcion, estado):
        self.descripcion = descripcion
        self.estado = estado
        self.asignado_a = ""

    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado


class Equipo:
    def __init__(self):
        self.miembros = []

    def agregar_miembro(self, miembro):
        self.miembros.append(miembro)

    def mostrar_miembros(self):
        print("Miembros del equipo:")
        for miembro in self.miembros:
            print(f"- {miembro}")



equipo = Equipo()
equipo.agregar_miembro("Juan")
equipo.agregar_miembro("María")

proyecto = Proyecto("Proyecto de ejemplo", "Descripción del proyecto")

tarea1 = Tarea("Tarea 1", "En progreso")
tarea2 = Tarea("Tarea 2", "Pendiente")
tarea3 = Tarea("Tarea 3", "Completada")

proyecto.agregar_tarea(tarea1)
proyecto.agregar_tarea(tarea2)
proyecto.agregar_tarea(tarea3)

proyecto.asignar_tarea("Tarea 1", "Juan")
proyecto.asignar_tarea("Tarea 2", "María")

proyecto.mostrar_tareas()
proyecto.generar_informe()

equipo.mostrar_miembros()
proyecto.agregar_tarea(Tarea)