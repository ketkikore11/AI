class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    def kruskal_mst(self):
        result = []
        self.edges = sorted(self.edges, key=lambda x:x[2])
        parent = [i for i in range(self.V)]

        for u, v, weight in self.edges:
            parent_u = self.find_parent(parent, u)
            parent_v = self.find_parent(parent, v)

            if parent_u!= parent_v:
                result.append((u, v, weight))
                parent[parent_u] = parent_v
        print("output")
        print("Edge \tWeight")
        for u, v, weight in result:
            print(u, "-", v, "\t", weight)

# Driver code
vertices = int(input("Enter the number of vertices: "))
edges = int(input("Enter the number of edges: "))

g = Graph(vertices)

print("Enter the edges and their weights (u v weight):")
for _ in range(edges):
    u, v, weight = map(int, input().split())
    g.add_edge(u, v, weight)

g.kruskal_mst()


#output
Enter the number of vertices: 5
Enter the number of edges: 6
Enter the edges and their weights (u v weight):
0 1 2
0 2 1
1 3 2
3 4 1
3 2 2
2 4 1
Edge    Weight
0 - 2    1    
3 - 4    1    
2 - 4    1    
0 - 1    2 
