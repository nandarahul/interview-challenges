#!/bin/python
import sys


class Heap:
    def __init__(self, max_heap=True):
        self.heap_list = [0]
        self.max_heap = max_heap

    def get_length(self):
        return len(self.heap_list)-1

    def get_maxmin(self):
        if len(self.heap_list) == 1:
            raise exception("Heap is Empty")
        return self.heap_list[1]

    def extract_maxmin(self):
        if len(self.heap_list) == 1:
            raise exception("Heap is Empty")
        result = self.heap_list[1]
        self.heap_list[1] = self.heap_list[-1]
        self.heap_list = self.heap_list[:-1]
        self.heapify_down(index=1)
        return result

    def heapify_up(self, index):
        if index < 1 or index >= len(self.heap_list):
            raise exception("invalid index passed")
        parent = index/2
        if parent < 1:
            return
        toswap = (self.max_heap and self.heap_list[index] > self.heap_list[parent]) or (not self.max_heap and
                                                                self.heap_list[index] < self.heap_list[parent])
        if toswap:
            self.heap_list[index], self.heap_list[parent] = self.heap_list[parent], self.heap_list[index]
            self.heapify_up(parent)

    def heapify_down(self, index):
        if index < 1 or index >= len(self.heap_list):
            raise exception("invalid index passed")
        left, right = 2*index, 2*index + 1
        original = index

        if left < len(self.heap_list):
            if self.max_heap and self.heap_list[left] > self.heap_list[index]:
                original = left
            elif not self.max_heap and self.heap_list[left] < self.heap_list[index]:
                original = left
        if right < len(self.heap_list):
            if self.max_heap and self.heap_list[right] > self.heap_list[original]:
                original = right
            elif not self.max_heap and self.heap_list[right] < self.heap_list[original]:
                original = right
        if original != index:
            self.heap_list[original], self.heap_list[index] = self.heap_list[index], self.heap_list[original]
            self.heapify_down(original)

    def insert(self, num):
        self.heap_list.append(num)
        self.heapify_up(index=len(self.heap_list)-1)


class MedianRunner:
    def __init__(self):
        self.L = Heap(max_heap=True)
        self.R = Heap(max_heap=False)

    def getMedian(self):
        if self.L.get_length() == self.R.get_length():
            return (float)(self.L.get_maxmin() + self.R.get_maxmin())/2
        elif self.L.get_length() > self.R.get_length():
            return self.L.get_maxmin()
        return self.R.get_maxmin()

    def insert(self, num):
        if self.L.get_length() == 0 or num < self.L.get_maxmin():
            self.L.insert(num)
        else:
            self.R.insert(num)
        if self.L.get_length() - self.R.get_length() > 1:
            t = self.L.extract_maxmin()
            self.R.insert(t)
            #print t, self.L.get_length(), self.R.get_length(), self.L.get_maxmin(), self.R.get_maxmin()

        elif self.R.get_length() - self.L.get_length() > 1:
            t = self.R.extract_maxmin()
            self.L.insert(t)

n = int(raw_input().strip())
a = []
MR = MedianRunner()
for a_i in xrange(n):
    a_t = int(raw_input().strip())
    MR.insert(a_t)
    print "%.1f" % MR.getMedian()
    a.append(a_t)
