# Implementation of Bubble Sort for both Numbers and Strigs
from sorting.sort import Sort


class BubbleSort(Sort):
    def __init__(self, arr) -> None:
        super().__init__(arr)

    def sort(self, reverse=False):
        for j in range(self.length):
            swapped = False
            for i in range(self.length - 1):
                # for ascending order sort
                if (self.arr[i][Sort.Key] > self.arr[i + 1][Sort.Key] and reverse == False):
                    self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
                    swapped = True

                # for descending order sort
                elif (self.arr[i][Sort.Key] < self.arr[i + 1][Sort.Key] and reverse == True):
                    self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
                    swapped = True
            if swapped == False:
                break
            print(j)
            # if j > 1500:
            #     break

        return self.arr


if __name__ == "__main__":
    numbers = [2, 1, 9, 3, 7, 4, 5]
    sortNumbers = BubbleSort(numbers)
    print("Asscending: ", sortNumbers.sort())
    print("Descending: ", sortNumbers.sort(True))

    strings = ['b', 'A', 'z', 'C']
    sortStrings = BubbleSort(strings)
    print("Asscending: ", sortStrings.sort())
    print("Descending: ", sortStrings.sort(reverse=True))
