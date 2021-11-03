from sorting.sort import Sort


# Implementation of Bitonic Sort for both Numbers and Strigs
class BitonicSort(Sort):
    def __init__(self, arr) -> None:
        super().__init__(arr)
        self.array()

    def sort(self, reverse=False):
        self.sortBitonic(0, self.length, 1)
        if reverse:
            return self.arr[::-1]
        return self.arr

    def compare(self, i, j, direction):
        try:
            if (direction == 1 and self.arr[i][Sort.Key] > self.arr[j][Sort.Key]) or (direction == 0 and self.arr[i][Sort.Key] < self.arr[j][Sort.Key]):
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        except:
            pass

    def merge(self, a, b, direction):
        if b > 1:
            k = int(b/2)
            for i in range(a, a+k):
                self.compare(i, i+k, direction)
            self.merge(a, k, direction)
            self.merge(a+k, k, direction)

    def sortBitonic(self, a, b, direction):
        if b > 1:
            k = int(b/2)
            self.sortBitonic(a, k, 1)
            self.sortBitonic(a+k, k, 0)
            self.merge(a, b, direction)
    
    def array(self):
        num = 1
        while (num * 2) <= self.length:
            num *= 2
        self.arr = self.arr[:num]
        # pass

if __name__ == "__main__":
    numbers = [2, 1, 9, 3, 2, 4, 5, 1]
    sortNumbers = BitonicSort(numbers)
    print("Asscending: ", sortNumbers.sort())
    print("Asscending: ", sortNumbers.sort(True))
