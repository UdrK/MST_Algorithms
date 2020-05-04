#!/usr/bin/env pypy

import txt_reader
import algorithms
import os
import time

directory_name = 'mst_dataset'

file_names = []
times_prim = []
times_naive_kruskal = []
times_kruskal = []

weights_prim = []
weights_naive_kruskal = []
weights_kruskal = []

i=1
tot = len(os.listdir(directory_name))
for file in os.listdir(directory_name):
    filename = os.fsdecode(file)
    if filename.endswith(".txt"):
        file_path = os.path.join(directory_name, filename)
        file_names.append(file_path)
        gr = txt_reader.file_to_graph(file_path)    # reading graph from file

        beginning_kruskal = time.time()
        m3, kruskal_weight = algorithms.kruskal(gr)         # Kruskal with union find
        end_kruskal = time.time()

        f_kruskal = open('kruskal_results.txt', 'a+')
        f_kruskal.write('{}, {}, {}\n'.format(filename, end_kruskal-beginning_kruskal, kruskal_weight))
        f_kruskal.close()

        print("kruskal done")

        beginning_prim = time.time()
        m1, prim_weight = algorithms.prim(gr, 1)            # Prim
        end_prim = time.time()

        f_prim = open('prim_results.txt', 'a+')
        f_prim.write('{}, {}, {}\n'.format(filename, end_prim - beginning_prim, prim_weight))
        f_prim.close()

        print("prim done")

        beginning_naive = time.time()
        m2, naive_kruskal_weight = algorithms.naive_kruskal(gr)     # Kruskal naive
        end_naive = time.time()

        f_naive = open('naive_results.txt', 'a+')
        f_naive.write('{}, {}, {}\n'.format(filename, end_naive - beginning_naive, naive_kruskal_weight))
        f_naive.close()

        # checking if the algorithms agree on the MST weight
        print('The algorithms agree {}/{}: {}'.format(i, tot, prim_weight == naive_kruskal_weight == kruskal_weight))
        i+=1





        

