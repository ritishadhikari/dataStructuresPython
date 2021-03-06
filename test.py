import time


def timeit(func):
    def execFunc(*args, **kwargs):
        startTime=time.time()
        result=func(*args, **kwargs)
        endTime=time.time()
        totalTime=endTime-startTime
        print(f"{func.__name__} took {totalTime} seconds")
        return result
    return execFunc

@timeit
def shellSort(elements):
    size=len(elements)
    gapSize=size//2
    while gapSize>=1:
        start=0
        while start<gapSize:
            for i in range(start+gapSize,size,gapSize):
                for j in range(i-gapSize,i,gapSize):
                    if elements[i] < elements[j]:
                        swapVal=elements[i]
                        elements[i]=elements[j]
                        elements[j]=swapVal     
            start+=1 
        gapSize-=1

    return elements

# @timeit
def insertionSort2(array):
    size=len(array)
    for i in range(1,size):
        for j in range(i-1,i):
            if array[i]<array[j]:
                swapVal=array[j]
                array[j]=array[i]
                array[i]=swapVal
    return array

@timeit
def mergeSort(elements):
    
    if len(elements)==1:
        return elements
    else:
        size=len(elements)
        midPoint=size//2
        leftArray=elements[:midPoint]
        rightArray=elements[midPoint:]

        leftArray=mergeSort(elements=leftArray)
        rightArray=mergeSort(elements=rightArray)

        ##################################################################
        elementsCP=[]
        leftIndex,rightIndex=0,0
        while leftIndex<len(leftArray) and rightIndex<len(rightArray):
            if leftArray[leftIndex]<=rightArray[rightIndex]:
                elementsCP.append(leftArray[leftIndex])
                leftIndex=leftIndex+1
            else:
                elementsCP.append(rightArray[rightIndex])
                rightIndex=rightIndex+1
        if leftIndex==len(leftArray):
            for element in rightArray[rightIndex:]:
                elementsCP.append(element)
        else:
            for element in leftArray[leftIndex:]:
                elementsCP.append(element)

        return elementsCP

if __name__=="__main__":
    
    element=[38, 7,	29,	9, 2, 15, 28]
    element=[29,7,38,9,2,15,28]
    element=[38,9,4,29,17,32,21]
    print(mergeSort(elements=element))