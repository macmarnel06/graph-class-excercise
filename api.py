"""Cliente HTTP para el servidor de la clase (proporcionado por la plantilla).

Sólo se usa `urllib` de la stdlib — la red de clase no tiene salida a
internet, así que `pip install requests` no es opción.
"""
import json
import urllib.error
import urllib.request

SERVER_PORT = 5173
_REQUEST_TIMEOUT = 10  # segundos


def checkin(host, student_id):
    """POST /api/checkin — devuelve `(status, payload)`."""
    return _post(f"http://{host}:{SERVER_PORT}/api/checkin",
                 {"student_id": student_id})


def submit(host, student_id, path):
    """POST /api/submit — devuelve `(status, payload)`."""
    return _post(f"http://{host}:{SERVER_PORT}/api/submit",
                 {"student_id": student_id, "path": path})


def _post(url, body):
    """POST JSON. Devuelve `(status_code, parsed_json_body)`.

    Si el servidor responde con error HTTP pero con cuerpo JSON
    (p.ej. `{"ok": false, "error": "..."}`), se devuelve ese cuerpo
    para que el llamador pueda mostrar el mensaje del servidor.
    """
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=_REQUEST_TIMEOUT) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        try:
            payload = json.loads(e.read().decode("utf-8"))
        except (ValueError, UnicodeDecodeError):
            payload = {"ok": False, "error": f"HTTP {e.code} (cuerpo no-JSON)"}
        return e.code, payload
    except urllib.error.URLError as e:
        return 0, {"ok": False, "error": f"no se pudo contactar al servidor: {e.reason}"}
