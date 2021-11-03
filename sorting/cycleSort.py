from sorting.sort import Sort

# Implementation of Cycle Sort for both Numbers and Strigs


class CycleSort(Sort):
    def __init__(self, arr) -> None:
        super().__init__(arr)

    def sort(self, reverse=False):
        for c in range(self.length):
            item = self.arr[c]
            counter = c

            for i in range(c + 1, self.length):
                if self.arr[i][Sort.Key] < item[Sort.Key]:
                    counter += 1

            item, self.arr[counter] = self.arr[counter], item

            while(counter != c):
                counter = c
                for i in range(c + 1, self.length):
                    if self.arr[i][Sort.Key] < item[Sort.Key]:
                        counter += 1
                print(counter)
                item, self.arr[counter] = self.arr[counter], item
        if reverse:
            return self.arr[::-1]
        return self.arr


if __name__ == "__main__":
    numbers = [2, 1, 9, 3, 2, 4, 5]
    sortNumbers = CycleSort(numbers)
    print("Asscending: ", sortNumbers.sort())
    print("Descending: ", sortNumbers.sort(reverse=True))

    strings = ['b', 'A', 'z', 'C']
    sortStrings = CycleSort(strings)
    print("Asscending: ", sortStrings.sort())
    print("Descending: ", sortStrings.sort(reverse=True))
