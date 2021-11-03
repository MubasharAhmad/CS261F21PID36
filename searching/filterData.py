from searching.search import Search
import pandas as pd


class FilterData(Search):
    def __init__(self, arr) -> None:
        super().__init__(arr)

    def search(self, value):
        data = []

        for i in self.arr:
            if value in str(i[self.Key]):
                data.append(i)

        df = pd.DataFrame(data)
        df.to_csv('CSV_Files/output.csv', index=False, encoding='utf-8', header=True)
