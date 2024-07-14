# def countNumber(num):
#     #  return len(str(num))

#   cnt=0
#   while num>0:
#     num= num//10
#     cnt+=1
#   return cnt

# num= int(input())
# ans = countNumber(num)
# print(ans)


#REVERSE A NUMBER

# def reverseNumber(num):
#   ans=0
#   while num>0:
#     rem=num%10
#     ans=ans*10+rem
#     num=num//10
#   return ans

# num= int(input())
# ans = reverseNumber(num)
# print(ans)

#Check Palindone

# def reverseNumber(num):
#   ans=0
#   while num>0:
#     rem=num%10
#     ans=ans*10+rem
#     num=num//10
#   return ans

# def pallindrome(num):
#   return num == reverseNumber(num)

# num= int(input())
# ans = pallindrome(num)
# print(ans)


#GCD or HCF

# def gcd(a,b):
#     divisor = min(a,b)
#     dividend = max(a,b)

#     while dividend%divisor!=0:
#        temp= dividend
#        dividend = divisor
#        divisor = temp%divisor
#     return divisor


# # num= int(input())
# ans = gcd(85,5)
# print(ans)


#Armstrong Number

# def armstrong(num):
#     ans=0
#     k= len(str(num))
#     temp = num

#     while num>0:
#       rem=num%10
#       ans= ans+rem**k
#       num=num//10
#     return temp==ans

# ans= armstrong(153)
# print(ans)

#Print all Divisors

# def numDivisor(num):
#    for i in range(1,num+1):
#       if num%i==0:
#          print(i)
   
# numDivisor(21)

#CHECK FOR THE PRIME

# def checkPrime(num):
#     if num <= 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# ans = checkPrime(17)
# print(ans)


#2nd apporach

# def checkPrime(num):
#     i=2
#     while i*i<=num:
#         if num % i == 0:
#             return False
#         i+=1
#     return True

# ans = checkPrime(12)
# print(ans)

#GIVEN A SERIES OF NUMBER. PRINT IT IS PRIME OR NOT.

# series= list[map(int,input().split())]

# def checkPrime(num):
#     i=2
#     while i*i<=num:
#         if num % i == 0:
#             return False
#         i+=1
#     return True

# for item in series:
#     ans=checkPrime(item)
#     print(item,ans)

#Complexcity= nlogn

# def countPrime(num):
#     cnt=0
#     for i in range(2,num+1):
#         if num%i==0:
#             cnt+=1


# ans=countPrime(17)
# print(ans)
    


          #RECURSION

# def printName(n):
#     if n==0:
#         return
#     print("Inspiration")
#     printName(n-1)

# printName(5)

#print 1 to N

# def printDigit(i,n):
#     if i>n:
#         return
#     print(i)
#     printDigit(i+1,n)

# printDigit(1,5)

#PRINT N TO 1

# def printDigit(n):
#     if n==0:
#         return
#     print(n)
#     printDigit(n-1)

# printDigit(8)

# 2nd aPPROARCH

# def printDigit(i,n):
#     if i>n:
#         return
#     printDigit(i+1,n)
#     print(i)

# printDigit(1,5)

#SUM OF 1ST N NOMBERS
# def sumNumber(i,n,sum=0):
#     if i>n:
#         print(sum)
#         return
#     sum=sum+i
#     sumNumber(i+1,n,sum)

# sumNumber(1,5)

# num=int(input())
# sum=0
# for i in range(1,num+1):
#     sum=sum+i
# print(sum)


# Factorail of A number n

# num=int(input())
# def fact(num):
#     ans=1
#     for i in range(1,num+1):
#         ans=ans*i
#     return ans

    

# result=fact(num)
# print(result)
    
#REVERSE AN ARRAY

# lst= list(map(int,input().split()))

# n=len(lst)

# for i in range(n//2):
#     lst[i],lst[n-1-i]= lst[n-1-i],lst[i]
#     #using a,b=b,a swap performed

# print(lst)


#TWO POINTER APPOROACH

# s=0
# e=n-1
# while s<=e:
#     lst[s],lst[e]=lst[e],lst[s]
#     s+=1
#     e-=1
# print(lst)

#Using Recurrsion

# def reverse(s,e,lst):
#     if s>e:
#         return
#     lst[s],lst[e]= lst[e],lst[s]
#     reverse(s+1,e-1,lst)

# reverse(s,e,lst)
# print(lst)
    
#CHECK PALLINDROME USING RECCURSSION

# string=input()

# def ispal(s,e,string):
#     if s>e:
#         return True
#     if string[s]!=string[e]:
#         return False
#     return ispal(s+1,e-1,string)

# ans=ispal(0,len(string)-1,string)
# print(ans)





    

