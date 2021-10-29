from abc import ABC, abstractmethod


class Sort:
    def __init__(self, arr) -> None:
        self.arr = arr
        self.length = len(arr)

    # method to sort elements
    @abstractmethod
    def sort(self, reverse=False):
        pass
