# Implementation of Merge Sort for both Numbers and Strigs
from sort import Sort


class MergeSort(Sort):
    def __init__(self, arr) -> None:
        super().__init__(arr)

    # sort
    def sort(self, reverse=False):
        self.mergeSort(0, len(self.arr) - 1, reverse)
        return self.arr

    # merge
    def merge(self, left, mid, right, reverse):
        L = []
        R = []

        for i in range(left, mid + 1):
            L.append(self.arr[i])
        for i in range(mid + 1, right + 1):
            R.append(self.arr[i])

        if reverse == False and type(self.arr[0]) == int:
            L.append(100000000000000000)
            R.append(100000000000000000)
        elif reverse == True and type(self.arr[0]) == int:
            L.append(-100000000000000000)
            R.append(-100000000000000000)

        elif reverse == False and type(self.arr[0]) == str:
            L.append("z")
            R.append("z")
        elif reverse == True and type(self.arr[0]) == str:
            L.append("A")
            R.append("A")

        i = 0
        j = 0

        for k in range(left, right+1):
            # for ascending order
            if reverse == False:
                if L[i] <= R[j]:
                    self.arr[k] = L[i]
                    i += 1
                else:
                    self.arr[k] = R[j]
                    j += 1
            # for descending order
            else:
                if L[i] >= R[j]:
                    self.arr[k] = L[i]
                    i += 1
                else:
                    self.arr[k] = R[j]
                    j += 1

    # merge sort
    def mergeSort(self, left, right, reverse):
        if left < right:
            mid = left + (right - left) // 2
            self.mergeSort(left, mid, reverse)
            self.mergeSort(mid + 1, right, reverse)
            self.merge(left, mid, right, reverse)


if __name__ == "__main__":
    numbers = [2, 1, 9, 3, 7, 4, 5]
    sortNumbers = MergeSort(numbers)
    print("Asscending: ", sortNumbers.sort())
    print("Descending: ", sortNumbers.sort(True))

    strings = ['b', 'A', 'z', 'C']
    sortStrings = MergeSort(strings)
    print("Asscending: ", sortStrings.sort())
    print("Descending: ", sortStrings.sort(reverse=True))
