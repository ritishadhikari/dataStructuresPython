def insertionSort(array):

    size=len(array)-1
    for i in range(size):
            for index,element in enumerate(array[:i+1]):
                if array[i+1] < element:
                    array.insert(index,array[i+1])
                    array.pop(i+2)
                    break

    return array


if __name__=="__main__":

    element=[38,9,29,7,2,15,28]

insertionSort(array=element)