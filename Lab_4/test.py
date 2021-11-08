from dijkstra_algorithm import Graph, Vertex
import unittest


class TestDijkstraAlgorithm(unittest.TestCase):
    def setUp(self):
        a = Vertex("A")
        b = Vertex("B")
        c = Vertex("C")
        d = Vertex("D")
        e = Vertex("E")
        f = Vertex("F")
        g = Vertex("G")
        h = Vertex("H")
        i = Vertex("I")

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

        vertexes = [a, b, c, d, e, f, g, h, i]
        self.graph = Graph()
        for vertex in vertexes:
            self.graph.add_vertex(vertex)

    def test_vertex_a(self):
        projected_result = {"A": 0, "B": 4, "C": 12, "D": 19, "E": 21, "F": 11, "G": 9, "H": 8, "I": 14}
        self.assertDictEqual(self.graph.dijkstra_algorithm("A"), projected_result)

    def test_vertex_b(self):
        projected_result = {"A": 4, "B": 0, "C": 8, "D": 15, "E": 22, "F": 12, "G": 12, "H": 11, "I": 10}
        self.assertDictEqual(self.graph.dijkstra_algorithm("B"), projected_result)

    def test_vertex_c(self):
        projected_result = {"A": 12, "B": 8, "C": 0, "D": 7, "E": 14, "F": 4, "G": 6, "H": 7, "I": 2}
        self.assertDictEqual(self.graph.dijkstra_algorithm("C"), projected_result)

    def test_vertex_d(self):
        projected_result = {"A": 19, "B": 15, "C": 7, "D": 0, "E": 9, "F": 11, "G": 13, "H": 14, "I": 9}
        self.assertDictEqual(self.graph.dijkstra_algorithm("D"), projected_result)

    def test_vertex_e(self):
        projected_result = {"A": 21, "B": 22, "C": 14, "D": 9, "E": 0, "F": 10, "G": 12, "H": 13, "I": 16}
        self.assertDictEqual(self.graph.dijkstra_algorithm("E"), projected_result)

    def test_vertex_f(self):
        projected_result = {"A": 11, "B": 12, "C": 4, "D": 11, "E": 10, "F": 0, "G": 2, "H": 3, "I": 6}
        self.assertDictEqual(self.graph.dijkstra_algorithm("F"), projected_result)

    def test_vertex_g(self):
        projected_result = {"A": 9, "B": 12, "C": 6, "D": 13, "E": 12, "F": 2, "G": 0, "H": 1, "I": 6}
        self.assertDictEqual(self.graph.dijkstra_algorithm("G"), projected_result)

    def test_vertex_h(self):
        projected_result = {"A": 8, "B": 11, "C": 7, "D": 16, "E": 13, "F": 3, "G": 1, "H": 0, "I": 7}
        self.assertDictEqual(self.graph.dijkstra_algorithm("H"), projected_result)

    def test_vertex_i(self):
        projected_result = {"A": 14, "B": 10, "C": 2, "D": 9, "E": 16, "F": 6, "G": 6, "H": 7, "I": 0}
        self.assertDictEqual(self.graph.dijkstra_algorithm("I"), projected_result)
