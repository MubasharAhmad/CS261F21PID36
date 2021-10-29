from sort import Sort

class QuickSort(Sort):
    def __init__(self, arr):
        self.arr = arr
    def sortInt(self, reverse=False):
        return self.quickSort(self.arr,0,len(self.arr)-1,reverse)
    def quickSort(self,arr, low, high,reverse):
        if (low < high):
            pi = self.partition(self.arr, low, high)
            self.quickSort(self.arr, low, pi-1,reverse)
            self.quickSort(self.arr, pi+1, high,reverse)
        if(reverse == True):
            return self.arr[:: -1]
        else:
            return self.arr
    def partition(self,arr, low, high):
        pivot = self.arr[high]
        i = (low - 1)
        for j in range(low,high):
            if(self.arr[j] < pivot):
                i += 1
                self.arr[i],self.arr[j] = self.arr[j],self.arr[i]
        self.arr[high],self.arr[i+1] = self.arr[i+1],self.arr[high]
        return (i+1)
    def sortString(self, reverse=False):
        return self.quickSort(self.arr,0,len(self.arr)-1,reverse)

if __name__ == "__main__":
    array = [2,-1,4,3,-2,9,7]
    output = QuickSort(array)
    print(output.sortInt(True))

    array1 = ["E","B","F","Q"]
    output1 = QuickSort(array1)
    print(output1.sortString(False))