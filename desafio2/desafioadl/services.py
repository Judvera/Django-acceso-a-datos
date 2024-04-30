from .models import Tarea, SubTarea

def recupera_tareas_y_subtareas():
    tareas = Tarea.objects.all()
    return list(tareas)

def crear_nueva_tarea(descripcion):
    tarea = Tarea.objects.create(descripcion=descripcion)
    return recupera_tareas_y_subtareas()

def crear_subtarea(tarea_id, descripcion):
    tarea = Tarea.objects.get(id=tarea_id)
    subtarea = SubTarea.objects.create(descripcion=descripcion, tarea=tarea)
    return recupera_tareas_y_subtareas()

def elimina_tarea(tarea_id):
    Tarea.objects.filter(id=tarea_id).delete()
    return recupera_tareas_y_subtareas()

def elimina_subtarea(subtarea_id):
    SubTarea.objects.filter(id=subtarea_id).delete()
    return recupera_tareas_y_subtareas()

def imprimir_en_pantalla(tareas_y_subtareas):
    for tarea in tareas_y_subtareas:
        print(f"[{tarea.id}] {tarea.descripcion}")
        for index, subtarea in enumerate(tarea.subtareas.all(), start=1):
            print(f".... [{index}] {subtarea.descripcion}")
