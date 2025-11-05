import heapq

def dijkstra(graph, start):
    # Distance dictionary, initialized to infinity
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    pq = [(0, start)]  # (distance, node)

    while pq:
        curr_dist, node = heapq.heappop(pq)

        if curr_dist > dist[node]:
            continue

        for neighbour, travel_time in graph[node]:
            new_dist = curr_dist + travel_time

            if new_dist < dist[neighbour]:
                dist[neighbour] = new_dist
                heapq.heappush(pq, (new_dist, neighbour))
    
    return dist


# -------- Example Graph (Time to travel between locations) --------
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('E', 2)],
    'E': [('C', 10), ('D', 2)]
}

source = 'A'

result = dijkstra(graph, source)

print(f"Minimum delivery time starting from {source}:")
for location in result:
    print(f"{location} : {result[location]} minutes")