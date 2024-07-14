def mergeSort(arr:[int], s:int,e:int):
    if s==e:
        return
    # Write your code here.
    mid=(s+e)//2
    mergeSort(arr,s,mid)
    mergeSort(arr,mid+1,e)

    left=arr[s:mid+1]
    right=arr[mid+1:e+1]

    i,j,k=0,0,s

    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
            k+=1
        else:
            arr[k]=right[j]
            j+=1
            k+=1
    while i<len(left):
            arr[k]=left[i]
            k+=1
            i+=1
    while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1