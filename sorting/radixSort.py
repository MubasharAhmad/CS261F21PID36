from sort import Sort

class radixSort(Sort):
    def __init__(self, arr,pos):
        self.arr = arr
        self.pos = pos
    def sortInt(self, reverse=False):
        return self.RadixSort(self.arr,reverse)
    def RadixSort(self,arr,reverse):
        Max = max(arr)
        pos = 1
        while((Max // pos) > 0):
            self.countSort(self.arr, pos)
            pos *= 10
        if(reverse == True):
            return self.arr[:: -1]
        else:
            return self.arr

    def countSort(self,arr, pos):
        output = [0] * (len(self.arr))
        count = [0] * (10)
        for i in range(0, len(arr)):
            index = (self.arr[i] // pos)
            count[index % 10] += 1
        #print(count)
        #print("-----------")
        for i in range(1, 10):
            count[i] += count[i - 1]
        #print(count)
        #print("-----------")
        i = len(self.arr) - 1
        while i >= 0:
            value = (self.arr[i] // pos)
            output[count[value % 10] - 1] = self.arr[i]
            count[value % 10] -= 1
            i -= 1
        for i in range(0, len(self.arr)):
            self.arr[i] = output[i]
if __name__ == "__main__":
    array = [110, 45, 65, 50, 90, 602, 24, 2, 66]
    pos = 1
    output = radixSort(array,pos)
    print(output.sortInt(False))