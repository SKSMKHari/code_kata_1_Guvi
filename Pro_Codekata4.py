str1=list(input("Enter String 1:"))
str2=list(input("Enter String 2:"))
lv1=len(str1)
v1=0
v2=0
while lv1>0:
    v1=v1+(ord(str2[v2])-ord(str1[v2]))
    v2=v2+1
    lv1=lv1-1
print(v1)
