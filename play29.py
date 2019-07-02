import math
l1=[int(i) for i in input().split()]
c1=0
n1=l1[1]+1
s1=l1[0]
for i in range(s1,n1):
    s1=math.sqrt(i)
    if(s1-math.floor(s1)==0):
        c1=c1+1
print(c1)
