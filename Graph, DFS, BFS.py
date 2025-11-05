from collections import deque

# Vertices
vertices = ['A', 'B', 'C', 'D', 'E']
n = len(vertices)

# -------- Adjacency Matrix --------
adj_matrix = [
    [0, 1, 1, 0, 0],  # A -> B, C
    [1, 0, 0, 1, 0],  # B -> A, D
    [1, 0, 0, 1, 1],  # C -> A, D, E
    [0, 1, 1, 0, 0],  # D -> B, C
    [0, 0, 1, 0, 0]   # E -> C
]

# -------- Adjacency List --------
adj_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D', 'E'],
    'D': ['B', 'C'],
    'E': ['C']
}

# -------- DFS Function --------
def dfs(start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbour in adj_list[start]:
        if neighbour not in visited:
            dfs(neighbour, visited)

# -------- BFS Function --------
def bfs(start):
    visited = set([start])
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neighbour in adj_list[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# -------- Execute --------
print("Adjacency Matrix:")
for row in adj_matrix:
    print(row)

print("\nAdjacency List:")
for key, value in adj_list.items():
    print(key, ":", value)

print("\nDFS starting from A:")
dfs('A')

print("\n\nBFS starting from A:")
bfs('A') 