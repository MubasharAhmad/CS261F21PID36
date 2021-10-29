from sort import Sort


# Implementation of Insertion Sort for both Numbers and Strigs
class InsertionSort(Sort):
    def __init__(self, arr) -> None:
        super().__init__(arr)

    def sort(self, reverse=False):
        for i in range(1, self.length):
            for j in range(i, 0, -1):
                if(self.arr[j] < self.arr[j - 1] and reverse == False):
                    self.arr[j], self.arr[j -
                                          1] = self.arr[j - 1],  self.arr[j]

                elif(self.arr[j] > self.arr[j - 1] and reverse == True):
                    self.arr[j], self.arr[j -
                                          1] = self.arr[j - 1],  self.arr[j]
                else:
                    break
        return self.arr


if __name__ == "__main":
    numbers = [2, 1, 9, 3, 7, 4, 5]
    sortNumbers = InsertionSort(numbers)
    print("Asscending: ", sortNumbers.sort())
    print("Descending: ", sortNumbers.sort(reverse=True))

    strings = ['b', 'A', 'z', 'C']
    sortStrings = InsertionSort(strings)
    print("Asscending: ", sortStrings.sort())
    print("Descending: ", sortStrings.sort(reverse=True))
