from collections import deque

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, vertex, neighbor):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
        self.adjacency_list[vertex].append(neighbor)

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        traversal = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                traversal.append(vertex)
                neighbors = self.adjacency_list.get(vertex, [])
                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return traversal

# Function to convert alphabet to integer
def alphabet_to_integer(char):
    return ord(char.upper()) - ord('A') + 1

# Function to convert integer to alphabet
def integer_to_alphabet(num):
    return chr(num + ord('A') - 1)

# Create graph from user input
graph = Graph()
num_edges = int(input("Enter the number of edges: "))

for _ in range(num_edges):
    vertex, neighbor = input("Enter vertex and its neighbor separated by space: ").split()
    vertex = alphabet_to_integer(vertex)
    neighbor = alphabet_to_integer(neighbor)
    graph.add_edge(vertex, neighbor)

start_vertex = input("Enter the starting vertex: ")
start_vertex = alphabet_to_integer(start_vertex)
bfs_traversal = graph.bfs(start_vertex)
bfs_traversal = [integer_to_alphabet(vertex) for vertex in bfs_traversal]
print("BFS Traversal starting from vertex", integer_to_alphabet(start_vertex), ":", bfs_traversal)
