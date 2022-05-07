import time
import numpy as np

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
                if elements[i]<elements[i-gapSize]:
                    elements[i],elements[i-gapSize]=elements[i-gapSize],elements[i]
            start+=1 
        gapSize-=1
    return elements

@timeit
def insertionSort(elements):
    size=len(elements)
    for i in range(1,size):
        for j in range(0,i):
            if elements[i]<elements[j]:
                swapVal=elements[j]
                elements[j]=elements[i]
                elements[i]=swapVal
    return elements

def swapPos(array,index):
    swapVal=array[index+1]
    array[index+1]=array[index]
    array[index]=swapVal
    return array

@timeit
def bubbleSort3(elements):
    arr=elements.copy()
    for indexi, i in enumerate(arr):
        j=0
        swap=False
        while j<len(arr)-1-indexi:
            if arr[j]>arr[j+1]:
                arr=swapPos(array=arr,index=j)
                swap=True
            else:
                pass
            j+=1
        if not swap:
            break
    return arr

@timeit
def selectionSort(elements):
    size=len(elements)
    for i in range(size-1):
        candidate=elements[i]  # candidate is the minimum element
        swap=False
        for j in range(i+1,size):
            if elements[j]<candidate:
                candidate=elements[j]
                index=j
                swap=True
        if swap:
            swapVal=elements[i]
            elements[i]=candidate
            elements[index]=swapVal
    return elements


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
    np.random.seed=45
    lst=np.random.randint(low=2, high=1000000,size=10000)

    # print(shellSort(elements=lst.copy()))
    # print(insertionSort(elements=lst.copy()))
    # print(bubbleSort3(elements=lst.copy()))
    # print(selectionSort(elements=lst.copy()))
    print(mergeSort(elements=lst.copy()))