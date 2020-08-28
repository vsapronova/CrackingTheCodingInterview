

# class Graph:
#     def __init__(self, nodes):
#         self.nodes = nodes
#         self.graph = [None] * self.nodes
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }


def bfs(graph, start_node, end_node):
    if start_node == end_node:
        return True
    visited = []
    queue = []
    visited.append(start_node)
    queue.append(start_node)
    while queue:
        n = queue.pop(0)
        if n == end_node:
            return True
        for node in graph:
            if node not in visited:
                queue.append(node)
                visited.append(node)
    return False

visited = []
def dfs(visited, graph,start, node):
    if start == node:
        return True
    if node not in visited:
       visited.append(node)
       print(node)
       for neighbor in graph:
           dfs(visited, graph, start, neighbor)



# print(bfs(graph, "a", "e"))
dfs(visited, graph, 'a')