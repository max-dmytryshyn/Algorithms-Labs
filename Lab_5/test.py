from prims_algorithm import Vertex, UndirectedGraph
import unittest


class TestPrimsAlgorithm(unittest.TestCase):
    def setUp(self):
        # first test graph
        self.undirected_graph_1 = UndirectedGraph()
        vertex_a1 = Vertex("A")
        vertex_b1 = Vertex("B")
        vertex_c1 = Vertex("C")
        vertex_d1 = Vertex("D")
        self.undirected_graph_1.add_vertexes(vertex_a1, vertex_b1, vertex_c1, vertex_d1)
        self.undirected_graph_1.add_edge(vertex_a1, vertex_b1, 1)
        self.undirected_graph_1.add_edge(vertex_a1, vertex_c1, 3)
        self.undirected_graph_1.add_edge(vertex_a1, vertex_d1, 4)
        self.undirected_graph_1.add_edge(vertex_b1, vertex_c1, 2)
        self.undirected_graph_1.add_edge(vertex_c1, vertex_d1, 5)

        # second test graph
        self.undirected_graph_2 = UndirectedGraph()
        vertex_a2 = Vertex("A")
        vertex_b2 = Vertex("B")
        vertex_c2 = Vertex("C")
        vertex_d2 = Vertex("D")
        vertex_e2 = Vertex("E")
        vertex_f2 = Vertex("F")
        self.undirected_graph_2.add_vertexes(vertex_a2, vertex_b2, vertex_c2, vertex_d2, vertex_e2, vertex_f2)
        self.undirected_graph_2.add_edge(vertex_a2, vertex_b2, 3)
        self.undirected_graph_2.add_edge(vertex_a2, vertex_c2, 1)
        self.undirected_graph_2.add_edge(vertex_a2, vertex_d2, 6)
        self.undirected_graph_2.add_edge(vertex_b2, vertex_c2, 5)
        self.undirected_graph_2.add_edge(vertex_b2, vertex_e2, 3)
        self.undirected_graph_2.add_edge(vertex_c2, vertex_d2, 5)
        self.undirected_graph_2.add_edge(vertex_c2, vertex_e2, 6)
        self.undirected_graph_2.add_edge(vertex_c2, vertex_f2, 4)
        self.undirected_graph_2.add_edge(vertex_d2, vertex_f2, 2)
        self.undirected_graph_2.add_edge(vertex_e2, vertex_f2, 6)

    def test_prim_1(self):
        self.assertEqual(self.undirected_graph_1.prims_algorithm(), 7)

    def test_prim_2(self):
        self.assertEqual(self.undirected_graph_2.prims_algorithm(), 13)

