iv=int(input("Enter Initial Value:"))
fv=int(input("Enter Final Value:"))
rv=0
while True:
    iv=iv+1
    if iv%2==0:
        d=0
    elif iv>=fv:
        break
    else:
        rv+=1
print(rv)
