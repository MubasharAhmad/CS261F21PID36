from os import error
from sorting.sort import Sort
# import sys
# sys.setrecursionlimit(100000)
import random


class QuickSort(Sort):
    counter = 0

    def __init__(self, arr):
        self.arr = arr

    def sort(self, reverse=False):
        try:
            return self.quickSort(self.arr, 0, len(self.arr)-1, reverse)
        except:
            print("In except block Quick sort")
            return []
    def quickSort(self, arr, low, high, reverse):
        if (low < high):
            pi = self.partition(self.arr, low, high)
            self.counter += 1
            # print(self.counter)
            self.quickSort(self.arr, low, pi-1, reverse)
            self.quickSort(self.arr, pi+1, high, reverse)
        if(reverse == True):
            return self.arr[:: -1]
        else:
            return self.arr

    def partition(self, arr, low, high):
        n = random.randint(low, high)
        pivot = self.arr[n]
        i = (low - 1)
        for j in range(low, high):
            try:
                if(self.arr[j][Sort.Key] < pivot[Sort.Key]):
                    i += 1
                    self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            except:
                pass
        self.arr[high], self.arr[i+1] = self.arr[i+1], self.arr[high]
        return (i+1)

    def sortString(self, reverse=False):
        return self.quickSort(self.arr, 0, len(self.arr)-1, reverse)


if __name__ == "__main__":
    array = [2, -1, 4, 3, -2, 9, 7]
    output = QuickSort(array)
    print(output.sortInt(True))

    array1 = ["E", "B", "F", "Q"]
    output1 = QuickSort(array1)
    print(output1.sortString(False))
