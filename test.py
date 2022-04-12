def shellSort(elements):
    size=len(elements)
    gapSize=size//2
    
    while gapSize>=1:
        start=0
        while start<gapSize:
            for i in range(start,size,gapSize):
                for j in range(start,i,gapSize):
                    if elements[j] > elements[i]:
                        swapVal=elements[i]
                        elements[i]=elements[j]
                        elements[j]=swapVal  
            i,j=0,0    
            start+=1 
        gapSize-=1

    return elements
# elements=[38,7,29,9,2,15,28]
elements=[21,38,29,17,4,25,11,32,9]
# elements=[38,39,29,17,16,25,11,32,7]
print(shellSort(elements=elements))