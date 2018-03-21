import numpy
arr=[]
nof=int(input("Enter no. of:"))
for i in range (0,nof):
    ipt=int(input("Enter the elements:"))
    arr.append(ipt)
med=numpy.median(arr)
print("Median Value:",med)
