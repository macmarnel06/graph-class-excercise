# Ejercicio de ruteo — plantilla del estudiante

Tu objetivo: calcular la ruta **más corta** desde tu nodo hasta el del profesor en el grafo de la clase, y enviarla al servidor.

## Pasos

1. **Edita `config.py`**
   - `STUDENT_ID` — tu número de carnet (ej. `ang25525`).
   - `TEACHER_HOST` — la IP que anuncia el instructor al inicio de la clase.
   - `TEACHER_ID` ya viene fijo; no lo cambies.

2. **Implementa `compute_path` en `student.py`**
   - Recibe el grafo como `dict[str, list[tuple[str, int]]]` (adyacencia con pesos).
   - Debe retornar una lista de ids: `[STUDENT_ID, ..., TEACHER_ID]`.
   - El grafo es **dirigido** y de pesos **positivos**.

3. **Corre el programa**
   ```
   python3 main.py
   ```
   El programa hace check-in, llama a tu `compute_path` y envía la ruta.
   La respuesta del servidor te dice si tu ruta es válida y si es óptima.

## Reintentos

Si el servidor reporta que tu ruta no es la más corta (o que hay un enlace roto), edita `student.py` y vuelve a correr. No hay límite de intentos.

## Restricciones

- Python 3, **solo librería estándar**. No uses `pip install`.
- No modifiques `main.py`, `api.py`, `graph.py`, `display.py` ni `topology.json`.
