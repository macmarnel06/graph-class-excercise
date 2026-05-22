import heapq

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
