# MST_Algorithms
Minimum spanning tree algorithms in python
As exercise for the advanced algorithms class i'm taking, i need to implement 3 algorithms that given a graph return a minimum spanning tree over the graph.

The graphs to be used for testing are in the **mst_dataset** folder.

Graphs are represented as a list of vertices and a list of edges, which in turn are a triplet: vertix_1, vertix_2, weight. We are using non oriented graphs.

The algorithms to be implemented are:

- Prim's algorithm
- Kruskal's algorithm (without union-find)
- Kruskal's algorithm (with union-find)

All non-trivial datastructures (heap for Prim and union-find for Kruskal) have been implemented from scratch.
