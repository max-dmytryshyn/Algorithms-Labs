import heapq
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

    def __lt__(self, other):
        return self.name < other.name


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

        queue = []
        heapq.heappush(queue, (0, self.vertexes[start_vertex_name]))
        while queue:
            cur_vertex = heapq.heappop(queue)[1]

            for edge in cur_vertex.edges.values():
                if distances[cur_vertex.name] + edge.weight < distances[edge.destination.name]:
                    distances[edge.destination.name] = distances[cur_vertex.name] + edge.weight

                if not visited[edge.destination.name]:
                    visited[edge.destination.name] = True
                    heapq.heappush(queue, (distances[edge.destination.name], edge.destination))

        return distances


if __name__ == "__main__":
    graph = Graph()
    input_file = open("./test_input.txt", "r", encoding='utf-8-sig')
    edges_amount, start_vertex = input_file.readline().split()
    edges_amount = int(edges_amount)
    for _ in range(edges_amount):
        edge_start, edge_end, edge_weight = input_file.readline().split()
        if edge_start not in graph.vertexes.keys():
            graph.vertexes[edge_start] = Vertex(edge_start)
        if edge_end not in graph.vertexes.keys():
            graph.vertexes[edge_end] = Vertex(edge_end)
        graph.vertexes[edge_start].add_edge(graph.vertexes[edge_end], float(edge_weight))

    distances = [distance for distance in graph.dijkstra_algorithm(start_vertex).values() if distance != inf]
    print(sum(distances)/(len(distances)-1))
