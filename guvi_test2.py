# your code goes here
a=int(input("Enter No. of Value"))
b=[]
l=[]
for i in range (0,a):
    c=int(input("Enter the values:"))
    b.append(c)
for j in b:
    if b.count(j)==1:
        l.append(j)
print(l[2])
