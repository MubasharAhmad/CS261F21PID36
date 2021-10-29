from sort import Sort

class BucketSort(Sort):
    def __init__(self, arr):
        self.arr = arr
    def sortInt(self, reverse=False):
        return self.bucketSort(self.arr,reverse)
    def insertionSort(self,array):
        for j in range(0, len(array)):
            key = array[j]
            i = j-1
            while(i >= 0 and array[i] > key):
                array[i+1] = array[i]
                i = i-1
            array[i+1] = key
        return (array)
    def bucketSort(self,x,reverse):
        arr = []
        buckets = 10
        for i in range(0,buckets):
            arr.append([])
        for i in x:
            ind = int(10 * i)
            arr[ind].append(i)
        for i in arr:
            self.insertionSort(i)
        counter = 0
        for i in arr:
            for j in i:
                x[counter] = j
                counter += 1
        if(reverse == True):
            return x[:: -1]
        else:
            return x
if __name__ == "__main__":
    array = [0.897, 0.565, 0.665,0.1234,0.367, 0.656, 0.3434]
    output = BucketSort(array)
    print(output.sortInt(True))
