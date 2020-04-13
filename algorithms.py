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
                    MST_weight += u_v_weight
                    heap.delete(v_position)
                    heap.insert([u_v_weight, v])
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
        if not edge[1] in aux_vertices_dict: # if edge doesn't make it cyclic
            aux_vertices_dict[edge[1]] = edge[0]
            MST_weight += edge[2]
            MST.append(edge)
        if len(MST) == g.n-1:
            done = True
    return MST, MST_weight

def kruskal(g, s):
    pass
