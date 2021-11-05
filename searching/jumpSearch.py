from searching.search import Search
import pandas as pd


class JumpSearch(Search):
    def __init__(self, arr) -> None:
        super().__init__(arr)

    def search(self, value):
        # low = 0
        high = 3
        result = []
        while(high < self.length and self.arr[high][Search.Key] <= value):
            # low = high
            high += 3
        h = min(self.length,high)
        for i in range(high - 3, h):
            if (str(value) == str(self.arr[i][Search.Key])):
                result.append(self.arr[i])
        df = pd.DataFrame(result)
        df.to_csv('CSV_Files/output.csv', index=False,
                  encoding='utf-8', header=True)

if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    s = JumpSearch(array)
    s.search(13)
