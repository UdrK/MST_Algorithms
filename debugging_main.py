import txt_reader
import algorithms

graph_path = 'mst_dataset/input_random_03_10.txt'
g = txt_reader.file_to_graph(graph_path)
g.print_graph()
print('-----------')
mst = algorithms.prim(g, 4)
print(mst)