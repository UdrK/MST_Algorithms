# heap class based on the description given in
# Introduction to Algorithms by Cormen, Leiserson, Rivest, Stein, third edition.

# it will be used in the Prism's algorithm to find a mst
# therefore each element in the list self.heap will be a list of 2 numbers:
# first: the minimum weight of any edge that connects the vertex to the mst
# second: the vertex

import math

class Heap:
    def __init__(self):
        self.heap = []

    def build_min_heap(self):
        half_way = int(len(self.heap)/2)
        for i in range(0, half_way):
            self.min_heapify(half_way-(i+1))

    def min_heapify(self, index):

        done = False
        while not done:
            left_child = (2*index)+1
            right_child = (2*index)+2
            heap_size = len(self.heap)

            smallest = index

            if left_child < heap_size:
                # self.heap[left_child][0] will access the minimum weight of any edge connecting the vertex
                # to the mst, these values are initially set to +inf by Prism's algorithm
                if self.heap[left_child][0] < self.heap[index][0]:
                    smallest = left_child

            if right_child < heap_size:
                if self.heap[right_child][0] < self.heap[smallest][0]:
                    smallest = right_child

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                done = True

    def insert(self, insertee):
        self.heap.append(insertee)
        self.build_min_heap()

    def pop(self):
        root = self.heap.pop(0)
        if len(self.heap) > 0:
            last = self.heap.pop(-1)
            self.heap.insert(0, last)
            self.build_min_heap()
        return root

    def delete(self, v):
        # when deleting an arbitrary vertex in the heap i need to swap it with the
        # leftmost lowermost leaf in the subtree to keep the tree balanced.
        if v < len(self.heap):
            rightmost_lowest_index = v
            while (2*rightmost_lowest_index)+2 < len(self.heap):
                rightmost_lowest_index = (2*rightmost_lowest_index)+2

            while rightmost_lowest_index+2 < len(self.heap):
                rightmost_lowest_index += 2

            self.heap[v] = self.heap[rightmost_lowest_index]
            del(self.heap[rightmost_lowest_index])
            self.build_min_heap()

    def contains(self, v):
        # is the vertex v in the heap?
        # returns its position, or -1 if not in the heap.
        for i in range(0, len(self.heap)):
            if v == self.heap[i][1]:
                return i
        return -1

    def key(self, v_position):
        # what's the weight associated to v_position?
        # returns math.inf if not in the heap, will be called only if in heap anyway.
        return self.heap[v_position][0]

    def is_empty(self):
        return len(self.heap) == 0

    def print_heap(self):
        for h in self.heap:
            print(h)