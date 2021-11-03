from sorting.sort import Sort


class PancakeSort(Sort):
    count = 0
    def __init__(self, arr) -> None:
        super().__init__(arr)
    
    def sort(self,reverse):
        length = len(self.arr)
        while(length != 0):
            if(type(self.arr[length - 1][Sort.Key]) == str):
                Max = "\u0000"
                for i in range(0,length):
                    # print(self.arr[i][Sort.Key])
                    if(str(self.arr[i][Sort.Key]) > (Max)):
                        Max = str(self.arr[i][Sort.Key])
                        ind = i
                        # print("Hello")
                length -= 1
                self.arr[length],self.arr[ind] = self.arr[ind], self.arr[length]
                self.count += 1
                if self.count == 1000:
                    break
                # print(str(self.count))
            elif (type(self.arr[length - 1][Sort.Key]) == int):
                Max = 0
                for i in range(0,length):
                    if((self.arr[i][Sort.Key]) > (Max)):
                        Max = self.arr[i][Sort.Key]
                        ind = i
                        # print("Hello")
                length -= 1
                self.arr[length],self.arr[ind] = self.arr[ind], self.arr[length]
                self.count += 1
                if self.count == 1000:
                    break
                
                print(str(self.count))
        # print("Hello")
        if(reverse == True):
            return self.arr[:: -1]
        else:
            return self.arr
if __name__ == "__main__":
    array = [110, 45, 65, 50, 90, 602, 24, 2, 66]
    output = PancakeSort(array)
    print(output.sort(True))

    # array1 = ["Egg","Water","Apple","Sorry"]
    # output = PancakeSort(array1)
    # print(output.sort(False))
