from collections import deque

# Representing the Graph using an Adjacency List based on CANONIGO
# Repeated letters are treated as separate vertices / nodes
graph = {
    'C': ['A', 'N1'],
    'A': ['C', 'O1', 'N2'],
    'N1': ['C', 'G'],
    'O1': ['A', 'N2'],
    'N2': ['A', 'O1', 'I'],
    'I': ['N2'],
    'G': ['N1', 'O2'],
    'O2': ['G']
}


# Breadth-First Search (BFS) Algorithm for Graph
def bfs_graph(start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # Clean display mapping original letters (ignoring numbers used to tell duplicates apart)
    display_result = [node[0] for node in result]
    print("Graph BFS Result:", " - ".join(display_result))


# Depth-First Search (DFS) Algorithm for Graph
def dfs_graph(start_node):
    visited = set()
    stack = [start_node]
    result = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)

            # Push neighbors in reverse order to explore left/primary paths first
            for neighbor in reversed(graph.get(vertex, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    display_result = [node[0] for node in result]
    print("Graph DFS Result:", " - ".join(display_result))


if __name__ == "__main__":
    print("--- GRAPH TRAVERSAL (CANONIGO) ---")
    bfs_graph('C')
    dfs_graph('C')