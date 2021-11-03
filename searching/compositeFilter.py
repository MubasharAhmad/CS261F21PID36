from searching.search import Search
import pandas as pd


class CompositeFilter(Search):
    def __init__(self, arr) -> None:
        super().__init__(arr)

    def search(self, value):
        lgOp = ""
        idx = 0
        value = value.split(" ")
        if "and" in value:
            idx = value.index("and")
            lgOp = "and"
        elif "or" in value:
            idx = value.index("or")
            lgOp = "or"
        elif "not" in value and value.index("not") == 0:
            lgOp = "not"
        q1, q2 = "", ""
        for i in range(idx):
            q1 += value[i] + " "
        for i in range(idx + 1, len(value)):
            q2 += value[i] + " "
        q1, q2 = q1.strip(), q2.strip()
        print(q1, q2)
        
        data = []

        for j in self.arr:
            text = str(j["Name"])+" "+j["Id"]+" "+str(j["Price"])+" "+str(j["Pages"])+" "+j["Author"]+" "+j["Language"]+" "+j["Type"]
            if lgOp == "and":
                if ((q1 in text) and (q2 in text)) == True:
                    data.append(j)

            elif lgOp == "or":
                if ((q1 in text) or (q2 in text)) == True:
                    data.append(j)

            elif lgOp == "not":
                if q2 not in text:
                    data.append(j)

        df = pd.DataFrame(data)
        df.to_csv('CSV_Files/output.csv', index=False, encoding='utf-8', header=True)
