from sort import Sort

class CountSort(Sort):
    def __init__(self, arr):
        self.arr = arr
    def sortInt(self, reverse=False):
        return self.countSort(self.arr,reverse)
        
    def countSort(self,arr,reverse):
        Max = max(arr)
        Min = min(arr)
        Max += 1
        count = [0] * (Max-Min)
        for i in range(0,len(self.arr)):
            increment = 1
            count[self.arr[i]-Min] += increment
        for i in range(1,len(count)):
            count[i] = count[i] + count[i-1]
        arr2 = [0] * len(self.arr)
        for i in reversed(range(0,len(self.arr))):
            value = count[self.arr[i]-Min]
            value -= 1
            count[self.arr[i]-Min] -= 1
            arr2[value] = (self.arr[i]-Min) + Min
        if(reverse == True):
            return arr2[:: -1]
        else:
            return arr2

if __name__ == "__main__":
    array = [2,-1,4,3,6,-2,3,7]
    output = CountSort(array)
    print(output.sortInt(True))
