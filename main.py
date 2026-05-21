"""
main.py — punto de entrada de la plantilla del ejercicio de ruteo.

Ciclo de vida (fijo, definido por el SPEC):
    1. Cargar `class_graph.json` desde el disco.
    2. POST /api/checkin para confirmar conectividad e imprimir vecinos.
    3. Llamar a `student.compute_path(...)` para calcular la ruta.
    4. POST /api/submit con la ruta calculada.
    5. Imprimir la respuesta del servidor.

Tú sólo necesitas:
  - editar `STUDENT_ID` y `TEACHER_HOST` en `config.py`,
  - implementar `compute_path` en `student.py`.
"""
import json
import os
import sys

import api
import config
import display
import graph
import student

GRAPH_FILE = "topology.json"


def main():
    graph_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        GRAPH_FILE,
    )

    try:
        adjacency, _raw = graph.load_graph(graph_path)
    except FileNotFoundError:
        print(f"error: no se encontro {GRAPH_FILE} junto a main.py")
        return 1
    except (json.JSONDecodeError, KeyError) as e:
        print(f"error: {GRAPH_FILE} esta mal formado: {e}")
        return 1

    print(f"Grafo cargado: {len(adjacency)} nodos.")
    print(f"Tu id: {config.STUDENT_ID}    Profesor: {config.TEACHER_ID}")
    print()

    # 1) Check-in
    status, payload = api.checkin(config.TEACHER_HOST, config.STUDENT_ID)
    display.print_checkin(status, payload)
    if status != 200 or not payload.get("ok"):
        print("Abortando: el check-in fallo.")
        return 1

    # 2) Calcular la ruta (responsabilidad del estudiante)
    try:
        path = student.compute_path(adjacency, config.STUDENT_ID, config.TEACHER_ID)
    except NotImplementedError:
        print("compute_path aun no esta implementado — abre student.py y completalo.")
        return 1
    except Exception as e:
        print(f"compute_path lanzo una excepcion: {type(e).__name__}: {e}")
        return 1

    if not isinstance(path, list) or not all(isinstance(n, str) for n in path):
        print(f"compute_path debe retornar list[str]; retorno: {path!r}")
        return 1

    # 3) Enviar
    status, payload = api.submit(config.TEACHER_HOST, config.STUDENT_ID, path)
    display.print_submit(status, payload, path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
