l=[]
nof=int(input("Enter the no. of :"))
for i in range(0,nof):
	ipt=int(input("Enter the elements:"))
	l.append(ipt)
l.sort()
print(l[0])
