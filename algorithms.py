from heap import Heap
from union_find import UnionFind
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

def is_acyclic(edges, new_edge):

    # if i've never encountered one of the 2 vertices in the new edge it can't be cyclic
    if not(new_edge[0] in edges and new_edge[1] in edges):
        return True

    # otherwise it could be cyclic but maybe not
    # list of vertices adjacent to the target vertex
    list_1 = edges[new_edge[1]]

    # list of vertices adjacent to the source vertex, if one of these (or their adjacents) appear in the list of
    # target's adjacent, there's a loop
    list_0 = edges[new_edge[0]].copy()

    checked = []

    while len(list_0) > 0:
        elem = list_0[0]
        if elem in list_1 or elem == new_edge[1]:
            return False
        else:
            for adj in edges[elem]:
                if not adj in list_0 and not adj in checked:
                    list_0.append(adj)

        checked.append(list_0.pop(0))

    return True


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

        if is_acyclic(aux_vertices_dict, edge):
            if not edge[0] in aux_vertices_dict:
                aux_vertices_dict[edge[0]] = []
            if not edge[1] in aux_vertices_dict:
                aux_vertices_dict[edge[1]] = []

            aux_vertices_dict[edge[0]].append(edge[1])
            aux_vertices_dict[edge[1]].append(edge[0])

            MST_weight += edge[2]
            MST.append(edge)

        if len(MST) == g.n-1 or heap.is_empty():
            done = True

    return MST, MST_weight

def kruskal(g):

    MST = []
    MST_weight = 0
    U = UnionFind()
    U.initialize(g.V)

    heap = Heap()
    for e in g.E:
        heap.insert([e[2], [e[0], e[1]]])

    done = False
    while not done:

        aux_edge = heap.pop()
        edge = [aux_edge[1][0], aux_edge[1][1], aux_edge[0]] # original edge format: v1, v2, w
        e0_find = U.find(edge[0])
        e1_find = U.find(edge[1])

        if e0_find != e1_find:
            MST.append(edge)
            MST_weight += edge[2]
            U.union(e0_find, e1_find)

        if len(MST) == g.n-1 or heap.is_empty():
            done = True

    return MST, MST_weight
