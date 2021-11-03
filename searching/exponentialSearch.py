from searching.search import Search


class ExponentialSearch(Search):
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
        n = 1
        while (n < self.length and self.arr[n][self.Key] <= value):
            n *= 2
        print(n)
        from searching.binarySearch import BinarySearch
        b_search = BinarySearch(self.arr)
        b_search.bsearch(value, n // 2, min(n, self.length - 1))
