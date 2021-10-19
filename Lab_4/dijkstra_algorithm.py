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


book = Vertex("book")
rare_lp = Vertex("rare lp")
poster = Vertex("poster")
drum_set = Vertex("drum set")
bass_guitar = Vertex("bass guitar")
piano = Vertex("piano")

book.add_edge(rare_lp, 5)
book.add_edge(poster, 0)
rare_lp.add_edge(bass_guitar, 15)
rare_lp.add_edge(drum_set, 20)
poster.add_edge(bass_guitar, 30)
poster.add_edge(drum_set, 35)
drum_set.add_edge(piano, 10)
drum_set.add_edge(poster, 15)
bass_guitar.add_edge(piano, 20)

graph = Graph()
graph.add_vertex(book)
graph.add_vertex(rare_lp)
graph.add_vertex(poster)
graph.add_vertex(drum_set)
graph.add_vertex(bass_guitar)
graph.add_vertex(piano)

for item in graph.dijkstra_algorithm("book").items():
    print(item[0] + ":", item[1])
