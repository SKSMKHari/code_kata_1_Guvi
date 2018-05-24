nof=int(input("enter the no of elements:"))
arr=[]
for i in range(1,nof+1):
    ipt=int(input("enter the numbers:"))
    arr.append(ipt)
arr.sort()
mid=len(arr)//2
print(arr[mid])
