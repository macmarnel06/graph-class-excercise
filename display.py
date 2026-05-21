"""Formato de salida para la consola (proporcionado por la plantilla).

Convierte las respuestas crudas del servidor en mensajes legibles, según
la tabla de la SECCIÓN 6 del SPEC:

    | 200, optimal=true   | Entregado y óptimo — vas al leaderboard.
    | 200, optimal=false  | Entregado pero no es la ruta más corta.
    | 400 "no directed.." | Enlace roto: una arista del path no existe.
    | 400 otros           | Cuerpo de submisión mal formado.
"""

_BAR = "-" * 60


def print_checkin(status, payload):
    print(_BAR)
    print(" CHECK-IN")
    print(_BAR)
    if status == 200 and payload.get("ok"):
        neighbors = payload.get("neighbors", [])
        node_count = payload.get("node_count")
        print(f"  Conexión OK. Nodos totales en el servidor: {node_count}")
        if neighbors:
            print("  Tus vecinos de salida (según el servidor):")
            for n in neighbors:
                print(f"    -> {n}")
        else:
            print("  El servidor reporta que no tienes vecinos de salida.")
    else:
        error = payload.get("error", payload)
        print(f"  FALLO de check-in (status={status}): {error}")
    print()


def print_submit(status, payload, path):
    print(_BAR)
    print(" SUBMIT")
    print(_BAR)
    print("  Path enviado:")
    print("    " + " -> ".join(path))
    print()

    if status == 200 and payload.get("ok"):
        cost = payload.get("cost")
        hops = payload.get("hops")
        optimal_cost = payload.get("optimal_cost")
        if payload.get("optimal"):
            rank = payload.get("rank")
            print(f"  [OK] Entregado y OPTIMO. costo={cost}, saltos={hops}.")
            print(f"  Posicion en el leaderboard: #{rank}")
        else:
            print(f"  [OK] Entregado, pero NO es la ruta mas corta.")
            print(f"       Tu costo={cost} (saltos={hops}); costo optimo={optimal_cost}.")
            print("       Edita compute_path y vuelve a correr.")
    else:
        error = payload.get("error", payload)
        if isinstance(error, str) and error.startswith("no directed edge"):
            print(f"  [FAIL] ENLACE ROTO: {error}")
            print("         Un salto de tu path no es una arista dirigida real.")
            print("         Revisa la direccion de las aristas.")
        else:
            print(f"  [FAIL] Submision mal formada (status={status}): {error}")
    print()
