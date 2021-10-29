from sort import Sort

class patienceSort(Sort):
    def __init__(self, arr):
        self.arr = arr

    def sortInt(self, reverse=False):
        return self.PatienceSortInt(self.arr, reverse)
    def PatienceSortInt(self,arr,reverse):
        list1 = []
        list1.append([arr[0]])
        for i in range(1,len(arr)):
            appended = False
            for j in list1:
                if j[len(j)-1] > arr[i]:
                    j.append(arr[i])
                    appended = True
                    break
            if (appended == False):
                list1.append([arr[i]])
        newArray = []
        for i in range(0,len(arr)):
            index = 0
            c = len(list1[0])
            for i in range(len(list1)):
                if(len(list1[i]) > c):
                    index = i
            compare1 = list1[index][len(list1[index]) - 1]
            for j in range(0,len(list1)):
                if(list1[j] != []):
                    compare2 = list1[j][len(list1[j])-1]
                    if(compare2 < compare1):
                        compare1 = compare2
                        index = j
            if(str(compare1) > str(0)):
                newArray.append(compare1)
                list1[index].pop(len(list1[index])-1)
            else:
                newArray.append(compare1)
                list1[index].pop(len(list1[index])-1)
        if(reverse == True):
            return newArray[:: -1]
        else:
            return newArray
    def sortString(self, reverse=False):
        return self.PatienceSortInt(self.arr, reverse)
    
if __name__ == "__main__":    
    array = [110, 45, 65, 50, 90, 602, 2, 2, -1]
    output = patienceSort(array)
    print(output.sortInt(False))

    array1 = ["Egg","Water","Apple","Sorry"]
    output = patienceSort(array1)
    print(output.sortString(True))