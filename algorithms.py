from heap import Heap
import math

def prim(g, s):
    MST = []
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
                if u_v_weight < heap.key(v):
                    MST[v-1] = u
                    heap.delete(v_position)
                    heap.insert([u_v_weight, v])
    return MST

def naive_kruskal(g):
    pass

def kruskal(g):
    pass
