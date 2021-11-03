from abc import abstractmethod

class Search:
    Key = ""
    def __init__(self, arr) -> None:
        self.arr = arr
        self.length = len(arr)
    
    @abstractmethod
    def search(self, value):
        pass