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
        gr = txt_reader.file_to_graph(file_path)

        beginning_prim = time.time()
        m1, prim_weight = algorithms.prim(gr, 1)
        end_prim = time.time()


        beginning_naive = time.time()
        m2, naive_kruskal_weight = algorithms.naive_kruskal(gr)
        end_naive = time.time()
        
        beginning_kruskal = time.time()
        m3, kruskal_weight = algorithms.kruskal(gr)
        end_kruskal = time.time()

        print('The algorithms agree {}/{}: {}'.format(i, tot, prim_weight == naive_kruskal_weight == kruskal_weight)) # == naive_kruskal_weight
        i+=1

        f_prim = open('prim_results.txt', 'a+')
        f_prim.write('{}, {}, {}\n'.format(filename, end_prim - beginning_prim, prim_weight))
        f_prim.close()


        f_prim = open('naive_results.txt', 'a+')
        f_prim.write('{}, {}, {}\n'.format(filename, end_naive - beginning_naive, naive_kruskal_weight))
        f_prim.close()
        

        f_prim = open('kruskal_results.txt', 'a+')
        f_prim.write('{}, {}, {}\n'.format(filename, end_kruskal-beginning_kruskal, kruskal_weight))
        f_prim.close()
