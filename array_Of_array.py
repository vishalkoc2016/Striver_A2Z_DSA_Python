arr=[[1,5],[5,6],[8,9],[2,9],[3,4]]
arr.sort()
print(arr)

#FOR SORTING ON 2ND KEY BASIS
#LETS SEE THE CODE VISHAL

arr.sort(key=lambda x:x[1])
print(arr)