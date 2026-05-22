"""
student.py — tu trabajo.

Implementa la función `compute_path` para encontrar una ruta MÁS CORTA
desde tu nodo hasta el nodo del profesor en el grafo de la clase.

Este es el único archivo que necesitas editar (además de los valores
STUDENT_ID y TEACHER_HOST en config.py).
"""


def compute_path(graph, student_id, teacher_id):
    # Dijkstra
    dist = {student_id: 0}
    prev = {}
    heap = [(0, student_id)]

    while heap:
        d, u = heapq.heappop(heap)
        if d != dist.get(u, float("inf")):
            continue
        if u == teacher_id:
            break
        for v, w in graph.get(u, []):
            nd = d + w
            if nd < dist.get(v, float("inf")):
                dist[v] = nd
                prev[v] = u
                heapq.heappush(heap, (nd, v))

    # Reconstruct path
    if teacher_id not in dist:
        return []  # no path found

    path = []
    cur = teacher_id
    while cur != student_id:
        path.append(cur)
        cur = prev.get(cur)
        if cur is None:
            return []  # safety
    path.append(student_id)
    path.reverse()
    return path


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
   
    
