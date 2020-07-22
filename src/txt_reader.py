from graph import Graph

def file_to_graph(file_path):
    f = open(file_path, 'r')
    file_lines = f.readlines()

    E = []

    number_of_vertices = int(file_lines[0].split()[0])
    V = [i for i in range(1, number_of_vertices+1)]

    for line in file_lines[1:]:
        E.append([int(e) for e in line.split()])

    f.close()

    g = Graph(V, E)
    return g
