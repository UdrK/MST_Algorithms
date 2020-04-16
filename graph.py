class Graph:
    def __init__(self, V, E):
        self.edges_dict = {}
        self.E = []
        self.V = V
        self.n = len(V)
        for v in V:
            self.edges_dict[v] = {}

        for e in E:
            if e[0] != e[1]:
                if e[0] in self.edges_dict and e[1] in self.edges_dict[e[0]]:
                    if e[2] < self.edges_dict[e[0]][e[1]]:
                        self.edges_dict[e[0]][e[1]] = e[2]
                        self.edges_dict[e[1]][e[0]] = e[2]

                        for i in range(0, len(self.E)):
                            if (self.E[i][0] == e[0] and self.E[i][1] == e[1]) or (self.E[i][0] == e[1] and self.E[i][1] == e[0]):
                                self.E[i][2] = e[2]
                                break
                else:
                    self.E.append([e[0], e[1], e[2]])
                    self.edges_dict[e[0]][e[1]] = e[2]
                    self.edges_dict[e[1]][e[0]] = e[2]

    def adjacents(self, v):
        return self.edges_dict[v].keys()

    def weight(self, u, v):
        return self.edges_dict[u][v]
