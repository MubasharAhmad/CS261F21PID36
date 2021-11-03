from searching.search import Search
import pandas as pd

class BinarySearch(Search):
    def __init__(self, arr) -> None:
        super().__init__(arr)
    
    def search(self, value):
        if type(self.arr[0][self.Key]) == int:
            try:
                value = int(value)
            except:
                pass
        else:
            value = str(value)
        self.bsearch(value, 0, self.length - 1)

    def bsearch(self, value, left, right):
        data = []
        try:
            while left <= right:
                mid = left + (right - left) // 2

                if value == self.arr[mid][self.Key]:
                    data.append(self.arr[mid])
                    break
                
                elif value < self.arr[mid][self.Key]:
                    right = mid - 1
                
                else:
                    left = mid + 1
        except:
            pass
        print(data)

        df = pd.DataFrame(data)
        df.to_csv('CSV_Files/output.csv', index=False, encoding='utf-8', header= True)
