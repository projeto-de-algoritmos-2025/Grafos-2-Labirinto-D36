import heapq
from settings import *

def get_neighbors(node, grid_obj):
    neighbors = []
    rows, cols = len(grid_obj.grid), len(grid_obj.grid[0])
    r, c = node
    
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        
        if 0 <= nr < rows and 0 <= nc < cols:
            terrain_type = grid_obj.grid[nr][nc]['type']
            if terrain_type != "wall":
                neighbors.append((nr, nc))
    return neighbors

def dijkstra(grid_obj, start, end):
    if (not start or not end or 
        grid_obj.grid[start[0]][start[1]]['type'] == "wall" or 
        grid_obj.grid[end[0]][end[1]]['type'] == "wall"):
        return [], {}

    distances = { (r, c): float('inf') for r, row in enumerate(grid_obj.grid) for c, val in enumerate(row) }
    predecessors = {}
    
    distances[start] = 0
    priority_queue = [(0, start)]
    visited_nodes = set()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue
        
        if current_node in visited_nodes:
            continue
        
        visited_nodes.add(current_node)

        if current_node == end:
            break 
            
        for neighbor in get_neighbors(current_node, grid_obj):
            terrain = grid_obj.grid[neighbor[0]][neighbor[1]]['type']
            weight = TERRAIN_WEIGHTS.get(terrain, 1) 
            
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
                
    if end not in predecessors:
        return [], visited_nodes
        
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessors.get(current)
    
    path.reverse() 

    if path[0] == start:
        return path, visited_nodes
    else:
        return [], visited_nodes