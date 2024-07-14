arr=[5,9,5,4,3,4,3,8]
print(arr)

d={}
for item in arr:
    d[item]=d.get(item,0)+1


#min aur max
mxcount=0
mxvalue=-1
# print(d.items())

mncount =1000000
mnvalue=None

for key,count in d.items():
    if mxcount<count:
        mxvalue=key
        mxcount=count

    if mncount>count:
        mnvalue=key
        mncount=count
print(mxcount,mxvalue)
print(mncount,mnvalue)


#Big(o) me sare chize ho jati hai isme 
# Next sorting Karenge


