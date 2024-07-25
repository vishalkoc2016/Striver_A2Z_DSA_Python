arr=list(map(int,input().split()))
n=len(arr)

prefix=[0]*(n)

for i in range(n):
    if i==0:
        prefix[i]=arr[i]
    else:
        prefix[i]=arr[i]+prefix[i-1]
print(prefix)

# l=2
l=0
r=5

print(prefix[r]-prefix[l-1])

if l==0:
    print(prefix[r])