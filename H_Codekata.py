list={}
arr=[]
ipt=int(input("Enter No. of:"))
for i in range(0,ipt):
    arr.append(int(input("Enter Values:")))
for i in arr:
    if i in list:
        list[i]+=1
    else:
        list[i]=1
for i in list:
    if list[i]==1:
        print (i)
        break
