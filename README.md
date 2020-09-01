# MST_Algorithms

As exercise for the advanced algorithms class i'm taking, i need to implement 3 algorithms that given a graph return a minimum spanning tree over the graph.

The language i've choosen for this exercise is python, the decision is based on the fact that the exercise is thought for groups of 3 students but i've decided to do it on my own, and i prefer speed of development over performances.

The graphs to be used for testing are in the **mst_dataset** folder.

Graphs are represented as a list of vertices and a list of edges, which in turn are a triplet: vertix_1, vertix_2, weight. We are using non oriented graphs.

## What is an MST?

Let a graph G be a couple (V, E) where V is a set of vertices and E is a set of edges, where each edge is a triplet (u, v, w) where u and v are vertices and w is an integer representing the weight of the edge between u and v.

Then, an MST (minimum spanning tree) M is a couple (V', E') such that V' = V and E' is a subset of E such that M is a tree and its weight (the sum of weights of E') is minimum. 

## The algorithms:

The algorithms implemented are:

- Prim's algorithm
- Kruskal's algorithm (without union-find)
- Kruskal's algorithm (with union-find)

All non-trivial data structures (heap for Prim and union-find for Kruskal) have been implemented from scratch.

## Results:

The biggest result: **python is slow**.

Compared to implementations in other languages python's execution time is orders of magnitude bigger.

The second biggest result: **Union-Find is crucial for Kruskal's algorithm**.

Kruskal's algorithm is O(m log(n)) (with n number of vertices, m number of edges) only if implemented using the union-find data structure to determine if a graph is cyclic (has loops). Otherwise, using a naive implementation of mine, it becomes O(mn).

Complete results in report.pdf
