flg=0
v1=0
opt=[]
v2=[]
a=int(input("Enter a Value:"))
for i in range(0,a):
    v2.append(int(input("Enter the Value:")))
for i in v2:
    if i==v1:
        opt.append(i)
        v1+=1
        flg=1
    else:
        v1+=1
if flg==0:
    print (-1)
else:
    opt.sort()
    print (opt)
