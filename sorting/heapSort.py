# Implementation of Heap Sort for both Numbers and Strigs
from sorting.sort import Sort


class HeapSort(Sort):
    def __init__(self, arr) -> None:
        super().__init__(arr)

    def sort(self, reverse=False):
        for i in range((self.length // 2) - 1, -1, -1):
            self.makeHeap(self.length, i)

        for j in range(self.length - 1, 0, -1):
            self.arr[j], self.arr[0] = self.arr[0], self.arr[j]
            self.makeHeap(j, 0)
        if reverse:
            return self.arr[::-1]
        return self.arr

    def makeHeap(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        try:
            if type(self.arr[largest][Sort.Key]) == type(self.arr[left][Sort.Key]):
                if left < n and self.arr[largest][Sort.Key] < self.arr[left][Sort.Key]:
                    largest = left

                if right < n and self.arr[largest][Sort.Key] < self.arr[right][Sort.Key]:
                    largest = right
        except:
            pass

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.makeHeap(n, largest)


if __name__ == "__main__":
    numbers = [2, 1, 9, 3, 2, 4, 5, 1]
    sortNumbers = HeapSort(numbers)
    print("Asscending: ", sortNumbers.sort())
