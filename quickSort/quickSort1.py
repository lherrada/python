from typing import List
import random


class quickSort3:
    def __init__(self, array: List):
        self.array = array

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def partition(self, left, right):
        # pivot_index = random.randint(left, right)
        # pivot = self.array[pivot_index]
        # self.swap(pivot_index, right)
        pivot = self.array[right]

        store_index = left
        for i in range(left, right):
            if self.array[i] < pivot:
                self.swap(i, store_index)
                store_index += 1

        self.swap(right, store_index)
        return store_index

    def quickSort(self, left, right):
        if left >= right:
            return
        index = self.partition(left, right)
        self.quickSort(left, index - 1)
        self.quickSort(index + 1, right)


array = [5, 9, 1, 0, 4, 3, 2]
print("Original: ", array)
p = quickSort3(array)
p.quickSort(0, len(array) - 1)
print("Sorted: ", array)
