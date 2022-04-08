def binarySearch(numbersList,numberToFind):
    Kn=len(numbersList)
    searchN=Kn//2
    indexVal=searchN
    if numberToFind==numbersList[searchN]:
        return indexVal
    elif numberToFind<=numbersList[searchN]:
        numbersList=numbersList[:searchN]
        if numberToFind<numbersList[0]:
            return None
        else:  
            indexVal=binarySearch(numbersList,numberToFind)
    elif numberToFind>=numbersList[searchN]:
        numbersList=numbersList[searchN:]
        if numberToFind>numbersList[-1]:
            return None
        else:
            indexVal=indexVal+binarySearch(numbersList,numberToFind)
    
    return indexVal

# Technique through While Loop as explained in Code Basics

def binarySearch(numbersList,numberToFind):

    leftIndex=0
    rightIndex=len(numbersList)-1

    while leftIndex<=rightIndex:
        midIndex=(leftIndex+rightIndex)//2
        if numberToFind==numbersList[midIndex]:
            return midIndex
        elif numberToFind>numbersList[midIndex]:
            leftIndex=midIndex+1
        else:
            rightIndex=midIndex-1
    
    else:
        return -1


if __name__=="__main__":
    numbersList=[12, 15, 17, 19, 21, 24, 45, 67,69,73]
    numberToFind=73
    binarySearch(numbersList=numbersList, numberToFind=numberToFind)