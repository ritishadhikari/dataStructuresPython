def selectionSort(array):
    size=len(array)
    for i in range(size-1):
        candidate=array[i]  # candidate is the minimum element
        swap=False
        for j in range(i+1,size):
            if array[j]<candidate:
                candidate=array[j]
                index=j
                swap=True
        if swap:
            swapVal=array[i]
            array[i]=candidate
            array[index]=swapVal
    return array

if __name__=="__main__":
    element=[38, 7,	29,	9, 2, 15, 7,28,3,83]
    print(selectionSort(element))
