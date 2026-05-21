"""
student.py — tu trabajo.

Implementa la función `compute_path` para encontrar una ruta MÁS CORTA
desde tu nodo hasta el nodo del profesor en el grafo de la clase.

Este es el único archivo que necesitas editar (además de los valores
STUDENT_ID y TEACHER_HOST en config.py).
"""


def compute_path(graph, student_id, teacher_id):
    """
    Devuelve una lista ordenada de ids de nodos representando una ruta
    de costo mínimo desde `student_id` hasta `teacher_id`.

    Ejemplo de retorno válido:
        ["ang25525", "rtr11004", "rtr11007", "rtr11001", "arr11463"]

    El grafo es DIRIGIDO y de pesos POSITIVOS. La ruta debe:
      - empezar en `student_id` y terminar en `teacher_id`,
      - usar sólo aristas dirigidas reales (cada par consecutivo debe
        ser una arista existente en `graph`),
      - tener peso total mínimo (cualquier ruta de costo mínimo se acepta).

    Parameters
    ----------
    graph : dict[str, list[tuple[str, int]]]
        Mapa de adyacencia: `nodo -> [(vecino, peso), ...]`.
        Sólo aparecen aristas que salen de `nodo` (dirigidas).
    student_id : str
        Id del nodo origen (tú).
    teacher_id : str
        Id del nodo destino (el profesor, `TEACHER_ID`).

    Returns
    -------
    list[str]
        Lista de ids del path, en orden, desde `student_id` a `teacher_id`.
    """
    # TODO: implementar el algoritmo de ruta más corta.
    raise NotImplementedError("Implementa compute_path en student.py")
