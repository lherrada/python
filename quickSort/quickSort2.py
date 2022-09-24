from typing import List


class quickySort:
    def __init__(self, array: List):
        self.array = array

    def partition(self, lowIndex, highIndex):
        left, right = lowIndex, highIndex
        pivot = self.array[highIndex]
        while left < right:
            while self.array[left] <= pivot and left < right:
                left += 1
            while self.array[right] >= pivot and left < right:
                right -= 1
            self.swap(left, right)

        self.swap(left, highIndex)
        return left

    def swap(self, left, right):
        self.array[left], self.array[right] = self.array[right], self.array[left]

    def qsort(self, left, right):
        if left >= right:
            return
        index = self.partition(left, right)
        self.qsort(left, index - 1)
        self.qsort(index + 1, right)


a = [3, 1, 6, 4, 9, 2]
print("Original array: ", a)
p = quickySort(a)
p.qsort(0,len(a) - 1)
print("Sorted array: ", a)
