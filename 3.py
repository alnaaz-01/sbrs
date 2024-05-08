class Graph:
    def __init__(self):
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def find(self, root, i):
        if root[i] != i:
            root[i] = self.find(root, root[i])
        return root[i]

    def union(self, root, rank, x, y):
        xroot = self.find(root, x)
        yroot = self.find(root, y)
        if rank[xroot] < rank[yroot]:
            root[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            root[yroot] = xroot
        else:
            root[yroot] = xroot
            rank[xroot] += 1

    def kruskals(self):
        self.graph.sort(key=lambda x: x[2])
        root = list(range(len(self.graph)))
        rank = [0] * len(self.graph)
        mst = []
        total_cost = 0
        for u, v, w in self.graph:
            x = self.find(root, u)
            y = self.find(root, v)
            if x != y:
                mst.append((u, v, w))
                total_cost += w
                self.union(root, rank, x, y)
        print("Minimum Spanning Tree:")
        for u, v, w in mst:
            print(f"{u} - {v}: {w}")
        print(f"Total cost of MST: {total_cost}")

g = Graph()
num_vertices = int(input("Enter the number of vertices: "))
num_edges = int(input("Enter the number of edges: "))

print("Enter edges in the format 'u v w', where u and v are vertices and w is the weight:")
for _ in range(num_edges):
    u, v, w = map(int, input().split())
    g.add_edge(u, v, w)

g.kruskals()
