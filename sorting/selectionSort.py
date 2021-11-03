from sorting.sort import Sort


# Implementation of Selection Sort for both Numbers and Strigs
class SelectionSort(Sort):
    def __init__(self, arr) -> None:
        super().__init__(arr)

    # method to sort numbers
    def sort(self, reverse=False):
        for i in range(self.length):
            for j in range(i + 1, self.length):
                if (self.arr[i][Sort.Key] > self.arr[j][Sort.Key] and reverse == False):
                    self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                elif (self.arr[i][Sort.Key] < self.arr[j][Sort.Key] and reverse == True):
                    self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            if i > 1500:
                break
            print(i)

        return self.arr


if __name__ == "__main__":
    numbers = [2, 1, 9, 3, 7, 4, 5]
    sortNumbers = SelectionSort(numbers)
    print("Asscending: ", sortNumbers.sort())
    print("Descending: ", sortNumbers.sort(reverse=True))

    strings = ['b', 'Ab', 'z', 'C']
    sortStrings = SelectionSort(strings)
    print("Asscending: ", sortStrings.sort())
    print("Descending: ", sortStrings.sort(reverse=True))
