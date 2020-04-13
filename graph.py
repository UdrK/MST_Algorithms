import math

class Graph:
    def __init__(self, V, E):
        self.V = V
        self.E = E
        self.n = len(V)
        self.m = len(E)
        self.edges_dict = {}
        for v in V:
            self.edges_dict[v] = {}

        for e in E:
            self.edges_dict[e[0]][e[1]] = e[2]

    @staticmethod
    def is_acyclic(E):
        aux_vertices_dict = {}

        for e in E:
            if e[1] in aux_vertices_dict == False:
                aux_vertices_dict[e[1]] = e[0]
            elif aux_vertices_dict[e[1]] != e[0]:
                return False
        return True

    def adjacents(self, v):
        return self.edges_dict[v].keys()

    def weight(self, u, v):
        return self.edges_dict[u][v]

    def print_graph(self):
        print('{} {}'.format(len(self.V), len(self.E)))
        for e in self.E:
            print('{} {} {}'.format(e[0], e[1], e[2]))
