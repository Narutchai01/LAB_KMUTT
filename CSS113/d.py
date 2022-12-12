nodes = ('A', 'B', 'C', 'D', 'E')
distances = {   'A': {'B': 19, 'C': 5}, 
                'B': {'A': 19, 'C': 5, 'D': 9, 'E': 2}, 
                'C': {'A': 5,'B': 5, 'D': 1, 'E': 6}, 
                'D': {'B': 9, 'E': 1, 'C': 1}, 
                'E': {'B': 2, 'D': 1, 'C': 6}}

unvisited = {node: None for node in nodes} #using None as +inf
visited = {}
current = str(input('Enter node:')).upper()
currentDistance = 0
unvisited[current] = currentDistance

while True:
    for neighbour, distance in distances[current].items():
        if neighbour not in unvisited: continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited: break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

print(visited)
