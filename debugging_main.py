#!/usr/bin/env pypy

import txt_reader
import algorithms
import os
import time

directory_name = 'mst_dataset'

graphs = []
file_names = []
times = []
weights = []

i = 1
for file in os.listdir(directory_name):
    if i<20:
        filename = os.fsdecode(file)
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_name, filename)
            file_names.append(file_path)
            gr = txt_reader.file_to_graph(file_path)
            beginning = time.time()

            m1, prim_weight = algorithms.prim(gr, 6)
            m2, kruskal_weight = algorithms.kruskal(gr)
            m3, naive_kruskal_weight = algorithms.naive_kruskal(gr)

            print("-----------------------------------------------------------------")
            print("prim_weight {}".format(prim_weight))
            print("kruskal_weight {}".format(kruskal_weight))
            print("naive_kruskal_weight {}".format(naive_kruskal_weight))
            print(prim_weight == kruskal_weight == naive_kruskal_weight)
            print("-----------------------------------------------------------------")
            end = time.time()

            i += 1
            times.append(end - beginning)


"""
f = open('naive_kruskal_times.txt', 'w+')
for t, fn, w in zip(times, file_names, weights):
    f.write('{}, {}, {}\n'.format(fn, t, w))

"""