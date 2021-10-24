
# file handling for txt files
class TxtFile:
    def readFile(self, path):
        f = open(path, "r", encoding="utf8")
        lst = f.read().splitlines()
        f.close()
        return lst

    def WriteToFile(self, path, data = []):
        f = open(path, "w")
        f.writelines([data[0], "\n", data[1], "\n", data[2], "\n"])
        f.close()
