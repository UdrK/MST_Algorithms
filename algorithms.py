from heap import Heap
import math

def prim(g, s):
    MST = []
    MST_weight = 0
    heap = Heap()

    for v in g.V:
        if v == s:
            heap.insert([0, v])
            MST.append(0)
        else:
            heap.insert([math.inf, v])
            MST.append(-1)

    while heap.is_empty() == False:
        u = heap.pop()[1]
        u_adjacents = g.adjacents(u)
        for v in u_adjacents:
            v_position = heap.contains(v)
            if v_position >= 0: # if v_position == -1 then heap doesn't contain v, i need the position to delete the node
                u_v_weight = g.weight(u, v) # returns math.inf if no edge is found, however at this point we know there is one
                if u_v_weight < heap.key(v_position):
                    MST[v-1] = u
                    heap.delete(v_position)
                    heap.insert([u_v_weight, v])

    for i in range(0, len(MST)):
        if not MST[i] == 0:
            MST_weight += g.edges_dict[i+1][MST[i]]

    return MST, MST_weight

def naive_kruskal(g):
    aux_vertices_dict = {}
    MST = []
    MST_weight = 0
    heap = Heap()
    for e in g.E:
        heap.insert([e[2], [e[0], e[1]]])

    done = False
    while not done:
        aux_edge = heap.pop()
        edge = [aux_edge[1][0], aux_edge[1][1], aux_edge[0]]
        if not edge[0] == edge[1]:
            if not(edge[0] in aux_vertices_dict and edge[1] in aux_vertices_dict): # if acyclic (doesn't work)
                aux_vertices_dict[edge[0]] = 1
                aux_vertices_dict[edge[1]] = 1

                MST_weight += edge[2]
                MST.append(edge)
            if len(MST) == g.n-1 or heap.is_empty():
                done = True
    return MST, MST_weight

def kruskal(g):
    pass
