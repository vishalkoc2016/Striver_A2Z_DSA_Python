from typing import*

def superiorElements(arr : List[int]) -> List[int]:
    n=len(arr)
    i=n-1
    ans=[]
    mx=-float('inf')
    while i>0:
        if arr[i]>mx:
            ans.append(arr[i])
            mx=arr[i]
        i-=1
    return ans   

                     