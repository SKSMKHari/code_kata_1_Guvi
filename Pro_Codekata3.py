str1=list(input("Enter String 1:"))
str2=list(input("Enter String 2:"))
ls1=len(str1)
ls2=len(str2)
var1=0
var2=0
arr=[]
while ls1>0:
    if str1[var1]==str2[var2]:
        arr.append(str1[var1])
    var2=var2+1
    var1=var1+1
    ls1=ls1-1
print(ls2-len(arr))
