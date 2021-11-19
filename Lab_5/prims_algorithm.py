import heapq


class Edge:
    def __init__(self, start, destination, weight=0):
        self.start = start
        self.destination = destination
        self.weight = weight


class UndirectedEdge:
    def __init__(self, first_vertex, second_vertex, weight=0):
        self.first_vertex = first_vertex
        self.second_vertex = second_vertex
        self.weight = weight


class Vertex:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.edges = {}

    def set_edge(self, destination, weight=0):
        self.edges[destination.name] = Edge(self, destination, weight)

    def __lt__(self, other):
        return self.name < other.name


class UndirectedGraph:
    def __init__(self):
        self.vertexes = {}
        self.edges = []

    def add_vertexes(self, *vertexes):
        for vertex in vertexes:
            self.vertexes[vertex.name] = vertex

    def add_edge(self, first_vertex, second_vertex, weight):
        if first_vertex.name not in self.vertexes.keys() or second_vertex.name not in self.vertexes.keys():
            raise KeyError()

        self.edges.append(UndirectedEdge(first_vertex, second_vertex, weight))
        self.vertexes[first_vertex.name].set_edge(second_vertex, weight)
        self.vertexes[second_vertex.name].set_edge(first_vertex, weight)

    def prims_algorithm(self):
        minimum_cost = 0
        start_vertex = list(self.vertexes.values())[0]
        visited = {vertex_name: False for vertex_name in self.vertexes.keys()}

        queue = []
        heapq.heappush(queue, (0, self.vertexes[start_vertex.name]))
        while queue:
            current_cost, cur_vertex = heapq.heappop(queue)
            if visited[cur_vertex.name]:
                continue
                
            visited[cur_vertex.name] = True
            minimum_cost += current_cost

            for edge in cur_vertex.edges.values():
                if not visited[edge.destination.name]:
                    heapq.heappush(queue, (edge.weight, edge.destination))

        return minimum_cost


if __name__ == "__main__":
    undirected_graph = UndirectedGraph()
    A = Vertex("A")
    B = Vertex("B")
    C = Vertex("C")
    D = Vertex("D")
    undirected_graph.add_vertexes(A, B, C, D)
    undirected_graph.add_edge(A, B, 1)
    undirected_graph.add_edge(A, C, 3)
    undirected_graph.add_edge(A, D, 4)
    undirected_graph.add_edge(B, C, 2)
    undirected_graph.add_edge(C, D, 5)
    print(undirected_graph.prims_algorithm())
