import math

class Graph:
    def __init__(self, V, E):
        self.V = V
        self.E = E

    def adjacents(self, v):
        adjacents = []
        for e in self.E:
            if v == e[0] and v != e[1] and e[1] not in adjacents:
                adjacents.append(e[1])
            elif v == e[1] and v != e[0] and e[0] not in adjacents:
                adjacents.append(e[0])
        return adjacents

    def weight(self, u, v):
        for e in self.E:
            if e[0] == u and e[1] == v:
                return e[2]
            elif e[0] == v and e[1] == u:
                return e[2]
        return math.inf

    def print_graph(self):
        print('{} {}'.format(len(self.V), len(self.E)))
        for e in self.E:
            print('{} {} {}'.format(e[0], e[1], e[2]))
