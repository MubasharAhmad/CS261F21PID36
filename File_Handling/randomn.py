import sys
import random
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

# file handling for txt files
class TxtFile:
    def readFile(self, path):
        f = open(path, "r", encoding="utf8")
        lst = f.read().splitlines()
        f.close()
        return lst

class Random:
    f = TxtFile()

    def __init__(self, AuthorsFile, LanguagesFile, TypesFile):
        self.Authors = self.f.readFile(AuthorsFile)
        self.Languages = self.f.readFile(LanguagesFile)
        self.Types = self.f.readFile(TypesFile)

    def GetID(self):
        c = ""
        for i in range(5):
            c += chr(random.randint(65, 90))
        return c + str(random.randint(10000, 99999))

    def GetAuthor(self):
        return self.Authors[random.randint(0, len(self.Authors) - 1)]

    def Getlanguage(self):
        return self.Languages[random.randint(0, len(self.Languages) - 1)]

    def GetType(self):
        return self.Types[random.randint(0, len(self.Types) - 1)]

    def GetPrice(self):
        return random.randint(1000, 9999)

    def GetPages(self):
        return random.randint(100, 5000)


if __name__ == "__main__":
    r = Random(r"TextFiles\Authors.txt",
               r"TextFiles\languages.txt", r"TextFiles\Types.txt")
    print(r.GetID(), r.GetAuthor(), r.Getlanguage(),
          r.GetType(), r.GetPages(), r.GetPrice())
