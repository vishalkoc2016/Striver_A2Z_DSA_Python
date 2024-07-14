# name = input()
# print('My name is',name)

# for i in range(5):
#   for j in range(5):
#    print("*",end="")
#   print()

# for i in range(1,6):
#   for j in range(i):
#    print("*",end="")
#   print()

# for i in range(1,6):
#   for j in range(1,i+1):
#    print(i,end="")
#   print()

# for i in range(5,1,-1):
#   for j in range(1,i+1):
#    print("*",end="")
#   print()

# for i in range(5,0,-1):
#   for j in range(1,i+1):
#    print(j,end="")
#   print()

# n=5

# for i in range(n):
#   #SPACE PRINT KARNA HAI PAHLE
#   for j in range(n-1-i):
#        print(" ",end="")

#   for j in range(2*i+1):
#        print("*",end="")

#   print()


# n=5

# for i in range(n):
#   #SPACE PRINT KARNA HAI PAHLE
#   for j in range(i):
#        print(" ",end="")

#   for j in range(2*(n-1-i)+1):
#        print("*",end="")

#   print()


# n=5

# for i in range(n):
#   #SPACE PRINT KARNA HAI PAHLE
#   for j in range(n-1-i):
#        print(" ",end="")

#   for j in range(2*i+1):
#        print("*",end="")

#   print()

# n=5

# for i in range(n):
#   #SPACE PRINT KARNA HAI PAHLE
#   for j in range(i):
#        print(" ",end="")

#   for j in range(2*(n-1-i)+1):
#        print("*",end="")

#   print()

# n=5

# for i in range(n):
#   #SPACE PRINT KARNA HAI PAHLE
#      for j in range(i+1):
#            print("*",end="")
#      print()

# for i in range(n-1):
#     for j in range(n-1-i):
#           print("*",end="")

#     print()

# n=5

# for i in range(2*n-1):
#      if i<n:
#   #SPACE PRINT KARNA HAI PAHLE
#         for j in range(i+1):
#            print("*",end="")
#      else:  
#         for j in range(2*n-1-i):
#           print("*",end="")

#      print()

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print((i+j+1)%2,end="")
#     print()

# n=4
# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end="")
    
#     for j in range((n-i-1)*2):
#         print (" ",end="")

#     for j in range(i+1,0,-1):
#         print(j,end="")
    

#     print()

# n=4
# k=1
# for i in range(n+1):
#     for j in range(i+1):
#         print(k ,end=" ")
#         k=k+1
    
#     print( )
                  


# def numTochar(num):
#     return chr(num+65)
# n=4
# A=65
# for i in range(n+1):
#     for j in range(i+1):
#         print(numTochar(j) ,end=" ")
    
#     print( )
             

# def numTochar(num):
#     return chr(num+65)
# n=5
# for i in range(n):
#     for j in range(n-i):
#         print(numTochar(j) ,end=" ")
#     print( )

def numTochar(num):
    return chr(num+65)
n=5
for i in range(n):
    for j in range(i+1):
        print(numTochar(i) ,end=" ")
    print( )