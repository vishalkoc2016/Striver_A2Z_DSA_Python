n=int(input())
ans=""
while n>0:
    r=n%2
    ans=str(r)+ans
    n=n//2
print(ans)