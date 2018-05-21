# your code goes here
a=int(input())
b=[]
for i in range(0,a):
    c=int(input())
    b.append(c)
fp=b[:len(b)//2]
sp=b[len(b)//2:]
f=sum(fp)/len(fp)
s=sum(sp)/len(sp)
if f==s:
    print("Yes")
else:
    print("NA")
