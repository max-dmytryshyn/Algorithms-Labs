from math import inf


class Edge:
    def __init__(self, destination, weight=0):
        if weight < 0:
            raise ValueError
        
        self.destination = destination
        self.weight = weight


class Vertex:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.edges = {}

    def add_edge(self, destination, weight=0):
        self.edges[destination.name] = Edge(destination, weight)


class Graph:
    def __init__(self):
        self.vertexes = {}

    def add_vertex(self, vertex):
        self.vertexes[vertex.name] = vertex

    def dijkstra_algorithm(self, start_vertex_name):
        distances = {vertex_name: inf for vertex_name in self.vertexes.keys()}
        distances[start_vertex_name] = 0
        visited = {vertex_name: False for vertex_name in self.vertexes.keys()}
        visited[start_vertex_name] = True
        
        queue = [self.vertexes[start_vertex_name]]
        while queue:
            cur_vertex = queue.pop(0)
            
            for edge in cur_vertex.edges.values():
                if not visited[edge.destination.name]:
                    visited[edge.destination.name] = True
                    queue.append(edge.destination)
                
                if distances[cur_vertex.name] + edge.weight < distances[edge.destination.name]:
                    distances[edge.destination.name] = distances[cur_vertex.name] + edge.weight

        return distances


if __name__ == "__main__":
    a = Vertex("A")
    b = Vertex("B")
    c = Vertex("C")
    d = Vertex("D")
    e = Vertex("E")
    f = Vertex("F")
    g = Vertex("G")
    h = Vertex("H")
    i = Vertex("I")
    vertexes = [a, b, c, d, e, f, g, h, i]

    a.add_edge(b, 4)
    a.add_edge(h, 8)

    b.add_edge(a, 4)
    b.add_edge(c, 8)
    b.add_edge(h, 11)

    c.add_edge(b, 8)
    c.add_edge(d, 7)
    c.add_edge(f, 4)
    c.add_edge(i, 2)

    d.add_edge(c, 7)
    d.add_edge(e, 9)
    d.add_edge(f, 14)

    e.add_edge(d, 9)
    e.add_edge(f, 10)

    f.add_edge(c, 4)
    f.add_edge(d, 14)
    f.add_edge(e, 10)
    f.add_edge(g, 2)

    g.add_edge(f, 2)
    g.add_edge(h, 1)
    g.add_edge(i, 6)

    h.add_edge(a, 8)
    h.add_edge(b, 11)
    h.add_edge(g, 1)
    h.add_edge(i, 7)

    i.add_edge(c, 2)
    i.add_edge(g, 6)
    i.add_edge(h, 7)

    graph = Graph()
    for vertex in vertexes:
        graph.add_vertex(vertex)

    for vertex in vertexes:
        print("Vertex:", vertex.name)
        for item in graph.dijkstra_algorithm(vertex.name).items():
            print(item[0] + ":", item[1])
        print("----------------------------------")
