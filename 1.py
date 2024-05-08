class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=' ')

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = set()
        self.dfs_util(start, visited)

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            v = queue.pop(0)
            print(v, end=' ')

            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)


def menu():
    print("\nMenu:")
    print("1. Depth First Search (DFS)")
    print("2. Breadth First Search (BFS)")
    print("3. Exit")


# Example Usage:
if (__name__ == "__main__"):
    g = Graph()
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            num_edges = int(input("Enter the number of edges: "))
            print("Enter the edges (source destination):")
            for _ in range(num_edges):
                edge = input().strip().split()
                source, destination = edge[0], edge[1]
                g.add_edge(source, destination)
            start_vertex = input("Enter the starting vertex for DFS traversal: ")
            print("DFS traversal:")
            g.dfs(start_vertex)
            print()
        elif choice == '2':
            num_edges = int(input("Enter the number of edges: "))
            print("Enter the edges (source destination):")
            for _ in range(num_edges):
                edge = input().strip().split()
                source, destination = edge[0], edge[1]
                g.add_edge(source, destination)
            start_vertex = input("Enter the starting vertex for BFS traversal: ")
            print("BFS traversal:")
            g.bfs(start_vertex)
            print()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please select again.")
