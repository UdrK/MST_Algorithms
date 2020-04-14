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

            # mst, mst_weight = algorithms.kruskal(gr)
            mst, mst_weight = algorithms.naive_kruskal(gr)
            # mst, mst_weight = algorithms.prim(gr, 6)
            weights.append(mst_weight)
            end = time.time()
            print("Done... {}".format(mst_weight))
            i += 1
            times.append(end - beginning)

f = open('naive_kruskal_times.txt', 'w+')
for t, fn, w in zip(times, file_names, weights):
    f.write('{}, {}, {}\n'.format(fn, t, w))