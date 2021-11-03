from sorting.sort import Sort
import pandas as pd


class MultiLevelSorting(Sort):
    def __init__(self, arr, data) -> None:
        super().__init__(arr)
        self.data = data

    def sort(self, reverse=False):
        sortedData = []
        if self.data == "":
            from sorting.mergeSort import MergeSort
            merge = MergeSort(self.arr)
            sortedData = merge.sort(reverse)
        else:
            subarray = []
            if type(self.arr[0][self.data]) == str:
                item = str(self.arr[0][self.data])[0]
            else:
                item = self.arr[0][self.data]

            for i in range(self.length - 2):
                if item ==  str(self.arr[i + 1][self.data])[0] and type(self.arr[0][self.data]) == str:
                    subarray.append(self.arr[i])
                elif item == self.arr[i + 1][self.data] and type(self.arr[i + 1][self.data]) == int:
                    subarray.append(self.arr[i])
                else:
                    from sorting.mergeSort import MergeSort
                    merge = MergeSort(subarray)
                    sorted = merge.sort(reverse)
                    for line in sorted:
                        sortedData.append(line)
                    subarray = []
                    if type(self.arr[0][self.data]) == str:
                        item = str(self.arr[i][self.data])[0]
                    else:
                        item = self.arr[i][self.data]

        df = pd.DataFrame(sortedData)
        df.to_csv('CSV_Files/multiLevelSortingOutput.csv', index=False, encoding='utf-8', header=True)
        f = open(r"TextFiles\multiSortingData.txt", "w")
        f.writelines([self.Key+"\n"])
        f.close()
        return sortedData
