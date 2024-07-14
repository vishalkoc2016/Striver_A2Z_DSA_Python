# name= "vishal kuamr gupta"
# age=24
# gender='M'
# weight= 60.14
# isTeacher=True

# #situdatio-> unique, add, remove, edit
# #set
# fruitsLiked= {"orange","apple","watermelone"}

# #repeated, add, remove, edit
# #list
# earningFrom2022=[22,55,45,54,35]

# #fixed repeat
# #list
# earningBefore2022=(22,54,64,82,41)

# #key value
# #dictionary
# property={
#    "orange":5,
#    "apple":"7kg"
#    "watermelon:""1kg"
# }

# #None
# overHyperd=None

# print(name,type(name))
# print(age,type(age))
# print(gender,type(gender))
# print(weight,type(weight))
# print(isTeacher,type(isTeacher))
# print(fruitsLiked,type(fruitsLiked))
# print(earningFrom2022,type(earningFrom2022))
# print(earningBefore2022,type(earningBefore2022))
# print(property,type(property))
# print(overHyperd,type(overHyperd))

# firstname= "Vishal Kumar"
# surname= "Gupta"
# name= firstname+" "+surname
# print(name)

# lst=[1,5,6,8,7]
# lst.append(4)
# print(lst)
# lst.insert(0,77) #1st position index show kr rha hai aur second wali value jo rakhni hai vaha 
# print(lst)

# lst.pop(-2) # -2 ka mtlb pichhe se dusare number pe jo hai usko pop kiye
# lst.pop(0)
# print(lst)

# lst[2]= 44
# print(lst)
           
# num=(5,4,7,3,7)
# print(num[2])           

# name = "Vishal"
# print(name[0:4]) 
# print(name[0:6:2])
# Ye jo 3rd jgh pe 2 hai vo 2-2 ke gap pe lega

# name= "Vijay Kumar"
# print(name[0:])
# print(name[0:11])
# print(name[0:11:1])

# # Reverse ka logic
# print(name[-1::-1])

# # Ye list ke liye bhi apply hota hai
# lst= [2,4,5,8,9]
# print(lst[-1::-1])
# print(lst[-1:0:-1]) 
# # yaha par vo 0th postion wala chhod dega

# lst = [2,5,4,6,9]
# print(lst,id(lst))
# lst.append(55)
# print(id(lst))
# so list is mutable 

# lst= [ 4,5,24,9,6,7]
# lst.append(12)
# print(lst)
# lst.insert(0,33)
# print(lst)

# lst.pop(1)
# print(lst)

# lst.remove(24)

# print(lst)

#append(element)
#insert(index, element)
# remove(elemnt)
# pop(index)

#String Modify
#string is imutable so can't change
#so use concat, slice

# name= "Vishal Kumar"
# res= name[0:6]+ "i "+ name[7:13] + "i"
# print(res)

# state = "I am an obdient student"
# lst = state.split()
# print(lst)

# colors= ["i","am","going","to","home"]
# res= " ".join(colors)
# print(res)
# print(res,type(res))


# mark = int(input())

# if mark>=90:
#     print("A")
# elif mark>=75:
#     print("B")
# elif mark>=60:
#     print("c")
# elif mark>=33:
#     print("D")
# else:
#     print("Fail")

# pushup = 1

# while pushup<=15:
#     print("Do not Pushup")
#     pushup = pushup+1

# for varaiable_name in SEQUENCE:
#     print("Do one pushup")

#     # sequence- list, tuple,
#  #[1,5,6,8,9]
#  #(4,9,3,7,5)
#  #range(1,4)

# print(list(range(1,4)))

# lst= list(range(3,16,1))
# print(lst)
#tuple me bhi kara sakte hai

# for num in range(1,16):
#   print(num)

# lst = [6,7,12,8,25]
# n= len(lst)
# # for i in range(n):
# #     print(i,lst[i])

# for i in range(n-1,-1,-1):
#     print(i,lst[i])

# lst= [2,3,4,5,17,23,29,31]

# k=105

# ans =-1

# for i in range(len(lst)):
#    if lst[i]==k:
#       ans=i
#       break 
# print(ans)

# NOW WE ARE STARTING FUNCTION

# def summation(a,b,c):
#     print(a+b+c)

# summation(46,33,22)

# def summation(lst):
#      lst.append(5)
#      print(id(lst))
#      lst=[5,9,7,8]
#      print(id(lst))

# lst = [3,5,6,72]
# print(id(lst))
# summation(lst)

# def summ(x):
#     print(id(x))
#     x=15
#     print(id(x))



# x=12
# print(id(x))
# summ(x)


# def summation(lst):
#     #  for num in lst:
#     #     print(num)

#     sum=0
#     for num in lst:
#       sum=sum+num
#       print("FUNCTION")
#     print(sum)


# lst = [3,5,6,72]
# print("------------>")
# summation(lst)


#ADD +1 TO EACH EMELNT OF LIST

def updatation(lst):
    n=len(lst)
    for i in range(n):
        lst[i]=lst[i]+1

lst =[1,2,3,2,6,5,1]
print(id(lst))
updatation(lst)
print(lst)
print(id(lst))