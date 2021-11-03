from searching.search import Search
import pandas as pd
import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

class LinearSearch(Search):
    def __init__(self, arr) -> None:
        super().__init__(arr)
    
    def search(self, value):
        result = []

        for data in self.arr:
            if (value == str(data[Search.Key])):
                result.append(data)
        
        df = pd.DataFrame(result)
        df.to_csv('CSV_Files/output.csv', index=False, encoding='utf-8', header= True)

