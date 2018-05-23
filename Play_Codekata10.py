cnt=0
rv=0
str1=input("Enter String 1:").lower()
str2=input("Enter String 2:").lower()
if str1==str2:
    print("no")
else:
    for i in str1:
        if i==str2[rv]:
            rv+=1
        else:
            rv+=1
            cnt+=1
            if cnt>1:
                break
    if cnt==1:
        print ("yes")
    else:
        print ("no")
