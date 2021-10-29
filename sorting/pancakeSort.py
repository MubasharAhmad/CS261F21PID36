from sort import Sort

class pancakeSort(Sort):
    def __init__(self, arr):
        self.arr = arr

    def sortInt(self, reverse=False):
        return self.PancakeSortInt(self.arr, reverse)

    def PancakeSortInt(self, arr, reverse):
        length = len(arr)
        while(length != 0):
            Maximum = 0
            for i in range(0,length):
                if(self.arr[i] > Maximum):
                    Maximum = self.arr[i]
                    index = i
            self.arr[length - 1] , self.arr[index] = self.arr[index], self.arr[length - 1]
            length -= 1
        if(reverse == True):
            return self.arr[:: -1]
        else:
            return self.arr
    def sortString(self, reverse=False):
        return self.PancakeSort(self.arr, reverse)

    def PancakeSort(self, arr, reverse):
        length = len(arr)
        while(length != 0):
            Maximum = 0
            for i in range(0,length):
                if(str(self.arr[i]) > str(Maximum)):
                    Maximum = self.arr[i]
                    index = i
            self.arr[length - 1] , self.arr[index] = self.arr[index], self.arr[length - 1]
            length -= 1
        if(reverse == True):
            return self.arr[:: -1]
        else:
            return self.arr
if __name__ == "__main__":
    array = [110, 45, 65, 50, 90, 602, 24, 2, 66]
    output = pancakeSort(array)
    print(output.sortInt(True))

    array1 = ["Egg","Water","Apple","Sorry"]
    output = pancakeSort(array1)
    print(output.sortString(True))