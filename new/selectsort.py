def selectsort(array):
    for i in range(len(array)-1,0,-1):
        maxone=0
        for j in range(1,i+1):
            if array[j]>array[maxone]:
                   maxone=j
            temp=array[i]
            array[i]=array[maxone]
            array[maxone]=temp
    return array
array=[3,1,4,7,5]
print selectsort(array)