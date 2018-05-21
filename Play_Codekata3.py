ipt = int(input("Enter Number to Reverse:"))
val=ipt
rvrs = 0
while(ipt > 0):
    rmdr = ipt %10
    rvrs = (rvrs *10) + rmdr
    ipt = ipt //10
print("reverse of %d is:" %val,rvrs)
