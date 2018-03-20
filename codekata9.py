v1=int(input('Enter the N value:'))
v2=int(input("enter the k value:"))
iv=[int(input()) for i in range(0,v1)]
if v2<v1:
    iv=iv[:v2]
    opt=sum(iv)
    print(opt)
else:
    print("wrong input:")
