"""Carga y representación del grafo (proporcionado por la plantilla)."""
import json


def load_graph(path):
    """
    Carga `class_graph.json` y devuelve `(adjacency, raw)`.

    `adjacency` es un dict de la forma:
        { nodo: [(vecino, peso), ...], ... }

    Todos los nodos que aparecen como `from` o `to` en `edges` quedan
    como llaves de `adjacency` (los nodos sin aristas de salida tienen
    lista vacía).
    """
    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)

    adjacency = {}
    for edge in raw["edges"]:
        src = edge["from"]
        dst = edge["to"]
        weight = edge["weight"]
        adjacency.setdefault(src, []).append((dst, weight))
        adjacency.setdefault(dst, [])

    return adjacency, raw
