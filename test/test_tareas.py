import pytest
from tareas import agregar_tarea, actualizar_tarea, marcar_completada, eliminar_tarea, listar_tareas, tareas

def setup_function():
    # Limpia las tareas antes de cada prueba
    tareas.clear()

def test_agregar_tarea():
    agregar_tarea(1, "Estudiar para el examen", "Alta")
    assert tareas[1] == {"descripcion": "Estudiar para el examen", "prioridad": "Alta", "completada": False}

    with pytest.raises(ValueError):
        agregar_tarea(1, "Ir al gimnasio", "Media")  # ID de tarea ya existe

def test_actualizar_tarea():
    agregar_tarea(1, "Estudiar para el examen", "Alta")
    actualizar_tarea(1, "Estudiar para el parcial", "Baja")
    assert tareas[1] == {"descripcion": "Estudiar para el parcial", "prioridad": "Baja", "completada": False}

    with pytest.raises(KeyError):
        actualizar_tarea(2, "Leer un libro", "Media")  # Tarea no existe

def test_marcar_completada():
    agregar_tarea(1, "Estudiar para el examen", "Alta")
    marcar_completada(1)
    assert tareas[1]["completada"] == True

    with pytest.raises(KeyError):
        marcar_completada(2)  # Tarea no existe

def test_eliminar_tarea():
    agregar_tarea(1, "Estudiar para el examen", "Alta")
    eliminar_tarea(1)
    assert 1 not in tareas

    with pytest.raises(KeyError):
        eliminar_tarea(2)  # Tarea no existe

def test_listar_tareas():
    agregar_tarea(1, "Estudiar para el examen", "Alta")
    agregar_tarea(2, "Hacer ejercicio", "Media")
    marcar_completada(2)
    
    pendientes = listar_tareas(completadas=False)
    completadas = listar_tareas(completadas=True)

    assert len(pendientes) == 1
    assert len(completadas) == 1

    assert pendientes[0]["descripcion"] == "Estudiar para el examen"
    assert completadas[0]["descripcion"] == "Hacer ejercicio"
